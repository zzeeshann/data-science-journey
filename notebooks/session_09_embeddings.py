"""
Session 9 — Reddit Lands: the modern lay-language voice
========================================================

Run this whole script in a single Colab cell on a T4 runtime.
(Runtime → Change runtime type → T4 GPU → Save, before running.)

Reuses the Session 7/8 pipeline. The change vs. Session 8:
  - Reddit r/Meditation is now loaded from the HuggingFace dataset
    `sentence-transformers/reddit-title-body` (Pushshift-sourced,
    pre-quality-filtered, mid-2010 → mid-2021), filtered to
    subreddit == "Meditation". This is the deferred-from-Session-7
    fix for the anonymous-JSON HTTP 403.

Three pre-registered tests:
  Test 1 — Reddit-as-modern-lay-voice descriptive landing.
           Where does r/Meditation sit relative to (a) the modern
           systems-thinking cluster (tinw, ackoff), (b) James 1890,
           (c) the ancient corpus? Reported via mean cross-source
           cosines and top-N pairs.
  Test 2 — Translation-register confound retest.
           Session 8 found a paired-diff lift in modern↔pos-12
           ancient, but the top-5 pairs were ALL James 1890 ↔
           I Ching hex-12 (Legge 1899). If the lift is a wholeness-
           register signal, Reddit (post-2010 modern English, no
           Victorian-prose match) should also show paired-diff > 0
           toward position-12 ancient passages at similar magnitude
           to tinw and ackoff. If it's a translation-register
           artefact, Reddit's paired-diff will be near zero or
           negative.
  Test 3 — H3 cross-era resonance, full version.
           With Reddit now in the matrix, run the same paired-
           difference test from Session 8 across all four modern
           corpora (tinw, ackoff, james, reddit), reporting per-
           corpus and aggregate.

Produces:
  - Printed receipts (BEGIN_RECEIPTS / END_RECEIPTS) → paste into
    sessions/session_09.md "Raw outputs (receipts)"
  - chapter_09_full_landscape.png — UMAP scatter, all five corpora
    finally in one frame.
"""

# ---------------------------------------------------------------------------
# 1. Install dependencies
# ---------------------------------------------------------------------------
import subprocess, sys
def pip(*pkgs):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *pkgs])

pip("sentence-transformers", "umap-learn", "datasets")

# ---------------------------------------------------------------------------
# 2. Imports
# ---------------------------------------------------------------------------
import re, time, os, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import umap
from datasets import load_dataset

RNG_SEED = 42
rng = np.random.default_rng(RNG_SEED)

# Optional HF token from Colab secrets (anonymous works too for this dataset)
try:
    from google.colab import userdata
    hf_token = userdata.get("HF_TOKEN")
    if hf_token:
        os.environ["HF_TOKEN"] = hf_token
        print("HF_TOKEN loaded from Colab secrets.")
    else:
        print("No HF_TOKEN in Colab secrets — using anonymous access.")
except Exception:
    print("Not in Colab — skipping HF_TOKEN lookup.")

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

# 3d. Reddit r/Meditation — HuggingFace dataset (replaces Session 7/8 broken anonymous API)
def fetch_reddit_meditation_hf(target=300, max_scan=500_000):
    """Stream sentence-transformers/reddit-title-body, keep r/Meditation
    posts whose body fits the 20–300 word filter, until we hit `target`."""
    print(f"Streaming sentence-transformers/reddit-title-body, "
          f"filtering subreddit==Meditation, target {target}...")
    ds = load_dataset(
        "sentence-transformers/reddit-title-body",
        split="train",
        streaming=True,
    )
    posts = []
    scanned = 0
    matched = 0  # Meditation rows seen, regardless of word filter
    t0 = time.time()
    for row in ds:
        scanned += 1
        if scanned % 20000 == 0:
            print(f"  scanned {scanned:,} rows | "
                  f"Meditation rows seen: {matched} | "
                  f"kept (20–300w): {len(posts)} | "
                  f"{time.time()-t0:.0f}s")
        if str(row.get("subreddit", "")).lower() != "meditation":
            continue
        matched += 1
        body = row.get("body", "") or ""
        body = re.sub(r"\s+", " ", body).strip()
        if not body:
            continue
        n_words = len(body.split())
        if 20 <= n_words <= 300:
            posts.append(body)
        if len(posts) >= target:
            break
        if scanned >= max_scan:
            print(f"  Hit safety bound {max_scan:,} rows; stopping early.")
            break
    print(f"Reddit r/Meditation posts loaded: {len(posts)}  "
          f"(scanned {scanned:,} rows, {matched} Meditation rows seen)")
    return posts

reddit_posts = fetch_reddit_meditation_hf(target=300)

# ---------------------------------------------------------------------------
# 3e. Ancient Voices — verified passages from the project repo
# ---------------------------------------------------------------------------
ANCIENT_BASE = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/ancient_voices/passages/"

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
# Reddit posts already arrive cleaned and word-filtered from the loader.
reddit_chunks  = list(reddit_posts)

print()
print("Chunk counts:")
print(f"  Thinking in Wholes : {len(tinw_chunks)}")
print(f"  Ackoff lecture     : {len(ackoff_chunks)}")
print(f"  James 1890         : {len(james_chunks)}")
print(f"  Reddit Meditation  : {len(reddit_chunks)}")
print(f"  Ancient Voices     : {len(ancient_records)}")

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
# 7. Indices and helpers
# ---------------------------------------------------------------------------

anc_mask  = (df["source"] == "ancient").to_numpy()
anc_idx   = np.where(anc_mask)[0]
pos12_idx = df.index[(df["source"] == "ancient") & (df["position"] == "12")].to_numpy()
pos11_idx = df.index[(df["source"] == "ancient") & (df["position"] == "11")].to_numpy()
pos13_idx = df.index[(df["source"] == "ancient") & (df["position"] == "13")].to_numpy()
wider_idx = df.index[(df["source"] == "ancient") & (df["position"] == "wider")].to_numpy()
non12_idx = np.concatenate([pos11_idx, pos13_idx, wider_idx])

modern_corpora = ["tinw", "ackoff", "james", "reddit"]

def mean_pairwise(indices):
    if len(indices) < 2:
        return float("nan")
    sub = sim[np.ix_(indices, indices)]
    iu = np.triu_indices(len(indices), k=1)
    return float(sub[iu].mean())

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

def top_modern_to_pos12(n, modern_source=None):
    """Top-N pairs where one side is a modern corpus and the other is pos-12.
    If modern_source is set, restrict to that one."""
    if modern_source is None:
        modern_mask = df["source"].isin(modern_corpora).to_numpy()
    else:
        modern_mask = (df["source"] == modern_source).to_numpy()
    M = sim.copy()
    pos12_mask = np.isin(np.arange(len(df)), pos12_idx)
    mask = np.outer(modern_mask, pos12_mask) | np.outer(pos12_mask, modern_mask)
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
        a, b = (i, j) if df.loc[i, "source"] in modern_corpora else (j, i)
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

def paired_diff_for_corpus(src):
    """Per-corpus paired-difference: cosine to pos-12 minus cosine to wider ancient."""
    idx = np.where((df["source"] == src).to_numpy())[0]
    if len(idx) == 0 or len(pos12_idx) == 0 or len(non12_idx) == 0:
        return None
    m_to_12    = sim[np.ix_(idx, pos12_idx)].mean(axis=1)
    m_to_wider = sim[np.ix_(idx, non12_idx)].mean(axis=1)
    return m_to_12 - m_to_wider

# ---------------------------------------------------------------------------
# 8. The receipts
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("BEGIN_RECEIPTS — copy everything below into sessions/session_09.md")
print("=" * 72)

print(f"\nMODEL: {MODEL_NAME}")
print(f"RANDOM_SEED: {RNG_SEED}")
print(f"VECTOR DIM: {vectors.shape[1]}")
print(f"TOTAL CHUNKS: {len(df)}    "
      f"(tinw={len(tinw_chunks)}, ackoff={len(ackoff_chunks)}, "
      f"james={len(james_chunks)}, reddit={len(reddit_chunks)}, "
      f"ancient={len(ancient_records)})")
print(f"REDDIT SOURCE: HF dataset sentence-transformers/reddit-title-body, "
      f"streamed and filtered to subreddit=='Meditation', body 20–300 words")
print(f"ANCIENT BREAKDOWN: position-12 n={len(pos12_idx)}, "
      f"position-11 n={len(pos11_idx)}, position-13 n={len(pos13_idx)}, "
      f"wider n={len(wider_idx)}")

print("\n--- PRE-REGISTERED PREDICTIONS (printed BEFORE the tests) ---")
print(
    "Test 1 — Reddit-as-modern-lay-voice landing.\n"
    "  Descriptive, no falsifiable prediction. Reported via mean cross-source\n"
    "  cosines and top-N pairs.\n"
    "Test 2 — Translation-register confound retest.\n"
    "  IF the modern↔pos-12 lift from Session 8 is a wholeness-register\n"
    "  signal, Reddit (post-2010 modern English) will show paired-diff > 0\n"
    "  toward pos-12 ancient passages, with magnitude in the same band\n"
    "  as tinw (+0.0154) and ackoff (+0.0176). IF the lift is a Victorian-\n"
    "  English / Legge-1899 translation-register artefact, Reddit's paired-\n"
    "  diff will be near zero or negative, while James's lift remains.\n"
    "Test 3 — H3 cross-era resonance, full version.\n"
    "  Aggregate paired-diff across all four modern corpora is expected to\n"
    "  remain positive (the Session 8 result was robust to bootstrap CI),\n"
    "  but the magnitude may shift if Reddit dilutes or amplifies it."
)

# ----- Test 1 — descriptive landing -----

print("\n--- TEST 1 — Where Reddit lands (descriptive) ---")

# Reddit's within-source mean cosine — a coherence sanity check
red_idx = np.where((df["source"] == "reddit").to_numpy())[0]
within_red = mean_pairwise(red_idx)
print(f"  Mean within-Reddit cosine: {within_red:+.4f}  "
      f"(n={len(red_idx)} chunks, n_pairs={len(red_idx)*(len(red_idx)-1)//2})")

# Mean Reddit ↔ each other corpus
print("  Mean Reddit ↔ each other corpus:")
for src in ["tinw", "ackoff", "james", "ancient"]:
    other = np.where((df["source"] == src).to_numpy())[0]
    if len(other) == 0 or len(red_idx) == 0:
        continue
    sub = sim[np.ix_(red_idx, other)]
    print(f"    reddit ↔ {src:8s}: {sub.mean():+.4f}  (n_pairs={sub.size})")

# Top pairs Reddit ↔ tinw, ackoff, james, ancient
show_pair("Top 5 Reddit ↔ Thinking in Wholes",  top_pairs(5, "reddit", "tinw"))
show_pair("Top 5 Reddit ↔ Ackoff",              top_pairs(5, "reddit", "ackoff"))
show_pair("Top 5 Reddit ↔ James 1890",          top_pairs(5, "reddit", "james"))
show_pair("Top 5 Reddit ↔ Ancient (any)",       top_pairs(5, "reddit", "ancient"))

# ----- Test 2 — Translation-register confound retest -----

print("\n--- TEST 2 — Translation-register confound retest ---")
print("  Per-corpus paired-difference (mean_to_pos12 − mean_to_wider):")

per_corpus_stats = {}
for src in modern_corpora:
    pd_vec = paired_diff_for_corpus(src)
    if pd_vec is None or len(pd_vec) == 0:
        continue
    per_corpus_stats[src] = pd_vec
    pos_frac = float((pd_vec > 0).mean())
    print(f"    {src:6s}: mean={pd_vec.mean():+.4f}  median={np.median(pd_vec):+.4f}  "
          f"pct_positive={pos_frac:.3f}  n={len(pd_vec)}")

print("\n  Top 5 Reddit ↔ position-12 ancient pairs (the falsification target):")
show_pair("Top 5 Reddit ↔ position-12 ancient", top_modern_to_pos12(5, modern_source="reddit"))

# ----- Test 3 — Aggregate cross-era -----

print("\n--- TEST 3 — Aggregate cross-era resonance (all 4 modern corpora) ---")
all_modern_idx = np.where(df["source"].isin(modern_corpora).to_numpy())[0]
all_to_12    = sim[np.ix_(all_modern_idx, pos12_idx)].mean(axis=1)
all_to_wider = sim[np.ix_(all_modern_idx, non12_idx)].mean(axis=1)
all_paired   = all_to_12 - all_to_wider

# Bootstrap 95% CI
boots = np.array([rng.choice(all_paired, size=len(all_paired), replace=True).mean()
                  for _ in range(10000)])
ci_lo, ci_hi = float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))

# Sign-flip permutation p
signs = rng.choice([-1.0, 1.0], size=(10000, len(all_paired)))
null_means = (signs * all_paired).mean(axis=1)
p_signflip = float((null_means >= all_paired.mean()).mean())

print(f"  modern chunks tested: {len(all_modern_idx)}  "
      f"(across tinw/ackoff/james/reddit)")
print(f"  overall paired diff (mean)             : {all_paired.mean():+.4f}")
print(f"  bootstrap 95% CI on paired-diff mean   : [{ci_lo:+.4f}, {ci_hi:+.4f}]")
print(f"  sign-flip permutation p (one-sided)    : {p_signflip:.4f}")

# ----- Reference cosines -----

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
sources = ["tinw", "ackoff", "james", "reddit", "ancient"]
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

# Top within-Reddit (sanity check on coherence)
show_pair("Top 5 within Reddit (sanity check)", top_pairs(5, "reddit", "reddit"))

# ---------------------------------------------------------------------------
# 9. UMAP — the full landscape, all five corpora
# ---------------------------------------------------------------------------

print("\nFitting UMAP (2D)...")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric="cosine", random_state=RNG_SEED)
xy = reducer.fit_transform(vectors)

modern_palette = {
    "tinw":   "#1f77b4",
    "ackoff": "#9467bd",
    "james":  "#d62728",
    "reddit": "#2ca02c",
}
modern_labels = {
    "tinw":   "Thinking in Wholes",
    "ackoff": "Ackoff lecture",
    "james":  "James 1890",
    "reddit": "Reddit r/Meditation",
}
ANCIENT_COLOR = "#e07a1f"

fig, ax = plt.subplots(figsize=(10, 7))

for src, colour in modern_palette.items():
    m = (df["source"] == src).to_numpy()
    if m.sum() == 0:
        continue
    ax.scatter(xy[m, 0], xy[m, 1], s=14, alpha=0.45,
               c=colour, label=f"{modern_labels[src]} (n={m.sum()})",
               edgecolors="white", linewidths=0.3)

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
ax.set_title("Full landscape — three modern corpora, Reddit r/Meditation, and 15 ancient passages")
ax.legend(loc="best", frameon=True, fontsize=8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
out_path = "/content/chapter_09_full_landscape.png" if "google.colab" in sys.modules else "chapter_09_full_landscape.png"
plt.savefig(out_path, dpi=160, bbox_inches="tight")
plt.show()
print(f"Chart saved: {out_path}")

print("\n" + "=" * 72)
print("END_RECEIPTS")
print("=" * 72)

# ---------------------------------------------------------------------------
# 10. Trigger download of the chart
# ---------------------------------------------------------------------------

try:
    from google.colab import files
    files.download(out_path)
except Exception:
    print("(not in Colab — chart is in the working directory)")
