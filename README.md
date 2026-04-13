# The Shadow of Consciousness

A data science project exploring how humans describe consciousness, meaning, and the self across cultures, eras, and traditions.

**Started:** April 2026 | **Status:** Phase 1 -- foundations

## The question

Is consciousness a product of the brain, or is consciousness primary and the brain its instrument? This can't be answered with data -- it's one of the deepest open problems in philosophy. But it leaves a *trace* in human language. Across thousands of years of writing, humans have tried to describe consciousness. That trace is real. That trace is data.

**This project doesn't try to answer the metaphysical question. It maps its shadow in how humans have written about consciousness across traditions and eras.**

## Three sub-questions

1. Do people who describe mystical or non-dual experiences use consistent language across cultures and eras?
2. How has the language of consciousness shifted from religious to neuroscientific over the last 200 years?
3. Do materialist and non-materialist thinkers describe the *experience* of consciousness differently, or only the *explanation* of it?

## Methods

Starting simple, building up:

- **Phase 1** -- Exploration. Load data. Count words. Simple charts.
- **Phase 2** -- Text cleaning, tokenising, frequency comparison.
- **Phase 3** -- Embeddings for semantic comparison.
- **Phase 4** -- LLM-assisted theme extraction.
- **Phase 5** -- Fine-tune a small model on a chosen corpus.

## Data sources

All free and public: Project Gutenberg, Hugging Face Datasets, Reddit archives (r/Meditation, r/NDE, r/Psychonaut), arXiv/PubMed abstracts, public-domain translations of mystical texts.

## Repo structure

```
00_index.md              -- the map (start here)
01_working_agreement.md  -- rules of engagement
02_project_brief.md      -- full project brief
03_project_structure.md  -- folder layout
04_roadmap.md            -- 6-month plan
05_glossary.md           -- concept definitions

sessions/                -- chronological record of real work
book/                    -- personal narrative, written as we go
notebooks/               -- Colab notebooks (.ipynb)
data/raw/                -- original datasets (never edited)
data/processed/          -- cleaned versions
outputs/                 -- charts, tables, findings
```

## Setup

- **Laptop:** 2016 MacBook Pro (Intel) -- for reading and writing
- **Cloud compute:** Google Colab free tier (T4 GPU)
- **Models/data:** Hugging Face
- **Thinking partner:** Claude / ChatGPT / Gemini

## Learning goals

Python for data work, text processing and NLP, embeddings and semantic search, using LLMs inside code, fine-tuning a small model, git/GitHub, and reading AI output skeptically.

## What this project is not

- Not an attempt to prove or disprove anything metaphysical.
- Not a literature review or philosophy paper.
- Not a product or startup.
- Not finished. A living project.
