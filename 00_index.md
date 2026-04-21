# 📍 Index — Start Here

*If you're an AI assistant picking this up in a new conversation, read this file first, then [01_working_agreement.md](01_working_agreement.md).*

---

## What this project is

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories the project's theoretical lens names. Full details in [02_project_brief.md](02_project_brief.md).

**Working sub-question:** #2 — sharpened at end of Session 3 to: *Is the worldview shift described in Thinking in Wholes (2026) — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?* Full plan in [research_plan_wholeness.md](research_plan_wholeness.md).

**Session 4 finding (the hook the investigation now orbits):** across 141 countries, between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained component fell in 98%. The WHR model predicts a substantially happier world than actually exists. Something systematic is moving outside the six measured variables, in the same direction, almost everywhere. The rest of the investigation is trying to name it.

**Repo:** https://github.com/zzeeshann/data-science-journey

---

## The files in this repo

### Root — planning and rules
- **[00_index.md](00_index.md)** — this file. The map.
- **[01_working_agreement.md](01_working_agreement.md)** — how we work. The rules of engagement.
- **[02_project_brief.md](02_project_brief.md)** — what the project is. Revised at end of Session 4 to remove the job-in-six-months framing and reflect the multi-year investigative ambition.
- **[03_project_structure.md](03_project_structure.md)** — folder layout, Mac setup, GitHub setup.
- **[04_roadmap.md](04_roadmap.md)** — rough plan. Not a commitment, a compass.
- **[05_glossary.md](05_glossary.md)** — definitions of terms. Single source of truth for concepts.
- **[research_plan_wholeness.md](research_plan_wholeness.md)** — the multi-session investigation plan. Four hypotheses, country-scale data, Hugging Face models. **Read this for project direction.**

### `/sessions/` — what we actually did
- **[session_01.md](sessions/session_01.md)** — first session: Colab setup, first LLM run, first observation.
- **[session_02.md](sessions/session_02.md)** — chose sub-question 2, GitHub live, first dataset loaded (PubMed), first measurement, first chart.
- **[session_03.md](sessions/session_03.md)** — loaded William James 1890 from Project Gutenberg, cleaned, filtered to paragraphs, first two-point comparison chart (PubMed vs James). Sub-question sharpened at end into the research plan.
- **[session_04.md](sessions/session_04.md)** — Wholeness Investigation opens. Loaded WHR 2011-2025. Cross-section correlations for H2 came back tied (0.812 vs 0.799, noise). Extension to 2019–2025 time series revealed the big finding: 99% of countries' measured factors rose, 98%' unexplained component fell. UK post-2019 decline is a concrete case. All four hypotheses now orbit "what is in the residual?"

### `/book/` — the personal book, written as we go
- **[chapter_01.md](book/chapter_01.md)** — Why I'm doing this.
- **[chapter_02.md](book/chapter_02.md)** — First contact.
- **[chapter_03.md](book/chapter_03.md)** — First measurement.
- **[chapter_04.md](book/chapter_04.md)** — Two shapes on one page.
- **[chapter_05.md](book/chapter_05.md)** — What the model can't see.

### `/book/images/`
- **[chapter_04_comparison.png](book/images/chapter_04_comparison.png)** — PubMed 2020s vs James 1890 side-by-side histogram.
- **[chapter_05_gdp_happiness.png](book/images/chapter_05_gdp_happiness.png)** — GDP vs happiness scatter, 144 countries, 2025, with line of best fit and labelled residuals.
- **[chapter_05_uk_decomposition.png](book/images/chapter_05_uk_decomposition.png)** — UK 2019–2025 two-panel close-up: happiness fell while measured factors rose; the unexplained collapsed.
- **[chapter_05_measured_vs_unexplained.png](book/images/chapter_05_measured_vs_unexplained.png)** — global scatter, 141 countries, 2019–2025: change in measured factors vs change in unexplained component, coloured by net happiness change. The big finding, in one chart.

### `/data/raw/` — source texts kept for analysis
- **[hamming_lecture_01_1995.txt](data/raw/hamming_lecture_01_1995.txt)** — Hamming, "Learning to Learn" Lecture 1, 1995. Parked.
- **[ackoff_lecture_systems_age.txt](data/raw/ackoff_lecture_systems_age.txt)** — Ackoff, "From Machine Age to Systems Age," ~1980s. Session 6 reference.
- **[thinking_in_wholes_2026.docx](data/raw/thinking_in_wholes_2026.docx)** — *Thinking in Wholes* (2026). The lens, not a data point.
- **[WHR26_Data_Figure_2.1.xlsx](data/raw/WHR26_Data_Figure_2.1.xlsx)** — World Happiness Report 2026 "Data for Figure 2.1" panel. 2,116 rows × 13 cols. Countries × years 2011–2025 with life evaluation and six factor contributions.

### `/data/processed/` — cleaned data products
- **[whr2025_clean.csv](data/processed/whr2025_clean.csv)** — 144-country 2025 cross-section. Renamed columns, Venezuela dropped, NaN rows removed.
- **[whr_changes_2019_2025.csv](data/processed/whr_changes_2019_2025.csv)** — 141-country change panel. 2019 level + 2025 level + delta for every factor, plus the `d_measured_sum` column used for the global scatter. Starting point for further investigations of the residual.

---

## How to use this index

- **Starting a new chat?** Upload this file + [01_working_agreement.md](01_working_agreement.md) + [02_project_brief.md](02_project_brief.md) + [research_plan_wholeness.md](research_plan_wholeness.md) + the most recent session record + the book *Thinking in Wholes*. The next session's kickoff file if one has been drafted.
- **Looking for a definition?** Check [05_glossary.md](05_glossary.md).
- **Looking for what we did last?** Check the most recent file in `/sessions/`.
- **Looking for the personal story?** Read `/book/` in order.
- **Looking for project direction?** Read [research_plan_wholeness.md](research_plan_wholeness.md).
- **Looking for the current hook?** "Name what is in the residual." That's what Sessions 5–10 are for.

---

*Keep this file updated. Every new file added = one new line here.*
