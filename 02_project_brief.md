# 📄 Project Brief — The Shadow of Consciousness

*A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and how societies around the world are actually doing under the categories the project's theoretical lens names.*

**Started:** April 2026
**Status:** Wholeness Investigation in progress (Sessions 4 onwards).
**Related:** [03_project_structure.md](03_project_structure.md) · [04_roadmap.md](04_roadmap.md) · [research_plan_wholeness.md](research_plan_wholeness.md)

---

## The question behind the project

The question that pulled me into this work is metaphysical: **is consciousness a product of the brain, or is consciousness primary and the brain its instrument?** This cannot be answered with data — it's one of the deepest open problems in philosophy (Chalmers's "hard problem").

But the question leaves a *trace* in human language. Across thousands of years of writing — mystics, neuroscientists, philosophers, poets, trip reports — humans have tried to describe consciousness. That trace is real. That trace is data.

**This project doesn't try to answer the metaphysical question. It maps its shadow in how humans have written about consciousness across traditions and eras — and, as the investigation has sharpened, how humans and societies are actually doing under the categories the theoretical lens names.**

## The three sub-questions

1. **Do people who describe mystical or non-dual experiences use consistent language across cultures and eras?** (Rumi, Meister Eckhart, Ramana Maharshi, near-death reports, psychedelic trip reports.)
2. **How has the language of consciousness shifted from religious to neuroscientific over the last 200 years?** — *sharpened at end of Session 3 to:* **is the worldview shift described in Thinking in Wholes (2026) — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?**
3. **Do materialist and non-materialist thinkers describe the *experience* of consciousness differently, or only the *explanation* of it?**

**Working focus:** sub-question 2, now the Wholeness Investigation. See [research_plan_wholeness.md](research_plan_wholeness.md) for the four hypotheses, six-to-ten session arc, and data sources.

## The ambition

This is a piece of immense, multi-level research — not a bootcamp exercise, not a portfolio piece, not a certificate. The ambition is to do real investigative work that holds up to adult scrutiny: to take a serious theoretical claim (the shift from machine-thinking to systems-thinking), operationalise it across country-scale wellbeing data, large text corpora, cross-cultural values surveys, and modern NLP, and write down honestly what the data says — including when it surprises me, including when it breaks my prior, including when a finding I wanted has to be withdrawn on cleaning. The work should read, at the end, like a sustained argument by a careful person, not like the output of a course.

## Data sources

All free, all public.

**Country-scale wellbeing and development:**
- World Happiness Report (country × year, 2011–2025) — loaded Session 4.
- UN Human Development Index, 1990–2024.
- Our World in Data — life expectancy, loneliness, social trust.
- World Bank Open Data — GDP, inequality, education.
- World Values Survey — values across ~100 countries and 40 years.

**Text at scale (Hugging Face):**
- Reddit corpora (r/Meditation, r/NDE, r/decidingtobebetter, r/loneliness, r/Psychonaut).
- News datasets — multi-decade headline and article corpora.
- Wikipedia and other reference corpora.
- Project Gutenberg for historical depth (William James already in repo).

**The theoretical lens:**
- *Thinking in Wholes* (2026), parked in `/data/raw/`. Supplies the categories the investigation measures the world against — wholeness, connection, development, system.
- Ackoff's "Machine Age to Systems Age" lecture, parked for Session 6 (embeddings).

## Methods

- **Phase 1 (Sessions 1–3):** Exploration. Load data. Count words. Simple charts. First two-point comparison.
- **Phase 2 (Sessions 4–5):** Country-scale wellbeing and development. World Happiness Report, HDI, GDP. Cross-country panels, correlations, decompositions.
- **Phase 3 (Sessions 6–7):** Embeddings and zero-shot classification. Semantic comparison of the book, Ackoff, James, Reddit corpora. Quantify the language of wholeness.
- **Phase 4 (Sessions 8–9):** Cross-cultural values (World Values Survey) and topic modelling on large corpora.
- **Phase 5 (Session 10 and beyond):** Synthesis. Pull every finding into one piece of writing. If the work is strong enough, it becomes a public artefact.

## Deliverables

- The book (in `/book/`), written as I go, chapter by session when a chapter is warranted.
- Session records with receipts (in `/sessions/`).
- Processed datasets (`/data/processed/`), reusable across sessions.
- Charts and figures (`/book/images/`).
- At least one piece of non-trivial modern-NLP work — embeddings, zero-shot classification, or a small fine-tune — used to answer a specific question in the investigation, not as a demo.
- One integrated synthesis piece at the end of the Wholeness Investigation, defensible to an intelligent reader who disagrees with the book's framing.

## What I'll learn along the way

Python for data work, pandas, text processing, scikit-learn, embeddings and semantic search, using LLMs inside code, fine-tuning a small model, git and GitHub, matplotlib, and — the skill the whole project trains — reading AI and data output skeptically. The "sense of drift." Noticing when a finding is too clean, or when one data point moved a story, or when a label stops meaning what you thought it meant.

## What this project is not

- Not an attempt to prove or disprove anything metaphysical.
- Not a literature review or philosophy paper.
- Not a product or startup.
- Not a portfolio piece optimised for a job application.
- Not a course.
- Not finished. A living project.

## Honest risks

- **Selection bias** in the texts chosen.
- **Translation drift** for mystical and cross-cultural texts.
- **LLM hallucination** on any model output — every finding must trace back to real data.
- **Scope creep** — the question is enormous. Stay narrow inside each session, go deep.
- **Overclaiming from the book.** The book is the lens, not the ground truth. Its claims are hypotheses. The data is allowed to disagree with it. It already has (Session 4's H2 single-year test was inconclusive), and the investigation is better for it.

## Success tests

At the end of the investigation:

1. I can walk a serious reader through what I did, why, and what I found, without notes, and defend every finding against a knowledgeable objection.
2. The work stands as an honest piece of independent research — something I'd put my name on a decade from now, whether or not anyone reads it.
3. I understand my own question *better* — even where I don't have an answer.
4. The book is a coherent argument, not a scrapbook. Each chapter earns its place.
