# The Shadow of Consciousness

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories its theoretical lens names.

**Started:** April 2026 | **Status:** Wholeness Investigation closed at Session 9. Book wrapped at Session 13. Project still open — Session 14 (May 2026) opened a new direction with a **local LLM analysis stack** on a Mac Mini M4 Pro. Next sub-question TBD.

## The question

Is consciousness a product of the brain, or is consciousness primary and the brain its instrument? This can't be answered with data -- it's one of the deepest open problems in philosophy. But it leaves a *trace* in human language. Across thousands of years of writing, humans have tried to describe consciousness. That trace is real. That trace is data.

**This project doesn't try to answer the metaphysical question. It maps its shadow in how humans have written about consciousness — and what the data says about how humans and societies are actually doing under the categories the project's theoretical lens names.**

## Where the project is now

The **Wholeness Investigation** (Sessions 4–9) is closed. Sessions 10–13 wrapped the existing book. Two findings stand on their own — neither extends to the other statistically.

- **Country-scale (Chapters 5–6).** Across 141 countries between 2019 and 2025, the six measured factors in the World Happiness Report rose in 99% of countries while the unexplained residual fell in 98%. Session 5 ruled out HDI stagnation as the explanation: 38 of 129 countries showed GDP up, HDI flat, residual collapsing. Neither income nor development metrics can see what's falling. The country-scale work in this book does not name what does.
- **Text-level (Chapters 7–9).** Cross-era embedding work produced one positive finding (Reddit r/Meditation ↔ William James 1890 phenomenology of introspection, cosines 0.58–0.61) plus two clean falsifications (the structural position-twelve cluster filed as selection bias; the wholeness-register interpretation falsified by Reddit's negative paired-difference).

Chapter 10 names the unit-of-analysis bridge problem between the two halves as the project's central methodological lesson. The four summary files at repo root ([`mistakes_made.md`](mistakes_made.md), [`summary_for_a_reader.md`](summary_for_a_reader.md), [`improvements.md`](improvements.md), [`reader_glossary_audit.md`](reader_glossary_audit.md)) summarise what was learned.

**Session 14 (May 2026)** opened the post-book direction: a local LLM analysis stack is now running on a Mac Mini M4 Pro — Ollama serving Qwen 2.5 14B (`qwen2.5:14b`, GGUF Q4_K_M) on `localhost:11434`, driven from JupyterLab via a plain `ask_qwen()` function. Classification-via-prompt is now a second analytical primitive alongside the embeddings pipeline from Sessions 7–9. The next investigation question has not been chosen.

## Three sub-questions

1. Do people who describe mystical or non-dual experiences use consistent language across cultures and eras?
2. How has the language of consciousness shifted from religious to neuroscientific over the last 200 years? — *sharpened at end of Session 3 into the Wholeness Investigation above.*
3. Do materialist and non-materialist thinkers describe the *experience* of consciousness differently, or only the *explanation* of it?

## Methods (as they actually unfolded)

- **Phase 1 (Sessions 1–3)** — Exploration. First data loaded, first cleaning and charts, first two-point comparison.
- **Phase 2 (Sessions 4–6)** — Country-scale wellbeing and development. WHR + HDI + GDP. Panels, correlations, decompositions. Session 6 was a process audit (off the main arc) and is included here.
- **Phase 3 (Sessions 7–9)** — Cross-era embeddings. Modern corpora plus 15 verified ancient passages plus Reddit r/Meditation. Two pre-registered falsification tests, one survived positive (Reddit↔James), two clean rejections.
- **Phase 4 (Sessions 10–13)** — Honest pass and book wrap. Session 10 audited the bridge between country-scale and text-level work. Sessions 11–13 closed the book — lessons chapter, readability audit, summary files. What had originally been planned for Phase 4 (WVS + topic modelling) was deferred when the audit closed the investigation.
- **Phase 5 (Session 14+)** — Post-book methods acquisition and the next investigation. Local LLM stack (Ollama + Qwen 2.5 14B) added in Session 14 as a second analytical primitive. Next sub-question pick TBD.

## Data sources

All free and public.

**Country-scale:** World Happiness Report (2011–2025), UN Human Development Index, Our World in Data, World Bank Open Data, World Values Survey.

**Text at scale:** Project Gutenberg, Hugging Face Datasets, Reddit corpora (r/Meditation, r/NDE, r/decidingtobebetter, r/loneliness, r/Psychonaut), news and Wikipedia corpora, PubMed/arXiv.

**Theoretical lens (parked in `/data/raw/`):** *Thinking in Wholes* (2026); Ackoff, "From Machine Age to Systems Age."

## Repo structure

```
README.md                    -- this file
guide.html                   -- local LLM setup guide (open in a browser)
CLAUDE.md                    -- operational brief for Claude Code (auto-loaded)
discipline.md                -- the 22 disciplines + drift-response protocol
00_index.md                  -- the map (start here)
01_working_agreement.md      -- rules of engagement
02_project_brief.md          -- full project brief
03_project_structure.md      -- folder layout
04_roadmap.md                -- roadmap (compass, not commitment)
05_glossary.md               -- concept definitions
research_plan_wholeness.md   -- historical plan for the Wholeness Investigation (closed at Session 9)

mistakes_made.md             -- mistakes + corrections + standing-process habits
summary_for_a_reader.md      -- ~500-word executive summary of the book
improvements.md              -- ten numbered points for the next investigation's planning brief
reader_glossary_audit.md     -- glossary additions log

sessions/                    -- chronological record of real work (Sessions 1–14)
book/                        -- the personal book, Chapters 1–10
notebooks/                   -- pipeline scripts (Sessions 7–9 embeddings; Session 14 local LLM TBD)
data/raw/                    -- original datasets and reference texts (force-tracked per file)
data/processed/              -- cleaned data products
```

## Setup

**Hardware**
- **Mac Mini M4 Pro, 24 GB RAM, macOS 26.3** — added in Session 14 for the local LLM analysis stack.
- **2016 MacBook Pro (Intel)** — reading, writing, project management. Not used for analysis.

**Compute**
- **Local (Session 14+):** Ollama serving Qwen 2.5 14B on `localhost:11434`, driven from JupyterLab 4.5.7. ~28 tokens/sec.
- **Cloud (Sessions 7–9):** Google Colab free tier with a T4 GPU for the embedding pipeline (`all-MiniLM-L6-v2`, UMAP).

**Models / data:** Hugging Face (datasets + sentence-transformers); Ollama (local LLM serving).

**Thinking partners:** Claude, ChatGPT, Gemini, DeepSeek.

### Quick start — local LLM stack

The full setup guide is at **[`guide.html`](guide.html)** — open in a browser for the architecture diagram, the LM-Studio→Ollama migration story, and the complete commands reference.

Minimal command set:

```bash
curl -fsSL https://ollama.com/install.sh | sh    # install Ollama
ollama pull qwen2.5:14b                           # pull the 14B model (~9 GB)
python3 -m venv venv && source venv/bin/activate  # Python environment
pip install -r requirements.txt                   # install dependencies
jupyter lab                                       # launch JupyterLab
```

Then write an `ask_qwen()` function pointing at `http://localhost:11434/v1/chat/completions` with `model: "qwen2.5:14b"`. The full function and the AG News 50-article validation run live in [`sessions/session_14.md`](sessions/session_14.md).

## Learning goals

Python for data work, pandas, text processing and NLP, embeddings and semantic search, using LLMs inside code, fine-tuning a small model, git/GitHub, matplotlib, and — the skill the whole project trains — reading AI and data output skeptically.

## What this project is not

- Not an attempt to prove or disprove anything metaphysical.
- Not a literature review or philosophy paper.
- Not a product or startup.
- Not a portfolio piece optimised for a job application.
- Not a course.
- Not finished. A living project.
