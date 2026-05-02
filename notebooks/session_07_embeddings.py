"""
Session 7 — Embeddings: First Encounter
=======================================

Run this whole script in a single Colab cell on a T4 runtime.
(Runtime → Change runtime type → T4 GPU → Save, before running.)

Produces:
  - Printed receipts for sessions/session_07.md
  - chapter_07_embedding_landscape.png saved to /content/
  - At the end: triggers files.download() for the chart

Paste the printed output (everything between BEGIN_RECEIPTS and END_RECEIPTS)
back into the Claude Code conversation. Drop the downloaded PNG into
book/images/chapter_07_embedding_landscape.png in the local repo.
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

# ---------------------------------------------------------------------------
# 3. Download the four corpora
# ---------------------------------------------------------------------------

def fetch(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")

# 3a. Thinking in Wholes — from the GitHub raw URL of the project repo
TINW_URL = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/data/raw/thinking_in_wholes_2026.md"
tinw_text = fetch(TINW_URL)

# 3b. Ackoff lecture — same project repo
ACKOFF_URL = "https://raw.githubusercontent.com/zzeeshann/data-science-journey/main/data/raw/ackoff_lecture_systems_age.txt"
ackoff_text = fetch(ACKOFF_URL)

# 3c. William James 1890 — Project Gutenberg, same URL Session 3 used
JAMES_URL = "https://www.gutenberg.org/cache/epub/57628/pg57628.txt"
james_raw = fetch(JAMES_URL)
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
sp = james_raw.find(start_marker)
sp = james_raw.find("\n", sp) + 1
ep = james_raw.find(end_marker)
james_text = james_raw[sp:ep].strip()

# 3d. Reddit r/Meditation — public JSON API, no auth, 2026
def fetch_reddit_meditation(target=300):
    posts = []
    seen = set()
    headers = {"User-Agent": "data-science-journey-research/1.0 (session 7)"}
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

# ---------------------------------------------------------------------------
# 4. Chunking — paragraph-level, 20 ≤ words ≤ 300
# ---------------------------------------------------------------------------

def chunk_paragraphs(text, min_words=20, max_words=300):
    paras = re.split(r"\n\s*\n", text)
    out = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        # collapse internal whitespace so word count is stable
        clean = re.sub(r"\s+", " ", p)
        n = len(clean.split())
        if min_words <= n <= max_words:
            out.append(clean)
    return out

tinw_chunks    = chunk_paragraphs(tinw_text)
ackoff_chunks  = chunk_paragraphs(ackoff_text)
james_chunks   = chunk_paragraphs(james_text)
# Reddit posts are already "paragraph-sized" units; apply same word filter.
reddit_chunks  = [re.sub(r"\s+", " ", p).strip() for p in reddit_posts]
reddit_chunks  = [c for c in reddit_chunks if 20 <= len(c.split()) <= 300]

print()
print("Chunk counts (paragraph-level, 20–300 words):")
print(f"  Thinking in Wholes : {len(tinw_chunks)}")
print(f"  Ackoff lecture     : {len(ackoff_chunks)}")
print(f"  James 1890         : {len(james_chunks)}")
print(f"  Reddit Meditation  : {len(reddit_chunks)}")

# Build the master DataFrame
records = (
    [{"source": "tinw",   "text": c} for c in tinw_chunks] +
    [{"source": "ackoff", "text": c} for c in ackoff_chunks] +
    [{"source": "james",  "text": c} for c in james_chunks] +
    [{"source": "reddit", "text": c} for c in reddit_chunks]
)
df = pd.DataFrame(records).reset_index(drop=True)
print(f"  TOTAL chunks       : {len(df)}")

# ---------------------------------------------------------------------------
# 5. Embed — all-MiniLM-L6-v2
# ---------------------------------------------------------------------------

MODEL_NAME = "all-MiniLM-L6-v2"
print(f"\nLoading {MODEL_NAME} ...")
model = SentenceTransformer(MODEL_NAME)
print("Embedding all chunks (this is the main compute step)...")
t0 = time.time()
vectors = model.encode(df["text"].tolist(), batch_size=64, show_progress_bar=True,
                       convert_to_numpy=True, normalize_embeddings=True)
print(f"Embeddings shape: {vectors.shape}    elapsed: {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 6. Pairwise cosine similarity (vectors already L2-normalised → dot product)
# ---------------------------------------------------------------------------

sim = vectors @ vectors.T          # shape (N, N)
np.fill_diagonal(sim, -1.0)        # suppress self-pairs

# helper: top-N pairs with optional source filters
def top_pairs(n, where_a=None, where_b=None, exclude_same=True):
    """where_a, where_b: source labels or None (any)."""
    a_mask = np.ones(len(df), dtype=bool) if where_a is None else (df["source"] == where_a).to_numpy()
    b_mask = np.ones(len(df), dtype=bool) if where_b is None else (df["source"] == where_b).to_numpy()
    M = sim.copy()
    if exclude_same:
        # zero out pairs where i==j is already done (diag = -1).
        # for cross-source mode, we don't need any extra mask.
        pass
    # mask: keep only (a, b) pairs we care about
    mask = np.outer(a_mask, b_mask)
    if where_a == where_b and where_a is not None:
        # within-corpus: dedupe by upper triangle
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

def bottom_pairs(n, where_a=None, where_b=None):
    a_mask = np.ones(len(df), dtype=bool) if where_a is None else (df["source"] == where_a).to_numpy()
    b_mask = np.ones(len(df), dtype=bool) if where_b is None else (df["source"] == where_b).to_numpy()
    M = sim.copy()
    mask = np.outer(a_mask, b_mask)
    if where_a == where_b and where_a is not None:
        mask = np.triu(mask, k=1)
    M = np.where(mask, M, 2.0)
    flat = M.flatten()
    order = np.argsort(flat)
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
        if M[i, j] > 1.5:
            break
        out.append((float(M[i, j]), int(i), int(j)))
        if len(out) >= n:
            break
    return out

def show_pair(label, pairs, full_text=False, max_chars=240):
    print(f"\n--- {label} ---")
    for k, (s, i, j) in enumerate(pairs, 1):
        a = df.loc[i]; b = df.loc[j]
        ta = a["text"] if full_text else (a["text"][:max_chars] + ("…" if len(a["text"]) > max_chars else ""))
        tb = b["text"] if full_text else (b["text"][:max_chars] + ("…" if len(b["text"]) > max_chars else ""))
        print(f"[{k}] cos={s:+.4f}   {a['source']}#{i}   ↔   {b['source']}#{j}")
        print(f"    A: {ta}")
        print(f"    B: {tb}")

# ---------------------------------------------------------------------------
# 7. The receipts
# ---------------------------------------------------------------------------

print("\n" + "="*72)
print("BEGIN_RECEIPTS — copy everything below into the conversation")
print("="*72)

print(f"\nMODEL: {MODEL_NAME}")
print(f"TOTAL CHUNKS: {len(df)}    "
      f"(tinw={len(tinw_chunks)}, ackoff={len(ackoff_chunks)}, "
      f"james={len(james_chunks)}, reddit={len(reddit_chunks)})")
print(f"VECTOR DIM: {vectors.shape[1]}")

# 7.1 Within-Thinking-in-Wholes — sanity check
show_pair("Top 5 within Thinking in Wholes",       top_pairs(5, "tinw", "tinw"))
show_pair("Bottom 5 within Thinking in Wholes",    bottom_pairs(5, "tinw", "tinw"))

# 7.2 Cross-corpus
show_pair("Top 5 James ↔ Thinking in Wholes",      top_pairs(5, "james", "tinw"))
show_pair("Top 5 James ↔ Reddit",                  top_pairs(5, "james", "reddit"))
show_pair("Top 5 James ↔ Ackoff",                  top_pairs(5, "james", "ackoff"))
show_pair("Top 5 Ackoff ↔ Thinking in Wholes",     top_pairs(5, "ackoff", "tinw"))

# 7.3 The surprise — Reddit ↔ Thinking in Wholes (full text for falsification)
print("\n--- Top 5 Reddit ↔ Thinking in Wholes (FULL TEXT) ---")
for k, (s, i, j) in enumerate(top_pairs(5, "reddit", "tinw"), 1):
    a = df.loc[i]; b = df.loc[j]
    print(f"\n[{k}] cos={s:+.4f}")
    print(f"  REDDIT (chunk {i}):")
    print(f"    {a['text']}")
    print(f"  THINKING IN WHOLES (chunk {j}):")
    print(f"    {b['text']}")

# 7.4 Bottom 5 most-orthogonal pairs anywhere
show_pair("Bottom 5 most orthogonal pairs (any pair)", bottom_pairs(5))

# Per-source mean cosines (rough texture)
print("\n--- Mean within-source cosine ---")
for src in ["tinw", "ackoff", "james", "reddit"]:
    idx = (df["source"] == src).to_numpy()
    sub = sim[np.ix_(idx, idx)]
    iu = np.triu_indices(sub.shape[0], k=1)
    if len(iu[0]) == 0:
        print(f"  {src}: n/a (only one chunk)")
        continue
    print(f"  {src}: {sub[iu].mean():+.4f}  (n_pairs={len(iu[0])})")

print("\n--- Mean cross-source cosine ---")
sources = ["tinw", "ackoff", "james", "reddit"]
for a in sources:
    for b in sources:
        if a >= b:
            continue
        ia = (df["source"] == a).to_numpy()
        ib = (df["source"] == b).to_numpy()
        sub = sim[np.ix_(ia, ib)]
        print(f"  {a}↔{b}: {sub.mean():+.4f}  (n_pairs={sub.size})")

# ---------------------------------------------------------------------------
# 8. UMAP 2D projection — coloured by source
# ---------------------------------------------------------------------------

print("\nFitting UMAP (2D)...")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric="cosine", random_state=42)
xy = reducer.fit_transform(vectors)

palette = {
    "tinw":   "#1f77b4",
    "ackoff": "#9467bd",
    "james":  "#d62728",
    "reddit": "#2ca02c",
}
labels = {
    "tinw":   "Thinking in Wholes",
    "ackoff": "Ackoff lecture",
    "james":  "James 1890",
    "reddit": "Reddit r/Meditation",
}

fig, ax = plt.subplots(figsize=(9, 6))
for src in sources:
    m = (df["source"] == src).to_numpy()
    ax.scatter(xy[m, 0], xy[m, 1], s=14, alpha=0.65,
               c=palette[src], label=f"{labels[src]} (n={m.sum()})",
               edgecolors="white", linewidths=0.3)
ax.set_xlabel("UMAP-1")
ax.set_ylabel("UMAP-2")
ax.set_title("Embedding landscape: four modern corpora, all-MiniLM-L6-v2")
ax.legend(loc="best", frameon=True, fontsize=9)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
out_path = "/content/chapter_07_embedding_landscape.png" if "google.colab" in sys.modules else "chapter_07_embedding_landscape.png"
plt.savefig(out_path, dpi=160, bbox_inches="tight")
plt.show()
print(f"Chart saved: {out_path}")

print("\n" + "="*72)
print("END_RECEIPTS")
print("="*72)

# ---------------------------------------------------------------------------
# 9. Trigger download of the chart so it's easy to drop into the repo
# ---------------------------------------------------------------------------

try:
    from google.colab import files
    files.download(out_path)
except Exception:
    print("(not in Colab — chart is in the working directory)")
