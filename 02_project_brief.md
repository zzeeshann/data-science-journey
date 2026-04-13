# 📄 Project Brief — The Shadow of Consciousness

*A data science project exploring how humans describe consciousness, meaning, and the self across cultures, eras, and traditions.*

**Started:** April 2026
**Status:** Phase 1 — foundations
**Related:** [03_project_structure.md](03_project_structure.md) · [04_roadmap.md](04_roadmap.md)

---

## The question behind the project

The question that pulled me into this work is metaphysical: **is consciousness a product of the brain, or is consciousness primary and the brain its instrument?** This cannot be answered with data — it's one of the deepest open problems in philosophy (Chalmers's "hard problem").

But the question leaves a *trace* in human language. Across thousands of years of writing — mystics, neuroscientists, philosophers, poets, trip reports — humans have tried to describe consciousness. That trace is real. That trace is data.

**This project doesn't try to answer the metaphysical question. It maps its shadow in how humans have written about consciousness across traditions and eras.**

## The three sub-questions

1. **Do people who describe mystical or non-dual experiences use consistent language across cultures and eras?** (Rumi, Meister Eckhart, Ramana Maharshi, near-death reports, psychedelic trip reports.)
2. **How has the language of consciousness shifted from religious to neuroscientific over the last 200 years?**
3. **Do materialist and non-materialist thinkers describe the *experience* of consciousness differently, or only the *explanation* of it?**

One sub-question will be chosen as the working focus. *(Not yet chosen — next decision.)*

## Data sources (candidate)

All free and public: Project Gutenberg, Hugging Face Datasets, Reddit archives (r/Meditation, r/NDE, r/Psychonaut), arXiv/PubMed abstracts, public-domain translations of mystical texts.

## Methods (planned)

Starting simple, building up:
- **Phase 1** — Exploration. Load data. Count words. Simple charts.
- **Phase 2** — Text cleaning, tokenising, frequency comparison.
- **Phase 3** — Embeddings for semantic comparison.
- **Phase 4** — LLM-assisted theme extraction.
- **Phase 5** — Fine-tune a small model on a chosen corpus.

## Deliverables

- Written report per sub-question.
- Jupyter notebooks showing analysis step by step.
- Cleaned datasets in `/data/processed/`.
- At least one fine-tuned model on Hugging Face.
- The book (see `/book/`).

## Learning goals

By completing this project I will learn: Python for data work, text processing and NLP, embeddings and semantic search, using LLMs inside code, fine-tuning a small model, git/GitHub, and the critical skill of reading AI output skeptically (the "sense of drift").

## What this project is not

- Not an attempt to prove or disprove anything metaphysical.
- Not a literature review or philosophy paper.
- Not a product or startup.
- Not finished. A living project.

## Honest risks

- **Selection bias** in texts chosen.
- **Translation drift** for mystical texts.
- **LLM hallucination** on any model output — every finding must trace back to real data.
- **Scope creep** — the question is enormous. Stay narrow, go deep.

## Success tests

At the end of the project:
1. I can talk about what I did with a technical person, no notes.
2. The repo is something I'm proud to link in a job application.
3. I understand my own question *better* — even if I don't have an answer.
