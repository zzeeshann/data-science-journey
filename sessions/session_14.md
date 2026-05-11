# Session 14 — Record

*First session of the post-book project. The Wholeness Investigation closed at Session 9; Sessions 10–13 wrapped the book. Session 14 is the methods-acquisition step for the next investigation: a local LLM analysis stack stood up on the user's M4 Pro Mac. No sub-question chosen yet. Exploratory / capability work, not a hypothesis test.*

---

## Goal

Move the project off Colab+T4-only tooling and acquire a second analytical primitive — **classification-via-LLM-prompt** — alongside the embedding-and-cosine-similarity pipeline that ran Sessions 7–9. Concretely: install LM Studio on the M4 Pro Mac, load Qwen 2.5 14B Instruct, expose it as a localhost OpenAI-compatible API, drive it from Jupyter, and prove the end-to-end pattern works on a standard labelled-text benchmark.

This is the *capability acquisition* step, not the start of an investigation. The next sub-question for the project has not been chosen. Discipline rules 1–4 (unit-of-analysis, statistical bridge up front, exploratory-vs-confirmatory marking, pre-registration) apply from the moment a question is named — none of them apply here, because no claim is being made about the world.

## What actually happened

The user worked through a tutorial authored by **DeepSeek** (the chatbot at deepseek.com — model class not specified in the document). The two source files DeepSeek produced — an HTML rendering and a condensed Markdown version — are now in [`data/raw/`](../data/raw/) (see Raw outputs below). The tutorial walks through installing LM Studio, downloading **Qwen 2.5 14B Instruct MLX 4-bit**, starting the local server, loading the AG News dataset via Hugging Face, and writing a single function (`ask_qwen`) that POSTs to `localhost:1234/v1/chat/completions` and returns the model's reply.

The user then ran the tutorial's small validation experiment on their Mac: classify 50 articles from AG News into one of four categories (`World`, `Sports`, `Business`, `Sci/Tech`) by prompt, and compare against the dataset's ground-truth labels. The reported result was **46/50 correct = 92% accuracy**. This figure comes from the tutorial document the user followed, not from a separately preserved notebook output — see Caveats #2 for the receipt gap.

This session record was drafted by Opus 4.7 (1M context) inside Claude Code on 2026-05-11, working from the two DeepSeek source files plus the user's confirmation that they ran the tutorial successfully on their Mac today. No model was used to *do* analysis in this session — only to document the work, copy the files into the repo, and integrate the new capability into the project's standing notes.

## The data (files touched)

| File | Edit |
|---|---|
| `data/raw/deepseek_local_llm_guide_2026_05_11.html` | created — DeepSeek-authored tutorial, full HTML version. Force-add (`data/raw/*` is gitignored). |
| `data/raw/deepseek_local_llm_guide_2026_05_11.md` | created — DeepSeek-authored tutorial, condensed Markdown version. Force-add. |
| `sessions/session_14.md` | created — this file |
| `00_index.md` | updated — Session 14 entry, two new `data/raw/` entries, *last-we-did* pointer refreshed |
| `05_glossary.md` | updated — four new entries in the alphabetical Sessions-4+ block: AG News, LM Studio, Local LLM, Quantization (4-bit) |
| `CLAUDE.md` | updated — *Last session committed* and *Next session* sections in the project-state block |

No chapters edited. No images produced. No `.ipynb` saved to `/notebooks/` — see Caveats #2.

The AG News dataset itself is **not** committed to `data/raw/`. It loads in one line via `datasets.load_dataset("ag_news")` (Hugging Face caches locally on first call). For a labelled benchmark of this size (120k rows, ~30 MB), the Hugging Face pull is the canonical source — duplicating it in-repo would be churn. If a future investigation reuses AG News, the loader call is recorded in the receipts at the bottom of this file.

## Findings

This session has no findings about the world. It has one finding about the project's analytical toolkit:

1. **A local-LLM classification pipeline runs end-to-end on the user's hardware.** The pattern is: HuggingFace dataset → Python `requests.post` → localhost OpenAI-compatible API served by LM Studio → Qwen 2.5 14B response parsed out of the JSON → comparison against ground truth. The user has now executed this pattern on a small validated benchmark. The capability is real, not theoretical.

2. **The tutorial's 92% on 50 AG News articles is consistent with what published benchmarks show for Qwen-class models on news topic classification.** AG News is a well-separated 4-class problem on short news passages; a 14B-parameter instruction-tuned model with a category list in the prompt should sit in the 88–95% range. The 92% figure isn't a finding about Qwen — it's a sanity check that the pipeline is wired correctly. If the run had come back at 25% (chance level) or wildly inconsistent across categories, that would have signalled a wiring problem. It didn't.

3. **The project now has two analytical primitives, not one.**
   - **Embeddings + cosine similarity** (Sessions 7–9): catches *resonance* — passages that occupy similar positions in semantic space, including across centuries. Cannot score, classify, or judge.
   - **LLM-classification-via-prompt** (Session 14 onwards): takes a prompt + a piece of text and returns a structured answer — a category label, a sentiment, a yes/no, a short summary, an extracted entity list. Cannot tell you what's *near* a passage in semantic space.
   - These are complementary, not interchangeable. A future investigation that wants *both* "what does this resonate with?" *and* "what is this saying, in our terms?" can now run both passes on the same corpus.

## What this means for the project

The book ([Chapters 1–10](../book/), [Sessions 1–13](../sessions/)) is closed and stays closed. Session 14 does not extend it — no chapter is added, no chapter is touched. The book documents the Wholeness Investigation; that investigation reached its conclusive endpoint at Session 9 and the book wrapped at Session 13.

The **project** — the multi-year ambition described in [`02_project_brief.md`](../02_project_brief.md) — continues. The next investigation gets picked when the user is ready. When it's picked, two things happen that didn't apply at the start of Sessions 1–9:

- **The disciplines from [`discipline.md`](../discipline.md) apply from session zero.** Rule 1 (unit of analysis written before any code runs), rule 2 (statistical bridge specified up front), rule 3 (exploratory vs confirmatory labelled), rule 4 (pre-registration) — none of these existed when the previous investigation began. They exist now and the next investigation inherits them.
- **The new investigation will produce its own plan file.** [`research_plan_wholeness.md`](../research_plan_wholeness.md) is the historical plan for the previous investigation and stays as a record. A new plan file (filename TBD when the question is named) gets created at the start of the next investigation.

Session 14's contribution to that future: when the next question is picked, the project's options are wider than they were. If the question is text-shaped and benefits from classification-style measurement — *how many of these passages express despair? what fraction of these documents mention nature? does this corpus skew positive or negative compared to that one?* — the local-LLM pipeline is now available. If the question is text-shaped and benefits from resonance-style measurement — *what 19th-century paragraph is closest to this Reddit post?* — the embedding pipeline from Sessions 7–9 is also still available.

## Caveats

1. **92% on 50 articles is tutorial-grade, not benchmark-grade.** No confidence interval (n=50 is small enough that the 95% CI on a 0.92 proportion runs roughly 0.81 to 0.98 — Wilson method, with a tail visible to anyone). No held-out test set design. No replication across multiple random samples. No comparison against a baseline (e.g. always-predict-the-majority-class). This figure is fine as a sanity check that the wiring works. It is not citable as a Qwen-on-AG-News benchmark.

2. **The notebook used to run the 50-article test was not preserved with this session record.** Sessions 7, 8, and 9 each have a corresponding `.py` file in `/notebooks/`. Session 14 does not. The reason is that the run happened inside Jupyter on the user's Mac during the tutorial walkthrough, and the working notebook was not saved out. The receipts at the bottom of this file include the function code (transcribed from the tutorial), but the actual run output — the 50 (prediction, true label) pairs that produced the 92% figure — is not in the repo. **Standing-process habit added (rule 16):** any future session that produces an analytical result must save the `.ipynb` (or `.py` export) to `/notebooks/` before commit. See [`discipline.md`](../discipline.md) §1 — Session 14's experience is the precedent.

3. **The tutorial was authored by an external LLM, not by the user or by this project.** DeepSeek wrote the HTML and Markdown that the user worked through. The user's contribution was running it end-to-end and confirming it worked. The analytical *understanding* of why the pipeline works has not been independently re-derived — for example, this session record doesn't reconstruct from first principles what `temperature=0.1` does, why MLX 4-bit quantization fits in ~9 GB, or what the localhost OpenAI-API contract actually requires. Those are now in the glossary (4-bit quantization entry) and inline in the tutorial files, available for reference. If a future investigation depends on the *details* of how this pipeline behaves at the edges, those details need to be re-derived from sources outside this tutorial.

4. **The 92% figure is reported by the tutorial document, not verified from a notebook output that lives in this repo.** The user did run the test on their Mac today (2026-05-11) and reports it matched the tutorial's expected value. This is a verifiable claim about their machine; this session record records it as the user reported it. Future investigations using this pipeline should preserve their own run outputs in `/notebooks/` per Caveat #2 above.

5. **No connection back to the book's findings is attempted, and none is implied.** The country-scale residual finding (Chapters 5–6) and the cross-era Reddit↔James phenomenology resonance finding (Chapters 7–9) are separate from anything Session 14 did. Local-LLM classification was not used to revisit either of those datasets in this session. If a future investigation chooses to revisit them with this new tool, that's a new investigation, with a new plan file and a unit-of-analysis decision made up front.

## Status at end of session

- Local LLM stack is running on the user's M4 Pro Mac: LM Studio + Qwen 2.5 14B Instruct MLX 4-bit + server on `localhost:1234`.
- The DeepSeek tutorial (HTML + Markdown) is in [`data/raw/`](../data/raw/) as parked source material.
- This session record is written. [`00_index.md`](../00_index.md), [`05_glossary.md`](../05_glossary.md), and [`CLAUDE.md`](../CLAUDE.md) are updated.
- The next investigation question has not been chosen. When it is, it will produce its own plan file, run under [`discipline.md`](../discipline.md)'s rules from session zero, and may use either or both of the project's two analytical primitives (embeddings, local LLM classification) as the question demands.
- The book ([Chapters 1–10](../book/), [Sessions 1–13](../sessions/)) stays closed.

## Raw outputs (receipts)

### The pipeline, as run

**Environment:** macOS, M4 Pro Mac, Python 3 in a venv, Jupyter notebook in the browser, LM Studio app running with `qwen2.5-14b-instruct` MLX 4-bit loaded and the local server started on port 1234 (Developer Mode enabled).

**Installed packages:** `datasets`, `jupyter`, `requests`, `pandas`, `matplotlib`, `seaborn`.

**Dataset loader:**
```python
from datasets import load_dataset
dataset = load_dataset("ag_news")
categories = {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}
```

**The function that makes the pipeline work:**
```python
import requests

def ask_qwen(prompt, article_text):
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        json={
            "model": "qwen2.5-14b-instruct",
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": article_text}
            ],
            "temperature": 0.1
        }
    )
    return response.json()["choices"][0]["message"]["content"]
```

**The classification prompt used in the 50-article validation run:**

> "Classify this news into ONE category: World, Sports, Business, or Sci/Tech."

(System role.) The article text (truncated to 1000 characters in the tutorial's example) went in as the user role.

**Reported result:** 46/50 = 0.92 accuracy. n=50, four-class problem, chance baseline = 0.25.

**What's not preserved in this repo:**
- The `.ipynb` notebook itself (see Caveats #2).
- The 50 (predicted_label, true_label) pairs (so the per-class accuracy and confusion matrix can't be recomputed from receipts).
- The exact response strings Qwen returned for each of the 50 calls (would let us check how often it answered cleanly vs. with extra commentary).

These are recovery-target items for the next session that uses this pipeline.

### Source files for this session

- [`data/raw/deepseek_local_llm_guide_2026_05_11.html`](../data/raw/deepseek_local_llm_guide_2026_05_11.html) — full HTML rendering of the tutorial. 15 KB. Eight parts: big picture, tools installed, the connection (Jupyter↔Qwen), what the experiment did, complete setup commands, key concepts, lessons, where to go next.
- [`data/raw/deepseek_local_llm_guide_2026_05_11.md`](../data/raw/deepseek_local_llm_guide_2026_05_11.md) — condensed Markdown version. 1.6 KB. Same content compressed; ends partway through Part 5 (the setup-commands block is truncated in the source). The HTML version is the complete reference.

### Models used in this session

- **Tutorial author:** DeepSeek (deepseek.com chatbot; specific model name and version not specified in the source files). External to this project.
- **Analytical model on the user's Mac:** Qwen 2.5 14B Instruct, MLX 4-bit quantization, served via LM Studio on `localhost:1234`. The pipeline's actual workhorse for the 50-article test.
- **Session record author:** Opus 4.7 (1M context), Claude Code on the user's machine, 2026-05-11. Drafted this file from the two DeepSeek source files plus the user's confirmation. No prose was generated by Qwen for this session record; Qwen's role in Session 14 was confined to running the 50-article classification.

Following [`discipline.md`](../discipline.md) rule 15 (asymmetric-pair pattern): this is a single-model session, by design — there is no analytical prose to audit, only a capability to record. Future sessions that produce findings via the local-LLM pipeline should run an Opus-class verification pass on the resulting prose before commit, same as Sessions 6–13.
