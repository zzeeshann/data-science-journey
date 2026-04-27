# 📍 Index — Start Here

*If you're an AI assistant picking this up in a new conversation, read this file first, then [01_working_agreement.md](01_working_agreement.md).*

---

## What this project is

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories the project's theoretical lens names. Full details in [02_project_brief.md](02_project_brief.md).

**Working sub-question:** #2 — sharpened at end of Session 3 to: *Is the worldview shift described in Thinking in Wholes (2026) — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?* Full plan in [research_plan_wholeness.md](research_plan_wholeness.md).

**The hook the investigation now orbits:** across 141 countries between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained component fell in 98%. The WHR model predicts a substantially happier world than actually exists. Session 5 extended this: 38 countries showed GDP up, HDI flat, and happiness declines landing entirely in the residual. Neither income nor development metrics can explain what's falling. The investigation is trying to name it.

**Repo:** https://github.com/zzeeshann/data-science-journey

---

## The files in this repo

### Root — planning and rules
- **[00_index.md](00_index.md)** — this file. The map.
- **[01_working_agreement.md](01_working_agreement.md)** — how we work. The rules of engagement.
- **[02_project_brief.md](02_project_brief.md)** — what the project is.
- **[03_project_structure.md](03_project_structure.md)** — folder layout, Mac setup, GitHub setup.
- **[04_roadmap.md](04_roadmap.md)** — rough plan. Not a commitment, a compass.
- **[05_glossary.md](05_glossary.md)** — definitions of terms. Single source of truth for concepts.
- **[research_plan_wholeness.md](research_plan_wholeness.md)** — the multi-session investigation plan. Four hypotheses, country-scale data, Hugging Face models. **Read this for project direction.**

### `/sessions/` — what we actually did
- **[session_01.md](sessions/session_01.md)** — first session: Colab setup, first LLM run, first observation.
- **[session_02.md](sessions/session_02.md)** — chose sub-question 2, GitHub live, first dataset loaded (PubMed), first measurement, first chart.
- **[session_03.md](sessions/session_03.md)** — loaded William James 1890, first two-point comparison chart. Sub-question sharpened into the research plan.
- **[session_04.md](sessions/session_04.md)** — Wholeness Investigation opens. Loaded WHR 2011–2025. Big finding: 99% of countries' measured factors rose, 98%' unexplained fell.
- **[session_05.md](sessions/session_05.md)** — H1 test. Merged WHR with UNDP HDI 1990–2023. GDP and HDI didn't fully decouple globally (r=0.32) but 38 countries showed GDP up, HDI flat, residual collapsing. Neither income nor development metrics explain the happiness drop. Analysis run in Julius AI.

### `/book/` — the personal book, written as we go
- **[chapter_01.md](book/chapter_01.md)** — Why I'm doing this.
- **[chapter_02.md](book/chapter_02.md)** — First contact.
- **[chapter_03.md](book/chapter_03.md)** — First measurement.
- **[chapter_04.md](book/chapter_04.md)** — Two shapes on one page.
- **[chapter_05.md](book/chapter_05.md)** — What the model can't see.
- **[chapter_06.md](book/chapter_06.md)** — The dashboard that couldn't see the drop.

### `/book/images/`
- **[chapter_04_comparison.png](book/images/chapter_04_comparison.png)** — PubMed 2020s vs James 1890 side-by-side histogram.
- **[chapter_05_gdp_happiness.png](book/images/chapter_05_gdp_happiness.png)** — GDP vs happiness scatter, 144 countries, 2025.
- **[chapter_05_uk_decomposition.png](book/images/chapter_05_uk_decomposition.png)** — UK 2019–2025 two-panel close-up.
- **[chapter_05_measured_vs_unexplained.png](book/images/chapter_05_measured_vs_unexplained.png)** — global scatter, 141 countries, the big finding.
- **[chapter_06_hdi_global_trend.png](book/images/chapter_06_hdi_global_trend.png)** — Mean global HDI 1990–2023 with 2019 marker. Thirty years of progress then a stall.
- **[chapter_06_gdp_hdi_scatter.png](book/images/chapter_06_gdp_hdi_scatter.png)** — GDP-factor change vs HDI change, 129 countries. r=0.32, wide spread.
- **[chapter_06_residual_hdi_scatter.png](book/images/chapter_06_residual_hdi_scatter.png)** — Residual change vs HDI change. Weak bivariate relationship (r=0.11).
- **[chapter_06_residual_hdi_labelled.png](book/images/chapter_06_residual_hdi_labelled.png)** — Same scatter, labelled: UK, US, Canada, Finland, Viet Nam, India. Coloured by happiness change.
- **[chapter_06_hdi_groups_boxplot.png](book/images/chapter_06_hdi_groups_boxplot.png)** — Residual change by HDI-change group (stagnating / middle / improving). Distributions barely differ.
- **[chapter_06_h1_health_scatter.png](book/images/chapter_06_h1_health_scatter.png)** — H1 subset (38 countries): residual vs health factor. Strongest signal inside the group.
- **[chapter_06_uk_hdi_happiness.png](book/images/chapter_06_uk_hdi_happiness.png)** — UK HDI 2010–2023 alongside happiness reference points. Flat development, falling happiness.

### `/data/raw/` — source files
- **[hamming_lecture_01_1995.txt](data/raw/hamming_lecture_01_1995.txt)** — Hamming, "Learning to Learn" Lecture 1, 1995. Parked.
- **[ackoff_lecture_systems_age.txt](data/raw/ackoff_lecture_systems_age.txt)** — Ackoff, "From Machine Age to Systems Age." Session 6 reference.
- **[thinking_in_wholes_2026.md](data/raw/thinking_in_wholes_2026.md)** — *Thinking in Wholes* (2026). The lens.
- **[WHR26_Data_Figure_2.1.xlsx](data/raw/WHR26_Data_Figure_2.1.xlsx)** — World Happiness Report 2026 panel. 2,116 rows × 13 cols.
- **[HDR25_Composite_indices_complete_time_series.csv](data/raw/HDR25_Composite_indices_complete_time_series.csv)** — UNDP HDI complete time series 1990–2023, 206 countries, 1,112 columns. Source: hdr.undp.org. Force-add (gitignored).

### `/data/processed/` — cleaned data products
- **[whr2025_clean.csv](data/processed/whr2025_clean.csv)** — 144-country 2025 cross-section.
- **[whr_changes_2019_2025.csv](data/processed/whr_changes_2019_2025.csv)** — 141-country change panel, the Session 4 big finding dataset.
- **[session_05_merged.csv](data/processed/session_05_merged.csv)** — 129-country merged panel: WHR 2019→2025 changes + HDI by year 1990–2023 + computed d_hdi columns. Built in Session 5. Starting point for all future HDI analysis.

---

## How to use this index

- **Starting a new chat?** Upload this file + [01_working_agreement.md](01_working_agreement.md) + [02_project_brief.md](02_project_brief.md) + [research_plan_wholeness.md](research_plan_wholeness.md) + the most recent session record + the book *Thinking in Wholes*.
- **Looking for a definition?** Check [05_glossary.md](05_glossary.md).
- **Looking for what we did last?** Check [session_05.md](sessions/session_05.md).
- **Looking for the personal story?** Read `/book/` in order.
- **Looking for project direction?** Read [research_plan_wholeness.md](research_plan_wholeness.md).
- **Looking for the current hook?** "Name what is in the residual." Sessions 6–10 are for that.

---

*Keep this file updated. Every new file added = one new line here.*
