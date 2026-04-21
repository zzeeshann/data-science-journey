# The Shadow of Consciousness

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories its theoretical lens names.

**Started:** April 2026 | **Status:** Phase 2 — Wholeness Investigation (Sessions 4+)

## The question

Is consciousness a product of the brain, or is consciousness primary and the brain its instrument? This can't be answered with data -- it's one of the deepest open problems in philosophy. But it leaves a *trace* in human language. Across thousands of years of writing, humans have tried to describe consciousness. That trace is real. That trace is data.

**This project doesn't try to answer the metaphysical question. It maps its shadow in how humans have written about consciousness — and what the data says about how humans and societies are actually doing under the categories the project's theoretical lens names.**

## Where the project is now

At the end of Session 3 the working sub-question was sharpened into the **Wholeness Investigation**: *is the worldview shift described in* Thinking in Wholes (2026) *— from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?* Four hypotheses, country-scale data, Hugging Face models. Full plan in [`research_plan_wholeness.md`](research_plan_wholeness.md).

Session 4 delivered a real finding the rest of the investigation now orbits: across 141 countries between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained component fell in 98%. The WHR model predicts a substantially happier world than exists. Something systematic is moving outside the six measured variables, in the same direction, almost everywhere. Sessions 5–10 try to name it.

## Three sub-questions

1. Do people who describe mystical or non-dual experiences use consistent language across cultures and eras?
2. How has the language of consciousness shifted from religious to neuroscientific over the last 200 years? — *sharpened at end of Session 3 into the Wholeness Investigation above.*
3. Do materialist and non-materialist thinkers describe the *experience* of consciousness differently, or only the *explanation* of it?

## Methods

- **Phase 1 (Sessions 1–3)** — Exploration. Load data. First cleaning and charts. First two-point comparison.
- **Phase 2 (Sessions 4–5)** — Country-scale wellbeing and development. WHR, HDI, GDP. Panels, correlations, decompositions.
- **Phase 3 (Sessions 6–7)** — Embeddings and zero-shot classification. Semantic comparison of the book, Ackoff, James, Reddit corpora.
- **Phase 4 (Sessions 8–9)** — Cross-cultural values (World Values Survey) and topic modelling on large corpora.
- **Phase 5 (Session 10+)** — Synthesis.

## Data sources

All free and public.

**Country-scale:** World Happiness Report (2011–2025), UN Human Development Index, Our World in Data, World Bank Open Data, World Values Survey.

**Text at scale:** Project Gutenberg, Hugging Face Datasets, Reddit corpora (r/Meditation, r/NDE, r/decidingtobebetter, r/loneliness, r/Psychonaut), news and Wikipedia corpora, PubMed/arXiv.

**Theoretical lens (parked in `/data/raw/`):** *Thinking in Wholes* (2026); Ackoff, "From Machine Age to Systems Age."

## Repo structure

```
00_index.md                  -- the map (start here)
01_working_agreement.md      -- rules of engagement
02_project_brief.md          -- full project brief
03_project_structure.md      -- folder layout
04_roadmap.md                -- roadmap (compass, not commitment)
05_glossary.md               -- concept definitions
research_plan_wholeness.md   -- the multi-session investigation plan

sessions/                    -- chronological record of real work
book/                        -- personal narrative, written as we go
notebooks/                   -- Colab notebooks (.ipynb)
data/raw/                    -- original datasets and reference texts
data/processed/              -- cleaned data products
outputs/                     -- charts, tables, findings
```

## Setup

- **Laptop:** 2016 MacBook Pro (Intel) -- for reading and writing
- **Cloud compute:** Google Colab free tier (T4 GPU)
- **Models/data:** Hugging Face
- **Thinking partner:** Claude / ChatGPT / Gemini

## Learning goals

Python for data work, pandas, text processing and NLP, embeddings and semantic search, using LLMs inside code, fine-tuning a small model, git/GitHub, matplotlib, and — the skill the whole project trains — reading AI and data output skeptically.

## What this project is not

- Not an attempt to prove or disprove anything metaphysical.
- Not a literature review or philosophy paper.
- Not a product or startup.
- Not a portfolio piece optimised for a job application.
- Not a course.
- Not finished. A living project.
