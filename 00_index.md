# 📍 Index — Start Here

*If you're an AI assistant picking this up in a new conversation, read this file first, then [01_working_agreement.md](01_working_agreement.md).*

---

## What this project is

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories the project's theoretical lens names. Full details in [02_project_brief.md](02_project_brief.md).

**Working sub-question:** #2 — sharpened at end of Session 3 to: *Is the worldview shift described in Thinking in Wholes (2026) — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?* Full plan in [research_plan_wholeness.md](research_plan_wholeness.md).

**The hook the investigation now orbits:** across 141 countries between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained component fell in 98%. The WHR model predicts a substantially happier world than actually exists. Session 5 extended this: 38 countries showed GDP up, HDI flat, and happiness declines landing entirely in the residual. Neither income nor development metrics can explain what's falling. The investigation is trying to name it. Phase 3 (Sessions 7–12) attacks the question through language: Session 7 built the pipeline on a modern corpus, Session 8 ran the first quantitative test of the 12-cluster on a verified ancient-text corpus and filed the cluster as selection bias (sim_12 sat at the 45th percentile of the permutation null), with a small but reliable cross-era resonance result that needs translation-register controls before it can be claimed.

**Repo:** https://github.com/zzeeshann/data-science-journey

---

## The files in this repo

### Root — planning and rules
- **[CLAUDE.md](CLAUDE.md)** — operational brief for Claude Code. Auto-loaded at session start. Covers current state, mechanical conventions, verification habits.
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
- **[session_06.md](sessions/session_06.md)** — Process audit, not a finding session. Caught and fixed three image-placement issues and one fabricated book citation in Chapter 6 (Sonnet 4.6 draft, Opus 4.7 audit). Researches whether AI models "get worse over time" — citing Chen/Zaharia/Zou 2023 and Anthropic's April 23 2026 Claude Code postmortem — and folds three new verification habits into the standing process.
- **[session_07.md](sessions/session_07.md)** — Embeddings: first encounter. First NLP session of the project. 1,744 paragraph chunks across *Thinking in Wholes*, the Ackoff lecture, and James 1890 embedded with `all-MiniLM-L6-v2`. Reddit r/Meditation hit HTTP 403 (anonymous JSON hardened) — deferred to Session 9. The unplanned finding: James 1890 ↔ *Thinking in Wholes* 2026 at cosine 0.5376 on a real cross-era resonance, passing the falsification check.
- **[session_08.md](sessions/session_08.md)** — The Oldest Voices. Embedding pipeline extended to a 15-passage verified ancient-text corpus. **Test 1 (12-cluster falsification): null** — sim_12 of +0.2310 sat at the 45th percentile of the 10,000-iteration permutation null (49th excluding I Ching hex-11 as sensitivity), p ≈ 0.51. Cluster filed as selection bias; the structural unit the model recognises is "same text" (sim_12_to_11 = +0.65), not "same position number across texts." **Test 2 (cross-era resonance): positive but compromised** — paired-diff +0.0130, bootstrap CI [+0.0118, +0.0142], sign-flip p = 0.0000, but all top-5 modern↔pos-12 pairs are James 1890↔Legge 1899 I Ching hex-12, raising a translation-register confound. Methodological discovery: position numbers aren't comparable across texts (KTU is a museum index, Faulkner Spell 12 is a scholar's catalogue, Gilgamesh Tablet 12 is the appended Sumerian source) — three of seven planned texts contributed wider-sample-only.

### `/book/` — the personal book, written as we go
- **[chapter_01.md](book/chapter_01.md)** — Why I'm doing this.
- **[chapter_02.md](book/chapter_02.md)** — First contact.
- **[chapter_03.md](book/chapter_03.md)** — First measurement.
- **[chapter_04.md](book/chapter_04.md)** — Two shapes on one page.
- **[chapter_05.md](book/chapter_05.md)** — What the model can't see.
- **[chapter_06.md](book/chapter_06.md)** — The dashboard that couldn't see the drop.
- **[chapter_07.md](book/chapter_07.md)** — First encounter with embeddings. What the model surfaced from the modern corpus. (Title and final summary set at end of Session 7.)
- **[chapter_08.md](book/chapter_08.md)** — The Oldest Voices. The 12-cluster did not survive its falsification test; same-text adjacency dominates the embedding geometry. The cross-era resonance result is positive in aggregate but dominated by James↔I-Ching-hexagram-12 in the qualitative receipts, leaving the translation-register confound as the next thing to control for.

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
- **[chapter_07_embedding_landscape.png](book/images/chapter_07_embedding_landscape.png)** — UMAP 2D projection of four modern corpora (Thinking in Wholes, Ackoff, James 1890, Reddit r/Meditation), coloured by source. all-MiniLM-L6-v2.
- **[chapter_08_cross_era.png](book/images/chapter_08_cross_era.png)** — UMAP 2D projection of three modern corpora plus 15 verified ancient passages. Marker shape encodes ancient position (★ position 12, ◆ position 11/13 control, ▪ wider sample). The position-12 stars sit mixed in with the controls — the visual confirmation of the null cluster result.

### `/data/raw/` — source files
- **[hamming_lecture_01_1995.txt](data/raw/hamming_lecture_01_1995.txt)** — Hamming, "Learning to Learn" Lecture 1, 1995. Parked.
- **[ackoff_lecture_systems_age.txt](data/raw/ackoff_lecture_systems_age.txt)** — Ackoff, "From Machine Age to Systems Age." Session 7 reference.
- **[thinking_in_wholes_2026.md](data/raw/thinking_in_wholes_2026.md)** — *Thinking in Wholes* (2026). The lens.
- **[WHR26_Data_Figure_2.1.xlsx](data/raw/WHR26_Data_Figure_2.1.xlsx)** — World Happiness Report 2026 panel. 2,116 rows × 13 cols.
- **[HDR25_Composite_indices_complete_time_series.csv](data/raw/HDR25_Composite_indices_complete_time_series.csv)** — UNDP HDI complete time series 1990–2023, 206 countries, 1,112 columns. Source: hdr.undp.org. Force-add (gitignored).
- **[james_principles_psychology_1890.txt](data/raw/james_principles_psychology_1890.txt)** — William James, *Principles of Psychology* Vol. 1 (1890), Project Gutenberg eBook 57628. Cleaned (Gutenberg wrappers stripped). 1,649,427 chars. Force-add (gitignored). First used in Session 7.

### `/data/processed/` — cleaned data products
- **[whr2025_clean.csv](data/processed/whr2025_clean.csv)** — 144-country 2025 cross-section.
- **[whr_changes_2019_2025.csv](data/processed/whr_changes_2019_2025.csv)** — 141-country change panel, the Session 4 big finding dataset.
- **[session_05_merged.csv](data/processed/session_05_merged.csv)** — 129-country merged panel: WHR 2019→2025 changes + HDI by year 1990–2023 + computed d_hdi columns. Built in Session 5. Starting point for all future HDI analysis.

### `/ancient_voices/` — corpus folder (added Session 7)

- **[ancient_voices/README.md](ancient_voices/README.md)** — what's here, what's not, the verification standard.
- **[ancient_voices/passages/README.md](ancient_voices/passages/README.md)** — format spec for verified passage files.
- `ancient_voices/passages/` — verified primary-source passages, loaded into the embedding pipeline from Session 8 onward.
- `ancient_voices/notes/` — working notes from primary-source reading. Not embedded; not load-bearing for analysis.

### `/notebooks/` — Colab pipelines

- **[session_07_embeddings.py](notebooks/session_07_embeddings.py)** — full Session 7 pipeline. Loads four corpora, embeds with `all-MiniLM-L6-v2`, computes pairwise cosine similarity, runs the three reads, saves the 2D UMAP chart. Designed to be reused in Session 8 with one extra `load_corpus("ancient_voices/passages/")` call.
- **[session_08_embeddings.py](notebooks/session_08_embeddings.py)** — Session 8 pipeline. Forks the Session 7 script. Adds the ancient-corpus loader (15 verified passages, fetched by raw URL), the 12-cluster falsification block (10,000-iteration permutation test with iching-hex-11 sensitivity rerun), the cross-era paired-difference test (bootstrap CI + sign-flip p), and the combined modern + ancient UMAP chart.

### Repo-root working docs

- **[ANCIENT_TEXTS_READING_GUIDE.md](ANCIENT_TEXTS_READING_GUIDE.md)** — primary-source reading order for the 12-cluster verification, between Sessions 7 and 8.
- **[start_session_08.md](start_session_08.md)** — brief for Session 8 (drafted in a session-planning chat). Reference-only now that Session 8 has run; the falsification rules and pre-registration discipline in this file landed verbatim in [session_08.md](sessions/session_08.md).

---

## How to use this index

- **Starting a new chat?** Upload this file + [01_working_agreement.md](01_working_agreement.md) + [02_project_brief.md](02_project_brief.md) + [research_plan_wholeness.md](research_plan_wholeness.md) + the most recent session record + the book *Thinking in Wholes*.
- **Looking for a definition?** Check [05_glossary.md](05_glossary.md).
- **Looking for what we did last?** Check [session_08.md](sessions/session_08.md).
- **Looking for the personal story?** Read `/book/` in order.
- **Looking for project direction?** Read [research_plan_wholeness.md](research_plan_wholeness.md).
- **Looking for the current hook?** "Name what is in the residual." Sessions 7–12 are Phase 3: embeddings + cross-era comparison + Reddit zero-shot + WVS + topic modelling, ending in a synthesis. Session 7 is the first NLP session. (Session 6 was a process audit, not a finding session — see [session_06.md](sessions/session_06.md).)

---

*Keep this file updated. Every new file added = one new line here.*
