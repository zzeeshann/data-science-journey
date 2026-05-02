"""
Session 8 — The Oldest Voices
=============================

Run this whole script in a single Colab cell on a T4 runtime.
(Runtime → Change runtime type → T4 GPU → Save, before running.)

Reuses the Session 7 pipeline (paragraph chunking, all-MiniLM-L6-v2,
cosine matrix) and extends it with a verified ancient-text corpus
loaded from ancient_voices/passages/ on the project repo.

Two pre-registered tests:
  Test 1 — 12-cluster falsification (permutation test on 4 pos-12
           passages vs the 15-passage ancient pool, with a sensitivity
           check excluding iching_hexagram_11).
  Test 2 — Cross-era resonance (paired-difference of each modern chunk's
           mean-cosine to pos-12 vs to wider ancient).

Produces:
  - Printed receipts (BEGIN_RECEIPTS / END_RECEIPTS) — paste into
    sessions/session_08.md "Raw outputs (receipts)"
  - chapter_08_cross_era.png — drop into book/images/

Reddit r/Meditation is expected to 403 (carry-over from Session 7).
The fetch is left in place so the receipts honestly show n=0.
Reddit is Session 9's problem.
"""

# ---------------------------------------------------------------------------
# 1. Install dependencies
# ---------------------------------------------------------------------------
import subprocess, sys
def pip(*pkgs):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *pkgs])

pip("sentence-transformers", "umap-learn")

# ---------------------------------------------------------------------------
# 2. Imports
# ---------------------------------------------------------------------------
import re, time, json, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import umap
import requests

RNG_SEED = 42
rng = np.random.default_rng(RNG_SEED)

# ---------------------------------------------------------------------------
# 3. Download the corpora
# ---------------------------------------------------------------------------

def fetch(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")

# 3a. Thinking in Wholes
TINW_URL = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/data/raw/thinking_in_wholes_2026.md"
tinw_text = fetch(TINW_URL)

# 3b. Ackoff lecture
ACKOFF_URL = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/data/raw/ackoff_lecture_systems_age.txt"
ackoff_text = fetch(ACKOFF_URL)

# 3c. William James 1890 — Project Gutenberg
JAMES_URL = "https://www.gutenberg.org/cache/epub/57628/pg57628.txt"
james_raw = fetch(JAMES_URL)
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
sp = james_raw.find(start_marker)
sp = james_raw.find("\n", sp) + 1
ep = james_raw.find(end_marker)
james_text = james_raw[sp:ep].strip()

# 3d. Reddit r/Meditation — kept in place from Session 7; expect HTTP 403
def fetch_reddit_meditation(target=300):
    posts = []
    seen = set()
    headers = {"User-Agent": "data-science-journey-research/1.0 (session 8)"}
    for sort in ["top", "hot", "new"]:
        for tparam in ([("t", "year"), ("t", "month")] if sort == "top" else [(None, None)]):
            url = f"https://www.reddit.com/r/Meditation/{sort}.json?limit=100"
            if tparam[0]:
                url += f"&{tparam[0]}={tparam[1]}"
            try:
                r = requests.get(url, headers=headers, timeout=30)
                if r.status_code != 200:
                    print(f"  reddit {sort} -> HTTP {r.status_code}")
                    continue
                data = r.json()
                for child in data["data"]["children"]:
                    d = child["data"]
                    pid = d.get("id")
                    txt = (d.get("selftext") or "").strip()
                    if (txt and pid not in seen
                            and not d.get("over_18") and not d.get("stickied")
                            and len(txt.split()) >= 20):
                        seen.add(pid)
                        posts.append(txt)
                time.sleep(2)
            except Exception as e:
                print(f"  reddit {sort} error: {e}")
            if len(posts) >= target:
                return posts
    return posts

reddit_posts = fetch_reddit_meditation(target=300)
print(f"Reddit r/Meditation posts pulled: {len(reddit_posts)}")

# 3e. Ancient Voices — verified passages from the project repo
ANCIENT_BASE = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/ancient_voices/passages/"

# (filename, text_id, position)
ANCIENT_FILES = [
    ("hammurabi_law_11.txt",                     "hammurabi",     "11"),
    ("hammurabi_law_12.txt",                     "hammurabi",     "12"),
    ("hammurabi_law_13.txt",                     "hammurabi",     "13"),
    ("enuma_elish_1_line_11.txt",                "enuma_elish",   "11"),
    ("enuma_elish_1_line_12.txt",                "enuma_elish",   "12"),
    ("enuma_elish_1_line_13.txt",                "enuma_elish",   "13"),
    ("iching_hexagram_11.txt",                   "iching",        "11"),
    ("iching_hexagram_12.txt",                   "iching",        "12"),
    ("iching_hexagram_13.txt",                   "iching",        "13"),
    ("inanna_descent_opening.txt",               "inanna",        "12"),
    ("pyramid_texts_unas_utterance_213.txt",     "pyramid_texts", "wider"),
    ("pyramid_texts_unas_utterance_217.txt",     "pyramid_texts", "wider"),
    ("gilgamesh_pennsylvania_tablet_dream.txt",  "gilgamesh",     "wider"),
    ("ugaritic_ktu_1_4_baal_to_mot.txt",         "ugaritic",      "wider"),
    ("ugaritic_ktu_1_23_invocation.txt",         "ugaritic",      "wider"),
]

def parse_passage(raw):
    """Split header from body on the first blank line; collapse whitespace."""
    parts = raw.split("\n\n", 1)
    body = parts[1] if len(parts) == 2 else parts[0]
    return re.sub(r"\s+", " ", body).strip()

ancient_records = []
for fname, text_id, pos in ANCIENT_FILES:
    raw = fetch(ANCIENT_BASE + fname)
    body = parse_passage(raw)
    ancient_records.append({
        "source": "ancient",
        "text": body,
        "text_id": text_id,
        "position": pos,
        "filename": fname,
    })
print(f"Ancient passages loaded: {len(ancient_records)}")

# ---------------------------------------------------------------------------
# 4. Chunking — paragraph-level for modern; one-chunk-per-file for ancient
# ---------------------------------------------------------------------------

def chunk_paragraphs(text, min_words=20, max_words=300):
    paras = re.split(r"\n\s*\n", text)
    out = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        clean = re.sub(r"\s+", " ", p)
        n = len(clean.split())
        if min_words <= n <= max_words:
            out.append(clean)
    return out

tinw_chunks    = chunk_paragraphs(tinw_text)
ackoff_chunks  = chunk_paragraphs(ackoff_text)
james_chunks   = chunk_paragraphs(james_text)
reddit_chunks  = [re.sub(r"\s+", " ", p).strip() for p in reddit_posts]
reddit_chunks  = [c for c in reddit_chunks if 20 <= len(c.split()) <= 300]

print()
print("Chunk counts:")
print(f"  Thinking in Wholes : {len(tinw_chunks)}")
print(f"  Ackoff lecture     : {len(ackoff_chunks)}")
print(f"  James 1890         : {len(james_chunks)}")
print(f"  Reddit Meditation  : {len(reddit_chunks)}")
print(f"  Ancient Voices     : {len(ancient_records)}")

# Build the master DataFrame (uniform schema with text_id + position columns).
records = (
    [{"source": "tinw",   "text": c, "text_id": "", "position": ""} for c in tinw_chunks]
  + [{"source": "ackoff", "text": c, "text_id": "", "position": ""} for c in ackoff_chunks]
  + [{"source": "james",  "text": c, "text_id": "", "position": ""} for c in james_chunks]
  + [{"source": "reddit", "text": c, "text_id": "", "position": ""} for c in reddit_chunks]
  + [{"source": r["source"], "text": r["text"],
      "text_id": r["text_id"], "position": r["position"]} for r in ancient_records]
)
df = pd.DataFrame(records).reset_index(drop=True)
print(f"  TOTAL chunks       : {len(df)}")

# ---------------------------------------------------------------------------
# 5. Embed — all-MiniLM-L6-v2
# ---------------------------------------------------------------------------

MODEL_NAME = "all-MiniLM-L6-v2"
print(f"\nLoading {MODEL_NAME} ...")
model = SentenceTransformer(MODEL_NAME)
print("Embedding all chunks...")
t0 = time.time()
vectors = model.encode(df["text"].tolist(), batch_size=64, show_progress_bar=True,
                       convert_to_numpy=True, normalize_embeddings=True)
print(f"Embeddings shape: {vectors.shape}    elapsed: {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 6. Pairwise cosine similarity
# ---------------------------------------------------------------------------

sim = vectors @ vectors.T
np.fill_diagonal(sim, -1.0)

# ---------------------------------------------------------------------------
# 7. Indices and helpers for the ancient tests
# ---------------------------------------------------------------------------

anc_mask  = (df["source"] == "ancient").to_numpy()
anc_idx   = np.where(anc_mask)[0]
pos12_idx = df.index[(df["source"] == "ancient") & (df["position"] == "12")].to_numpy()
pos11_idx = df.index[(df["source"] == "ancient") & (df["position"] == "11")].to_numpy()
pos13_idx = df.index[(df["source"] == "ancient") & (df["position"] == "13")].to_numpy()
wider_idx = df.index[(df["source"] == "ancient") & (df["position"] == "wider")].to_numpy()
non12_idx = np.concatenate([pos11_idx, pos13_idx, wider_idx])  # the wider-ancient pool

iching_hex11_idx = df.index[(df["text_id"] == "iching") & (df["position"] == "11")].to_numpy()

def mean_pairwise(indices):
    if len(indices) < 2:
        return float("nan")
    sub = sim[np.ix_(indices, indices)]
    iu = np.triu_indices(len(indices), k=1)
    return float(sub[iu].mean())

def mean_between(a_idx, b_idx):
    if len(a_idx) == 0 or len(b_idx) == 0:
        return float("nan")
    return float(sim[np.ix_(a_idx, b_idx)].mean())

def same_text_pos_to_pos(pos_a_label, pos_b_label):
    """Mean cosine between each text's pos_a passage and the same text's pos_b passage."""
    pairs = []
    for tid in df.loc[df["source"] == "ancient", "text_id"].unique():
        a = df.index[(df["text_id"] == tid) & (df["position"] == pos_a_label)].tolist()
        b = df.index[(df["text_id"] == tid) & (df["position"] == pos_b_label)].tolist()
        if a and b:
            pairs.append(float(sim[a[0], b[0]]))
    if not pairs:
        return float("nan"), 0
    return float(np.mean(pairs)), len(pairs)

# ---------------------------------------------------------------------------
# 8. Helpers for top-N pair receipts (Session 7 pattern)
# ---------------------------------------------------------------------------

def top_pairs(n, where_a=None, where_b=None):
    a_mask = np.ones(len(df), dtype=bool) if where_a is None else (df["source"] == where_a).to_numpy()
    b_mask = np.ones(len(df), dtype=bool) if where_b is None else (df["source"] == where_b).to_numpy()
    M = sim.copy()
    mask = np.outer(a_mask, b_mask)
    if where_a == where_b and where_a is not None:
        mask = np.triu(mask, k=1)
    M = np.where(mask, M, -2.0)
    flat = M.flatten()
    order = np.argsort(flat)[::-1]
    seen_pairs = set()
    out = []
    for idx in order:
        i, j = divmod(idx, len(df))
        if i == j:
            continue
        key = tuple(sorted((i, j)))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        if M[i, j] < -1.5:
            break
        out.append((float(M[i, j]), int(i), int(j)))
        if len(out) >= n:
            break
    return out

def top_modern_to_pos12(n):
    """Top-N pairs where one side is modern (tinw/ackoff/james) and the other is pos-12."""
    modern_mask = df["source"].isin(["tinw", "ackoff", "james"]).to_numpy()
    M = sim.copy()
    mask = np.outer(modern_mask, np.isin(np.arange(len(df)), pos12_idx))
    mask = mask | mask.T  # either direction
    M = np.where(mask, M, -2.0)
    np.fill_diagonal(M, -2.0)
    flat = M.flatten()
    order = np.argsort(flat)[::-1]
    seen_pairs = set()
    out = []
    for idx in order:
        i, j = divmod(idx, len(df))
        if i == j:
            continue
        key = tuple(sorted((i, j)))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        if M[i, j] < -1.5:
            break
        # canonicalise: modern first, ancient second
        a, b = (i, j) if df.loc[i, "source"] in ("tinw", "ackoff", "james") else (j, i)
        out.append((float(M[i, j]), a, b))
        if len(out) >= n:
            break
    return out

def show_pair(label, pairs, max_chars=240):
    print(f"\n--- {label} ---")
    for k, (s, i, j) in enumerate(pairs, 1):
        a = df.loc[i]; b = df.loc[j]
        ta = a["text"][:max_chars] + ("…" if len(a["text"]) > max_chars else "")
        tb = b["text"][:max_chars] + ("…" if len(b["text"]) > max_chars else "")
        a_label = f"{a['source']}#{i}" if a["source"] != "ancient" else f"ancient/{a['text_id']}-{a['position']}"
        b_label = f"{b['source']}#{j}" if b["source"] != "ancient" else f"ancient/{b['text_id']}-{b['position']}"
        print(f"[{k}] cos={s:+.4f}   {a_label}   ↔   {b_label}")
        print(f"    A: {ta}")
        print(f"    B: {tb}")

# ---------------------------------------------------------------------------
# 9. Permutation test
# ---------------------------------------------------------------------------

def perm_test(pool_indices, observed, sample_size, n_perm=10000):
    means = np.empty(n_perm)
    pool = np.asarray(pool_indices)
    for k in range(n_perm):
        s = rng.choice(pool, size=sample_size, replace=False)
        means[k] = mean_pairwise(s)
    pct = float((means < observed).mean() * 100.0)
    p   = float((means >= observed).mean())
    return pct, p, float(means.mean()), float(means.std()), means

# ---------------------------------------------------------------------------
# 10. The receipts
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("BEGIN_RECEIPTS — copy everything below into sessions/session_08.md")
print("=" * 72)

print(f"\nMODEL: {MODEL_NAME}")
print(f"RANDOM_SEED: {RNG_SEED}")
print(f"VECTOR DIM: {vectors.shape[1]}")
print(f"TOTAL CHUNKS: {len(df)}    "
      f"(tinw={len(tinw_chunks)}, ackoff={len(ackoff_chunks)}, "
      f"james={len(james_chunks)}, reddit={len(reddit_chunks)}, "
      f"ancient={len(ancient_records)})")
print(f"ANCIENT BREAKDOWN: position-12 n={len(pos12_idx)}, "
      f"position-11 n={len(pos11_idx)}, position-13 n={len(pos13_idx)}, "
      f"wider n={len(wider_idx)}")
print(f"ANCIENT pos-12 members: "
      f"{[(df.loc[i,'text_id']) for i in pos12_idx]}")

print("\n--- PRE-REGISTERED PREDICTIONS (printed BEFORE running tests) ---")
print(
    "Test 1 — sim_12 will fall above the 95th percentile of the\n"
    "  permutation distribution (one-sided p < 0.05). Sensitivity:\n"
    "  result reported both with and without iching_hexagram_11 in the pool.\n"
    "Test 2 — across modern chunks, paired-difference\n"
    "  (mean cosine to position-12) − (mean cosine to wider ancient)\n"
    "  will have a positive mean with 95% bootstrap CI excluding zero."
)

# ----- Test 1 -----
sim_12 = mean_pairwise(pos12_idx)
sim_11 = mean_pairwise(pos11_idx)
sim_13 = mean_pairwise(pos13_idx)
sim_12_to_11_mean, n_12_to_11 = same_text_pos_to_pos("12", "11")
sim_12_to_13_mean, n_12_to_13 = same_text_pos_to_pos("12", "13")

print("\n--- TEST 1 — 12-cluster falsification ---")
print(f"  sim_12       (n={len(pos12_idx)} passages, n_pairs={len(pos12_idx)*(len(pos12_idx)-1)//2}) : {sim_12:+.4f}")
print(f"  sim_11       (n={len(pos11_idx)} passages, n_pairs={len(pos11_idx)*(len(pos11_idx)-1)//2}) : {sim_11:+.4f}")
print(f"  sim_13       (n={len(pos13_idx)} passages, n_pairs={len(pos13_idx)*(len(pos13_idx)-1)//2}) : {sim_13:+.4f}")
print(f"  sim_12_to_11 (same-text pairs, n={n_12_to_11})                          : {sim_12_to_11_mean:+.4f}")
print(f"  sim_12_to_13 (same-text pairs, n={n_12_to_13})                          : {sim_12_to_13_mean:+.4f}")

# Permutation — including iching_hex_11
pct_in, p_in, mu_in, sd_in, _ = perm_test(anc_idx, sim_12, sample_size=len(pos12_idx))
print(f"\n  Permutation — INCLUDING iching_hexagram_11 in pool")
print(f"    pool size: {len(anc_idx)}, sample size: {len(pos12_idx)}, n_perm: 10000")
print(f"    sim_12 percentile in null distribution : {pct_in:.2f}")
print(f"    one-sided p (perm_mean ≥ sim_12)       : {p_in:.4f}")
print(f"    permutation mean ± std                 : {mu_in:+.4f} ± {sd_in:.4f}")

# Permutation — excluding iching_hex_11
if len(iching_hex11_idx) > 0:
    pool_ex = np.array([i for i in anc_idx if i != iching_hex11_idx[0]])
else:
    pool_ex = anc_idx
pct_ex, p_ex, mu_ex, sd_ex, _ = perm_test(pool_ex, sim_12, sample_size=len(pos12_idx))
print(f"\n  Permutation — EXCLUDING iching_hexagram_11 from pool (sensitivity)")
print(f"    pool size: {len(pool_ex)}, sample size: {len(pos12_idx)}, n_perm: 10000")
print(f"    sim_12 percentile in null distribution : {pct_ex:.2f}")
print(f"    one-sided p (perm_mean ≥ sim_12)       : {p_ex:.4f}")
print(f"    permutation mean ± std                 : {mu_ex:+.4f} ± {sd_ex:.4f}")

# ----- Test 2 -----
modern_mask = df["source"].isin(["tinw", "ackoff", "james"]).to_numpy()
modern_idx  = np.where(modern_mask)[0]

m_to_12    = sim[np.ix_(modern_idx, pos12_idx)].mean(axis=1)
m_to_wider = sim[np.ix_(modern_idx, non12_idx)].mean(axis=1)
paired    = m_to_12 - m_to_wider

# Bootstrap 95% CI
boots = np.array([rng.choice(paired, size=len(paired), replace=True).mean()
                  for _ in range(10000)])
ci_lo, ci_hi = float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))

# Sign-flip permutation p
signs = rng.choice([-1.0, 1.0], size=(10000, len(paired)))
null_means = (signs * paired).mean(axis=1)
p_signflip = float((null_means >= paired.mean()).mean())

print("\n--- TEST 2 — Cross-era resonance ---")
print(f"  modern chunks tested: {len(modern_idx)}  "
      f"(tinw={(df.loc[modern_idx,'source']=='tinw').sum()}, "
      f"ackoff={(df.loc[modern_idx,'source']=='ackoff').sum()}, "
      f"james={(df.loc[modern_idx,'source']=='james').sum()})")
print(f"  per-corpus paired-difference (mean_to_pos12 − mean_to_wider):")
for src in ["tinw", "ackoff", "james"]:
    m = (df.loc[modern_idx, "source"] == src).to_numpy()
    if m.sum() == 0:
        continue
    sub = paired[m]
    pos_frac = float((sub > 0).mean())
    print(f"    {src:6s}: mean={sub.mean():+.4f}  median={np.median(sub):+.4f}  "
          f"pct_positive={pos_frac:.3f}  n={m.sum()}")
print(f"  overall paired diff (all modern chunks)   : mean={paired.mean():+.4f}")
print(f"  bootstrap 95% CI on paired-diff mean      : [{ci_lo:+.4f}, {ci_hi:+.4f}]")
print(f"  sign-flip permutation p (one-sided)        : {p_signflip:.4f}")

# Sanity reference: the within-corpus and cross-corpus means (rough texture)
print("\n--- Reference — mean within-source cosine ---")
for src in ["tinw", "ackoff", "james", "reddit", "ancient"]:
    idx = (df["source"] == src).to_numpy()
    if idx.sum() < 2:
        print(f"  {src:8s}: n/a (only {idx.sum()} chunk(s))")
        continue
    sub = sim[np.ix_(idx, idx)]
    iu = np.triu_indices(sub.shape[0], k=1)
    print(f"  {src:8s}: {sub[iu].mean():+.4f}  (n_pairs={len(iu[0])})")

print("\n--- Reference — mean cross-source cosine ---")
sources = ["tinw", "ackoff", "james", "ancient"]
for a in sources:
    for b in sources:
        if a >= b:
            continue
        ia = (df["source"] == a).to_numpy()
        ib = (df["source"] == b).to_numpy()
        if ia.sum() == 0 or ib.sum() == 0:
            continue
        sub = sim[np.ix_(ia, ib)]
        print(f"  {a:8s} ↔ {b:8s}: {sub.mean():+.4f}  (n_pairs={sub.size})")

# Top-5 modern ↔ position-12 pairs (qualitative receipts)
show_pair("Top 5 modern ↔ position-12 pairs (FULL TEXT)", top_modern_to_pos12(5))

# ---------------------------------------------------------------------------
# 11. UMAP — combined modern + ancient embedding space
# ---------------------------------------------------------------------------

print("\nFitting UMAP (2D)...")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric="cosine", random_state=RNG_SEED)
xy = reducer.fit_transform(vectors)

modern_palette = {
    "tinw":   "#1f77b4",
    "ackoff": "#9467bd",
    "james":  "#d62728",
}
modern_labels = {
    "tinw":   "Thinking in Wholes",
    "ackoff": "Ackoff lecture",
    "james":  "James 1890",
}
ANCIENT_COLOR = "#e07a1f"

fig, ax = plt.subplots(figsize=(10, 7))

# Modern points
for src, colour in modern_palette.items():
    m = (df["source"] == src).to_numpy()
    if m.sum() == 0:
        continue
    ax.scatter(xy[m, 0], xy[m, 1], s=14, alpha=0.45,
               c=colour, label=f"{modern_labels[src]} (n={m.sum()})",
               edgecolors="white", linewidths=0.3)

# Ancient points — three marker shapes (12 / control / wider)
ancient_groups = [
    ("position 12 (n={})".format(len(pos12_idx)), pos12_idx, "*", 240, 1.0),
    ("position 11 or 13 (control, n={})".format(len(pos11_idx) + len(pos13_idx)),
     np.concatenate([pos11_idx, pos13_idx]) if (len(pos11_idx) + len(pos13_idx)) else np.array([], dtype=int),
     "D", 110, 0.6),
    ("wider sample (n={})".format(len(wider_idx)), wider_idx, "s", 80, 0.4),
]
for label, idxs, marker, size, lw in ancient_groups:
    if len(idxs) == 0:
        continue
    ax.scatter(xy[idxs, 0], xy[idxs, 1], s=size, marker=marker,
               c=ANCIENT_COLOR, label=label,
               edgecolors="black", linewidths=lw, zorder=5)

# Annotate each ancient point with a short label
def short_label(text_id, position):
    tid_short = {
        "hammurabi": "ham", "enuma_elish": "enuma", "iching": "iching",
        "inanna": "inanna", "pyramid_texts": "pyramid",
        "gilgamesh": "gilgamesh", "ugaritic": "ugaritic",
    }.get(text_id, text_id)
    pos_short = position if position != "wider" else "w"
    return f"{tid_short}-{pos_short}"

for i in anc_idx:
    label = short_label(df.loc[i, "text_id"], df.loc[i, "position"])
    ax.annotate(label, (xy[i, 0], xy[i, 1]),
                fontsize=7, xytext=(4, 4), textcoords="offset points",
                color="black", zorder=6)

ax.set_xlabel("UMAP-1")
ax.set_ylabel("UMAP-2")
ax.set_title("Cross-era embedding landscape — modern wholeness texts and 15 ancient passages")
ax.legend(loc="best", frameon=True, fontsize=8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
out_path = "/content/chapter_08_cross_era.png" if "google.colab" in sys.modules else "chapter_08_cross_era.png"
plt.savefig(out_path, dpi=160, bbox_inches="tight")
plt.show()
print(f"Chart saved: {out_path}")

print("\n" + "=" * 72)
print("END_RECEIPTS")
print("=" * 72)

# ---------------------------------------------------------------------------
# 12. Trigger download of the chart
# ---------------------------------------------------------------------------

try:
    from google.colab import files
    files.download(out_path)
except Exception:
    print("(not in Colab — chart is in the working directory)")
