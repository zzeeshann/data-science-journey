# Session 14 — Record

*First session of the post-book project. The Wholeness Investigation closed at Session 9; Sessions 10–13 wrapped the book. Session 14 is the methods-acquisition step for the next investigation: a local LLM analysis stack stood up on the user's M4 Pro Mac (Mac Mini, 24 GB RAM, macOS 26.3). The session ran on a single day (2026-05-11) through three iterations of the tooling. **Phase A** stood up the stack on **LM Studio** with Qwen 2.5 14B Instruct MLX 4-bit and hit two specific engine errors. **Phase A.5** tried the `jupyter-ai` v3.0.0 Jupyter extension as the in-notebook driver; that hit UI registration bugs and was abandoned in favour of a plain `ask_qwen()` function. **Phase B** removed LM Studio, installed **Ollama**, pulled `qwen2.5:14b`, and pointed `ask_qwen()` at `localhost:11434`. **Ollama + plain `ask_qwen()` + JupyterLab 4.5.7 is the working stack at the end of the session**, running at ~28 tokens/sec. No sub-question chosen yet. Exploratory / capability work, not a hypothesis test.*

---

## Goal

Move the project off Colab+T4-only tooling and acquire a second analytical primitive — **classification-via-LLM-prompt** — alongside the embedding-and-cosine-similarity pipeline that ran Sessions 7–9. Concretely: get **Qwen 2.5 14B Instruct** serving on the M4 Pro Mac as a localhost OpenAI-compatible API, drive it from Jupyter, and prove the end-to-end pattern works on a standard labelled-text benchmark. The *which serving stack* was not pre-committed — the goal was a working pipeline, and the path through tools was allowed to follow what actually held up under use.

This is the *capability acquisition* step, not the start of an investigation. The next sub-question for the project has not been chosen. Discipline rules 1–4 (unit-of-analysis, statistical bridge up front, exploratory-vs-confirmatory marking, pre-registration) apply from the moment a question is named — none of them apply here, because no claim is being made about the world.

## What actually happened

The session ran in three iterations of tooling on the same day. The user worked through three DeepSeek-authored tutorials in sequence — DeepSeek is the chatbot at deepseek.com; specific model name/version is not declared in any of the three documents.

**Phase A — LM Studio.** The user worked through the first DeepSeek tutorial, now parked at [`data/raw/deepseek_local_llm_guide_2026_05_11.html`](../data/raw/deepseek_local_llm_guide_2026_05_11.html). It walks through installing **LM Studio**, downloading **Qwen 2.5 14B Instruct MLX 4-bit**, starting the local server on port **1234**, and writing an `ask_qwen()` function that POSTs to `localhost:1234/v1/chat/completions`. The pipeline came up on the first attempt and ran at ~28 tokens/sec — a speed the consolidated tutorial confirms is what MLX 4-bit on Apple Silicon delivers for this model. The 50-article AG News validation produced **46/50 = 92% accuracy**.

LM Studio then broke twice in a row on subsequent invocations. The third tutorial documents the failures specifically: *Attempt 2 — engine error, `libpython3.11.dylib` not found* (an auto-update broke an internal Python library path on the user's machine; the tutorial calls this a known LM Studio bug). *Attempt 3 — "No LM Runtime found for format 'safetensors'"* (LM Studio's runtime registration confused itself between GGUF, MLX, and Safetensors model formats). Two real, reproducible-by-symptom failures, both on the same M4 Pro Mac, both within the same day.

**Phase A.5 — `jupyter-ai` extension, abandoned.** Between the LM Studio failures and the Ollama install, the user tried the `jupyter-ai` v3.0.0 Jupyter extension as an alternative way to chat with the local model from inside the notebook. The settings UI failed to register and the chat panel couldn't connect to Ollama. The third DeepSeek tutorial flags this as a known v3.0.0 issue and recommends going back to a plain `ask_qwen()` function. The extension was uninstalled (the third tutorial gives the multi-package uninstall command verbatim) and the pipeline reverted to the plain-function design.

**Phase B — Ollama + plain `ask_qwen()` + JupyterLab.** The user removed LM Studio (`rm -rf ~/.lmstudio` plus dragging the app to Trash, both per the consolidated tutorial), installed **Ollama** with `curl -fsSL https://ollama.com/install.sh | sh`, and pulled **`qwen2.5:14b`** (~9 GB, GGUF Q4_K_M by Ollama's default). `ask_qwen()` was repointed at `localhost:11434/v1/chat/completions` with `model: "qwen2.5:14b"`. The OpenAI-API contract is identical between the two stacks — only the URL, port, and model identifier changed, so the rest of the notebook needed no rework. The notebook environment also moved from `jupyter notebook` (Phase A's tutorial) to **JupyterLab 4.5.7** (the third tutorial's recommendation), run from a venv at `~/pro/news-data-science`. The same 46/50 = 92% figure is reported in the second and third tutorials; whether that's an independent re-run on Ollama or a copy of the Phase-A number is undetermined from the receipts available (see Caveats #2).

The second DeepSeek tutorial — parked at [`data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html`](../data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html) — also introduces two cells beyond the basic pipeline: a batch loop with progress reporting and a Seaborn-rendered confusion matrix. Neither is recorded as having been run; they're available as next steps.

The third tutorial — [`data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html`](../data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html), titled *"Complete Setup Guide (Ollama Edition)"* — is the **canonical commands reference** for this stack going forward. It includes the LM-Studio→Ollama migration story as a four-attempt table, the `jupyter-ai`→plain-function migration as a two-attempt table, the architecture diagram for the working stack, and a complete commands table from `curl ... install.sh` through `jupyter lab` and the startup `alias news=…`. A future session that needs to rebuild this stack from scratch should read that file before this session record.

This session record was drafted by Opus 4.7 (1M context) inside Claude Code on 2026-05-11, working from the four DeepSeek source files plus the user's confirmation of the LM Studio failures and the subsequent migrations. No model was used to *do* analysis in this session — only to document the work, copy the files into the repo, and integrate the new capability into the project's standing notes.

## The data (files touched)

| File | Edit |
|---|---|
| `data/raw/deepseek_local_llm_guide_2026_05_11.html` | created — DeepSeek-authored Phase-A tutorial (LM Studio path), full HTML version. Force-add (`data/raw/*` is gitignored). |
| `data/raw/deepseek_local_llm_guide_2026_05_11.md` | created — Phase-A tutorial, condensed Markdown version. Force-add. |
| `data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html` | created — DeepSeek-authored Phase-B tutorial (Ollama path), full HTML version. Adds the LM-Studio-vs-Ollama comparison, the batch-50 cell, the confusion-matrix cell. Force-add. |
| `data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html` | created — DeepSeek-authored consolidated reference, titled *"(Ollama Edition)"*. Includes the LM-Studio→Ollama 4-attempt migration table with specific bug receipts, the `jupyter-ai`→plain-function 2-attempt migration table, architecture diagram, results table (~28 tok/sec, 92%), and a complete commands reference. **The canonical setup guide for this stack going forward.** Force-add. |
| `sessions/session_14.md` | created and updated in place across all three phases — this file |
| `00_index.md` | updated — Session 14 entry, four new `data/raw/` entries, *last-we-did* and *current-hook* lines refreshed |
| `05_glossary.md` | updated — six new entries in the alphabetical Sessions-4+ block: AG News, JupyterLab, LM Studio, Local LLM, Ollama, Quantization (4-bit) |
| `CLAUDE.md` | updated — *State*, *Last session committed*, *Next session* sections + force-tracked file list updated |

No chapters edited. No images produced. No `.ipynb` saved to `/notebooks/` — see Caveats #2.

The AG News dataset itself is **not** committed to `data/raw/`. It loads in one line via `datasets.load_dataset("ag_news")` (Hugging Face caches locally on first call). For a labelled benchmark of this size (120k rows, ~30 MB), the Hugging Face pull is the canonical source — duplicating it in-repo would be churn. If a future investigation reuses AG News, the loader call is recorded in the receipts at the bottom of this file.

## Findings

This session has no findings about the world. It has one finding about the project's analytical toolkit:

1. **A local-LLM classification pipeline runs end-to-end on the user's hardware.** The pattern is: HuggingFace dataset → Python `requests.post` → localhost OpenAI-compatible API served by **Ollama** (after switching away from LM Studio) → Qwen 2.5 14B response parsed out of the JSON → comparison against ground truth. The user has executed this pattern on a small validated benchmark. The capability is real, not theoretical.

   The OpenAI-compatible API contract is what made the LM Studio→Ollama swap a one-line change in the `ask_qwen()` function — different URL, different port, different model identifier, otherwise identical request shape. This is *portability* in the practical sense: the analytical code didn't need rewriting when the serving stack was replaced. Any future investigation that uses this pipeline should keep the URL, port, and model identifier in a config block rather than hardcoded inside `ask_qwen()`, so future tool swaps stay one-line changes.

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

2. **The notebook used to run the 50-article test was not preserved with this session record, and it is unclear whether the 92% figure was independently re-run on Ollama after the switch.** Sessions 7, 8, and 9 each have a corresponding `.py` file in `/notebooks/`. Session 14 does not. The run(s) happened inside Jupyter on the user's Mac during the tutorial walkthroughs, and no notebook was saved out for either phase. Both DeepSeek tutorials report the same 46/50 = 92% number — that consistency could be a genuine result on both stacks (MLX-quantized Qwen on LM Studio in Phase A and GGUF-quantized Qwen on Ollama in Phase B, on the same 50 AG News articles, both with `temperature=0.1`) or it could be the tutorial-author copying the Phase-A figure into the Phase-B writeup. The receipts in this repo cannot distinguish those cases. **Standing-process habit added (proposed rule 16):** any future session that produces an analytical result must save the `.ipynb` (or `.py` export) to `/notebooks/` before commit. Session 14's experience is the precedent. See [`discipline.md`](../discipline.md).

3. **The LM Studio failures are recorded by symptom, not by independent reproducibility test.** The consolidated tutorial preserves two specific error states — *Attempt 2: `libpython3.11.dylib` not found*, attributed in the tutorial to an LM Studio auto-update breaking an internal path; *Attempt 3: "No LM Runtime found for format 'safetensors'"*, attributed to runtime-registration confusion across GGUF/MLX/Safetensors formats. Both are real strings the user encountered today on this machine. They are NOT independently verified against LM Studio's issue tracker or release notes for this project; the tutorial document is the only source. The decision to uninstall was pragmatic — switch to the tool that works — and the move-on cost was zero because the OpenAI-API contract is shared. A future investigation that wants to *recommend* one stack over the other in print would need its own reproducibility test on a clean machine, not a reference back to this caveat.

4. **The tutorials were authored by an external LLM, not by the user or by this project.** DeepSeek wrote both HTML guides. The user's contribution was running them end-to-end and confirming the pipeline worked. The analytical *understanding* of why the pipeline works has not been independently re-derived — for example, this session record doesn't reconstruct from first principles what `temperature=0.1` does, why GGUF Q4_K_M and MLX 4-bit both land at ~9 GB for a 14B-parameter model, or what the OpenAI-API contract actually requires for compliance. Those are now in the glossary (Quantization, Local LLM, Ollama, LM Studio entries) and inline in the tutorial files, available for reference. If a future investigation depends on the *details* of how this pipeline behaves at the edges, those details need to be re-derived from sources outside these tutorials.

5. **The 92% figure(s) are reported by the tutorial documents, not verified from notebook outputs that live in this repo.** The user did run the tests on their Mac today (2026-05-11) and reports the figure matched the tutorial's expected value. This is a verifiable claim about their machine; this session record records it as the user reported it. Future sessions using either pipeline should preserve their own run outputs in `/notebooks/` per Caveat #2 above.

6. **No connection back to the book's findings is attempted, and none is implied.** The country-scale residual finding (Chapters 5–6) and the cross-era Reddit↔James phenomenology resonance finding (Chapters 7–9) are separate from anything Session 14 did. Local-LLM classification was not used to revisit either of those datasets in this session. If a future investigation chooses to revisit them with this new tool, that's a new investigation, with a new plan file and a unit-of-analysis decision made up front.

## Status at end of session

- Local LLM stack running on the user's M4 Pro Mac (Mac Mini, 24 GB RAM, macOS 26.3): **Ollama serving `qwen2.5:14b` (GGUF Q4_K_M, ~9 GB) on `localhost:11434`**, driven from **JupyterLab 4.5.7** via the OpenAI-compatible chat-completions API, at ~28 tokens/sec. The notebook venv lives at `~/pro/news-data-science/venv`. LM Studio is uninstalled (`~/.lmstudio` removed, app trashed). The `jupyter-ai` extension is uninstalled.
- All four DeepSeek tutorial files (Phase-A HTML + Markdown, Phase-B HTML, Phase-C consolidated HTML) are in [`data/raw/`](../data/raw/) as parked source material. [`deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html`](../data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html) is the canonical commands reference for the working stack.
- This session record is written across all three phases. [`00_index.md`](../00_index.md), [`05_glossary.md`](../05_glossary.md), and [`CLAUDE.md`](../CLAUDE.md) are updated.
- The next investigation question has not been chosen. When it is, it will produce its own plan file, run under [`discipline.md`](../discipline.md)'s rules from session zero, and may use either or both of the project's two analytical primitives (embeddings, local LLM classification) as the question demands.
- The book ([Chapters 1–10](../book/), [Sessions 1–13](../sessions/)) stays closed.

## Raw outputs (receipts)

### The pipeline at end of session

**Environment (end of session):** macOS 26.3 on a Mac Mini M4 Pro with 24 GB RAM. Python 3 in a venv at `~/pro/news-data-science/venv`. **JupyterLab 4.5.7** served from the same venv via `jupyter lab`. **Ollama running locally**, model `qwen2.5:14b` pulled and loaded (`ollama list` shows it; the model file is ~9 GB GGUF Q4_K_M by Ollama's default for this name). Inference speed ~28 tokens/sec.

**Installed Python packages:** `datasets`, `jupyter`, `requests`, `pandas`, `matplotlib`, `seaborn`.

**Minimal command set to rebuild the stack from scratch** (the consolidated tutorial holds the full version; this is the smallest set a future reader needs):

```bash
# 1. Local LLM runtime
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:14b           # ~9 GB, GGUF Q4_K_M

# 2. Python project
mkdir -p ~/pro/news-data-science && cd ~/pro/news-data-science
python3 -m venv venv
source venv/bin/activate
pip install datasets jupyter requests pandas matplotlib seaborn

# 3. Notebook
jupyter lab                       # opens at http://localhost:8888
```

**Dataset loader (unchanged across both phases):**
```python
from datasets import load_dataset
dataset = load_dataset("ag_news")
categories = {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}
```

**The current `ask_qwen()` function (Phase B — Ollama):**
```python
import requests

def ask_qwen(prompt, article_text):
    response = requests.post(
        "http://localhost:11434/v1/chat/completions",   # Ollama
        json={
            "model": "qwen2.5:14b",                     # Ollama's model name
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": article_text}
            ],
            "temperature": 0.1
        }
    )
    return response.json()["choices"][0]["message"]["content"]
```

**The earlier `ask_qwen()` function (Phase A — LM Studio, no longer running but kept here as record):**
```python
# Phase A — superseded. Server uninstalled.
def ask_qwen(prompt, article_text):
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",    # LM Studio
        json={
            "model": "qwen2.5-14b-instruct",            # LM Studio's MLX 4-bit
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": article_text}
            ],
            "temperature": 0.1
        }
    )
    return response.json()["choices"][0]["message"]["content"]
```

The OpenAI-API contract is identical between the two stacks — only the URL, port, and model identifier change. A single function with a config block could front both; this hasn't been written.

**The classification prompt used in both validation runs:**

> "Classify this news into ONE category: World, Sports, Business, or Sci/Tech. Return ONLY the category name."

(System role.) The article text (truncated to 1000 characters per the tutorials) went in as the user role.

**Reported result:** 46/50 = 0.92 accuracy in both DeepSeek tutorials (Phase A on LM Studio with MLX-quantized Qwen, Phase B on Ollama with GGUF-quantized Qwen). n=50, four-class problem, chance baseline = 0.25. Whether the Phase-B figure is an independent re-run or a copy of the Phase-A figure is undetermined from the receipts — see Caveats #2.

**Next steps available from the Ollama tutorial but not run yet in receipts:**
- A batch loop over 50 articles with progress reporting, error-recording, and a `pandas.DataFrame` of `(article_id, true_label, qwen_prediction, correct)` rows (Cell 4 of the Phase-B tutorial).
- A Seaborn confusion-matrix heatmap of `pd.crosstab(df["true_label"], df["qwen_prediction"])` (Cell 5).

**What's not preserved in this repo:**
- The `.ipynb` notebook(s) themselves (see Caveats #2).
- The 50 (predicted_label, true_label) pairs from either phase, so per-class accuracy and confusion matrix cannot be recomputed from receipts.
- The exact response strings Qwen returned for each of the 50 calls (would let us check how often it answered cleanly vs. with extra commentary, and whether MLX and GGUF gave bit-identical outputs at `temperature=0.1`).

These are recovery-target items for the next session that uses this pipeline.

### Source files for this session

- [`data/raw/deepseek_local_llm_guide_2026_05_11.html`](../data/raw/deepseek_local_llm_guide_2026_05_11.html) — Phase A (LM Studio) tutorial, full HTML. 15 KB. Eight parts: big picture, tools installed, the connection (Jupyter↔Qwen), what the experiment did, complete setup commands, key concepts, lessons, where to go next.
- [`data/raw/deepseek_local_llm_guide_2026_05_11.md`](../data/raw/deepseek_local_llm_guide_2026_05_11.md) — Phase A tutorial, condensed Markdown. 1.6 KB. Ends partway through Part 5 (the setup-commands block is truncated in the source). The Phase-A HTML is the complete reference.
- [`data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html`](../data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html) — Phase B (Ollama) tutorial, full HTML. ~20 KB. Six sections: project overview, full system setup, the main notebook (five cells including batch loop and confusion matrix), restart commands, concepts explained (notably the Ollama-vs-LM-Studio comparison table that documents *why* the switch happened), recommended repo structure.
- [`data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html`](../data/raw/deepseek_local_llm_guide_2026_05_11_ollama_consolidated.html) — Phase C consolidated reference, *"Complete Setup Guide (Ollama Edition)"*. ~10 KB. Five sections: the journey (LM Studio→Ollama 4-attempt table and jupyter-ai→plain-function 2-attempt table, both with specific error strings), final working setup (architecture diagram, the five install steps, the `ask_qwen()` function), results achieved (28 tok/sec, 92% accuracy), complete commands reference (one table of every CLI command the project uses), and recommended repo structure (`requirements.txt`, `.gitignore`, `README.md` templates). **The canonical setup guide a future reader or student should use to rebuild this stack.**

### Models used in this session

- **Tutorial author:** DeepSeek (deepseek.com chatbot; specific model name and version not specified in any of the three source files). External to this project. Authored both Phase-A and Phase-B tutorials.
- **Analytical model on the user's Mac (Phase B, current):** Qwen 2.5 14B Instruct, GGUF Q4_K_M quantization, served via Ollama on `localhost:11434`. Pipeline workhorse at end of session.
- **Analytical model on the user's Mac (Phase A, retired):** Qwen 2.5 14B Instruct, MLX 4-bit quantization, served via LM Studio on `localhost:1234`. Used for the Phase-A 50-article test; LM Studio has since been uninstalled.
- **Session record author:** Opus 4.7 (1M context), Claude Code on the user's machine, 2026-05-11. Drafted this file from the three DeepSeek source files plus the user's confirmation of the LM Studio→Ollama switch. No prose was generated by Qwen for this session record; Qwen's role in Session 14 was confined to running the 50-article classification(s).

Following [`discipline.md`](../discipline.md) rule 15 (asymmetric-pair pattern): this is a single-model session, by design — there is no analytical prose to audit, only a capability to record. Future sessions that produce findings via the local-LLM pipeline should run an Opus-class verification pass on the resulting prose before commit, same as Sessions 6–13.
