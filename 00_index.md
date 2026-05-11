# 📍 Index — Start Here

*If you're an AI assistant picking this up in a new conversation, read this file first, then [01_working_agreement.md](01_working_agreement.md).*

---

## What this project is

A multi-year data science investigation into how humans describe consciousness, meaning, and the self — and, as the investigation has sharpened, how humans and societies are actually doing under the categories the project's theoretical lens names. Full details in [02_project_brief.md](02_project_brief.md).

**Working sub-question:** #2 — sharpened at end of Session 3 to: *Is the worldview shift described in Thinking in Wholes (2026) — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?* Full plan in [research_plan_wholeness.md](research_plan_wholeness.md).

**Two findings, separately:**

*Country-scale (Chapters 5–6).* Across 141 countries between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained component fell in 98% — the WHR model predicts a substantially happier world than actually exists. Session 5 extended this: 38 countries showed GDP up, HDI flat, happiness declines landing entirely in the residual. Neither income nor development metrics can explain what's falling, and the country-scale work in this book does not name what does.

*Text-level (Chapters 7–9).* The cross-era embedding work produced one positive finding — Reddit r/Meditation ↔ William James 1890 phenomenology of introspection, top pairs at cosines 0.58–0.61, four of five hitting James paragraph #810 on the felt sense of attention turning inward — and two clean falsifications (the structural-position-twelve cluster filed as selection bias; the wholeness-register interpretation falsified by Reddit's negative paired-difference toward pos-12).

**The two halves do not connect statistically.** The connecting word "residual" is metaphorical across them, not a shared variable. Session 10 audited the gap and surfaced it; Chapter 10 names it as the project's structural lesson. Sessions 11–13 wrap the book — lessons-learned chapter, readability pass, summary files. After Session 13 this investigation is complete and the existing book is a conclusive artefact. The project itself stays open — the next investigation will happen on a topic yet to be chosen.

**Repo:** https://github.com/zzeeshann/data-science-journey

---

## The files in this repo

### Root — planning and rules
- **[CLAUDE.md](CLAUDE.md)** — operational brief for Claude Code. Auto-loaded at session start. Covers current state, mechanical conventions, summary of verification habits (full version in `discipline.md`).
- **[discipline.md](discipline.md)** — the rules. Twenty-two disciplines (organised by phase: pre-session, during-session, before-commit, plan-files, end-of-session) plus the drift-response protocol. Required reading every session. If a session is about to violate a rule (or already has), Claude stops, names the rule by number, cites the precedent, and asks before continuing. The single source of truth for *how* the project runs.
- **[00_index.md](00_index.md)** — this file. The map.
- **[01_working_agreement.md](01_working_agreement.md)** — how we work. Voice and collaboration norms; complementary to `discipline.md` (which covers methodology).
- **[02_project_brief.md](02_project_brief.md)** — what the project is.
- **[03_project_structure.md](03_project_structure.md)** — folder layout, Mac setup, GitHub setup.
- **[04_roadmap.md](04_roadmap.md)** — rough plan. Not a commitment, a compass.
- **[05_glossary.md](05_glossary.md)** — definitions of terms. Single source of truth for concepts.
- **[research_plan_wholeness.md](research_plan_wholeness.md)** — the Wholeness Investigation's plan file. Four hypotheses, country-scale data, Hugging Face models. **Historical record now (investigation closed at Session 9).** The next investigation will produce its own plan file.

### `/sessions/` — what we actually did
- **[session_01.md](sessions/session_01.md)** — first session: Colab setup, first LLM run, first observation.
- **[session_02.md](sessions/session_02.md)** — chose sub-question 2, GitHub live, first dataset loaded (PubMed), first measurement, first chart.
- **[session_03.md](sessions/session_03.md)** — loaded William James 1890, first two-point comparison chart. Sub-question sharpened into the research plan.
- **[session_04.md](sessions/session_04.md)** — Wholeness Investigation opens. Loaded WHR 2011–2025. Big finding: 99% of countries' measured factors rose, 98%' unexplained fell.
- **[session_05.md](sessions/session_05.md)** — H1 test. Merged WHR with UNDP HDI 1990–2023. GDP and HDI didn't fully decouple globally (r=0.32) but 38 countries showed GDP up, HDI flat, residual collapsing. Neither income nor development metrics explain the happiness drop. Analysis run in Julius AI.
- **[session_06.md](sessions/session_06.md)** — Process audit, not a finding session. Caught and fixed three image-placement issues and one fabricated book citation in Chapter 6 (Sonnet 4.6 draft, Opus 4.7 audit). Researches whether AI models "get worse over time" — citing Chen/Zaharia/Zou 2023 and Anthropic's April 23 2026 Claude Code postmortem — and folds three new verification habits into the standing process.
- **[session_07.md](sessions/session_07.md)** — Embeddings: first encounter. First NLP session of the project. 1,744 paragraph chunks across *Thinking in Wholes*, the Ackoff lecture, and James 1890 embedded with `all-MiniLM-L6-v2`. Reddit r/Meditation hit HTTP 403 (anonymous JSON hardened) — deferred to Session 9. The unplanned finding: James 1890 ↔ *Thinking in Wholes* 2026 at cosine 0.5376 on a real cross-era resonance, passing the falsification check.
- **[session_08.md](sessions/session_08.md)** — The Oldest Voices. Embedding pipeline extended to a 15-passage verified ancient-text corpus. **Test 1 (12-cluster falsification): null** — sim_12 of +0.2310 sat at the 45th percentile of the 10,000-iteration permutation null (49th excluding I Ching hex-11 as sensitivity), p ≈ 0.51. Cluster filed as selection bias; the structural unit the model recognises is "same text" (sim_12_to_11 = +0.65), not "same position number across texts." **Test 2 (cross-era resonance): positive but compromised** — paired-diff +0.0130, bootstrap CI [+0.0118, +0.0142], sign-flip p = 0.0000, but all top-5 modern↔pos-12 pairs are James 1890↔Legge 1899 I Ching hex-12, raising a translation-register confound. Methodological discovery: position numbers aren't comparable across texts (KTU is a museum index, Faulkner Spell 12 is a scholar's catalogue, Gilgamesh Tablet 12 is the appended Sumerian source) — three of seven planned texts contributed wider-sample-only.
- **[session_09.md](sessions/session_09.md)** — Reddit Lands. Reddit fetch fixed via Hugging Face streaming (`sentence-transformers/reddit-title-body`, filtered to subreddit==Meditation, 76 posts after a 500k-row scan). Three pre-registered tests, one direct attack on Session 8's open question. **Test 2 (translation-register confound retest): wholeness-register interpretation falsified** — Reddit's paired-diff toward pos-12 came in *negative* at −0.0045 (42.1% positive) while the three formal-prose corpora all sat in the +0.012–+0.018 band. The Session 8 cross-era lift is a formal-English-prose register effect, not wholeness language. **Test 1 surfaced the cleanest cross-era finding so far**: Reddit↔James 1890 mean cosine +0.1364 (highest Reddit-to-modern), top pairs at 0.58–0.61 cosine, four of five hitting James paragraph #810 on the phenomenology of inward attention. Modern lay-meditation prose and 19th-century introspection science describe the same kind of moment.
- **[session_10.md](sessions/session_10.md)** — The Honest Pass. Project-level audit, not a finding session. Triggered by user asking *"are we even doing correct investigation?"* Read all 9 sessions + 9 chapters cold; produced [`project_state.md`](project_state.md) at repo root surfacing the structural problem: country-scale work (Sessions 4–6) and text-level work (Sessions 7–9) are two separate investigations the chapters glue together with the word "residual" — the bridge is rhetorical, not empirical. Five options surfaced (A–E). **Decision: Option C with strong Chapter 10** — honest close of Phase 3, with the bridge lesson made the most teachable chapter in the book. Sessions 11–13 wrap up.
- **[session_11.md](sessions/session_11.md)** — Wrap-up 1 of 3. Wrote [`book/chapter_10.md`](book/chapter_10.md) — the lessons-learned chapter — and applied six surgical patches removing the rhetorical-bridge sentences flagged by the Session 10 audit (Chapters 5/6/7/9 and the index hook paragraph). Added dated status notes to all four hypotheses in [`research_plan_wholeness.md`](research_plan_wholeness.md) reflecting what the evidence actually showed vs the original wording. Investigation closed at Session 9; Sessions 12 (book-readability audit) and 13 (summary files) remain.
- **[session_12.md](sessions/session_12.md)** — Wrap-up 2 of 3. Book-readability audit: the 14-year-old pass. Cold-read every chapter into [`notes/book_audit_findings.md`](notes/book_audit_findings.md), then patched in place. Seven new glossary entries (Bootstrap CI, p-value, Paired-difference test, Register, Sign-flip permutation, Subreddit & Pushshift, Vector / vector space) added to [`05_glossary.md`](05_glossary.md). Scale-anchor parentheticals added on first appearance of each dense statistic per chapter (cosines, correlations, p-values, paired-differences); cross-links added on first use of every technical term that has a glossary entry. No rewrites. The chapters' findings, numbers, and voice all stay; only readability changes. Citation-grep verification (Session 6 precedent) caught two paraphrases of *Thinking in Wholes* — both verified clean against the source book. Session 13 (summary files) remains.
- **[session_13.md](sessions/session_13.md)** — Wrap-up 3 of 3. The four summary files at repo root: [`mistakes_made.md`](mistakes_made.md) (six entries — every catch + fix + standing-process habit), [`summary_for_a_reader.md`](summary_for_a_reader.md) (~500-word executive summary in the chapters' voice), [`improvements.md`](improvements.md) (ten numbered points for the next investigation's planning brief), [`reader_glossary_audit.md`](reader_glossary_audit.md) (audit log of Session 12's seven glossary additions, with future-audit slot). With this session the existing book is a complete, conclusive artefact. The project itself remains open — the next investigation has not been chosen.
- **[session_14.md](sessions/session_14.md)** — First session of the post-book project. Methods-acquisition, not a finding session. Local LLM stack stood up on user's M4 Pro Mac in two phases on the same day. **Phase A:** LM Studio + Qwen 2.5 14B Instruct MLX 4-bit on `localhost:1234`; engine bugs surfaced. **Phase B:** Ollama serving `qwen2.5:14b` (GGUF Q4_K_M) on `localhost:11434` — the working stack at end of session. The OpenAI-API contract is identical between stacks, so the swap was a one-line change in `ask_qwen()`. Tutorial walkthroughs authored by DeepSeek (three source files parked in [`data/raw/`](data/raw/)) report 50-article AG News classification at 92% accuracy in both phases — tutorial-grade sanity check, not a benchmark (n=50, no CI, notebooks not preserved, Phase-B independence undetermined from receipts). The project now has two analytical primitives — embeddings-and-cosine-similarity (Sessions 7–9) and LLM-classification-via-prompt (this session). Next investigation question still TBD.

### `/book/` — the personal book, written as we go
- **[chapter_01.md](book/chapter_01.md)** — Why I'm doing this.
- **[chapter_02.md](book/chapter_02.md)** — First contact.
- **[chapter_03.md](book/chapter_03.md)** — First measurement.
- **[chapter_04.md](book/chapter_04.md)** — Two shapes on one page.
- **[chapter_05.md](book/chapter_05.md)** — What the model can't see.
- **[chapter_06.md](book/chapter_06.md)** — The dashboard that couldn't see the drop.
- **[chapter_07.md](book/chapter_07.md)** — First encounter with embeddings. What the model surfaced from the modern corpus. (Title and final summary set at end of Session 7.)
- **[chapter_08.md](book/chapter_08.md)** — The Oldest Voices. The 12-cluster did not survive its falsification test; same-text adjacency dominates the embedding geometry. The cross-era resonance result is positive in aggregate but dominated by James↔I-Ching-hexagram-12 in the qualitative receipts, leaving the translation-register confound as the next thing to control for.
- **[chapter_09.md](book/chapter_09.md)** — Reddit Lands. The wholeness-register interpretation of Session 8's lift falsified: Reddit's paired-diff toward pos-12 ancient is negative. The formal-English-prose corpora share a register that meets Legge 1899's Victorian translation; lay meditation prose doesn't, and doesn't get the lift. The cleanest cross-era result that survived is Reddit r/Meditation ↔ James 1890 phenomenology of introspection, top pairs 0.58–0.61.
- **[chapter_10.md](book/chapter_10.md)** — *What I Got Wrong, and How I Caught It.* The lessons-learned chapter. Names the unit-of-analysis mistake — country-scale residual data and paragraph-level cosines glued together rhetorically without a statistical bridge — that the chapters' framing carried until the Session 10 audit caught it. Plain-language lesson on matching the unit to the question, plus three habits to carry into the next investigation. The most teachable chapter in the book for a beginner.

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
- **[chapter_09_full_landscape.png](book/images/chapter_09_full_landscape.png)** — UMAP 2D projection of all five corpora finally in one frame: tinw, ackoff, james, Reddit r/Meditation, and 15 ancient passages. Reddit's green cluster sits visibly isolated on the left side — the chart-level statement of Session 9's negative paired-difference result.

### `/data/raw/` — source files
- **[hamming_lecture_01_1995.txt](data/raw/hamming_lecture_01_1995.txt)** — Hamming, "Learning to Learn" Lecture 1, 1995. Parked.
- **[ackoff_lecture_systems_age.txt](data/raw/ackoff_lecture_systems_age.txt)** — Ackoff, "From Machine Age to Systems Age." Session 7 reference.
- **[thinking_in_wholes_2026.md](data/raw/thinking_in_wholes_2026.md)** — *Thinking in Wholes* (2026). The lens.
- **[WHR26_Data_Figure_2.1.xlsx](data/raw/WHR26_Data_Figure_2.1.xlsx)** — World Happiness Report 2026 panel. 2,116 rows × 13 cols.
- **[HDR25_Composite_indices_complete_time_series.csv](data/raw/HDR25_Composite_indices_complete_time_series.csv)** — UNDP HDI complete time series 1990–2023, 206 countries, 1,112 columns. Source: hdr.undp.org. Force-add (gitignored).
- **[james_principles_psychology_1890.txt](data/raw/james_principles_psychology_1890.txt)** — William James, *Principles of Psychology* Vol. 1 (1890), Project Gutenberg eBook 57628. Cleaned (Gutenberg wrappers stripped). 1,649,427 chars. Force-add (gitignored). First used in Session 7.
- **[deepseek_local_llm_guide_2026_05_11.html](data/raw/deepseek_local_llm_guide_2026_05_11.html)** — DeepSeek-authored Phase-A tutorial walking through the **LM Studio** path (Qwen 2.5 14B Instruct MLX 4-bit on `localhost:1234`). Complete HTML version with all eight parts. The user worked through this on 2026-05-11 before switching to Ollama. Force-add (gitignored). First used in Session 14.
- **[deepseek_local_llm_guide_2026_05_11.md](data/raw/deepseek_local_llm_guide_2026_05_11.md)** — Same Phase-A tutorial, condensed Markdown. Truncated partway through Part 5; the HTML is the complete reference. Force-add (gitignored). First used in Session 14.
- **[deepseek_local_llm_guide_2026_05_11_ollama.html](data/raw/deepseek_local_llm_guide_2026_05_11_ollama.html)** — DeepSeek-authored Phase-B tutorial walking through the **Ollama** path (`qwen2.5:14b` on `localhost:11434`). Adds the LM-Studio-vs-Ollama comparison (documents *"We switched away due to engine bugs"*), a batch-50 loop with progress reporting, and a Seaborn confusion-matrix cell. Force-add (gitignored). First used in Session 14.

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
- **[session_09_embeddings.py](notebooks/session_09_embeddings.py)** — Session 9 pipeline. Forks the Session 8 script. Replaces the broken anonymous-Reddit-API fetch with a streaming Hugging Face load (`sentence-transformers/reddit-title-body`, subreddit filter, optional `HF_TOKEN` from Colab secrets). Adds the translation-register confound retest (per-corpus paired-difference table including Reddit) and the descriptive Reddit-landing receipts. UMAP chart now spans all five corpora.

### `/notes/` — working notes the audit produced

- **[notes/book_audit_findings.md](notes/book_audit_findings.md)** — Session 12 audit's per-chapter findings list (line-number-specific). Cross-cutting items (new glossary entries, missing cross-links) noted at the bottom. Working doc, not chapter prose.

### Repo-root summary files (Session 13)

- **[mistakes_made.md](mistakes_made.md)** — six-entry mistakes-and-corrections record. Each entry: what happened, where, how it was caught, the fix, the habit added to standing process. Sources: Sessions 5 (chart artefacts), 6 (fabricated quote), 8 (catalogue-vs-position), 9 (pre-registered prediction the data rejected), 10 (unit-of-analysis bridge problem — the largest), 11 (plan-file preservation decision). The most useful single document the project produced for someone planning their own multi-session investigation.
- **[summary_for_a_reader.md](summary_for_a_reader.md)** — ~500-word self-contained executive summary in the chapters' voice. For someone who has not read the book and wants to understand what the project is. Reflects the post-Session-11 *"two findings, separately"* framing: country-scale residual finding (Chapters 5–6) and cross-era Reddit↔James phenomenology resonance (Chapters 7–9), with the connection between them explicitly named as rhetorical-not-statistical.
- **[improvements.md](improvements.md)** — ten numbered points for the next investigation's planning brief. Methodological discipline (1–4), measurement choices (5–8), process discipline (9–10). Most load-bearing: #1 — *write the unit of analysis at the top of every session brief, before any code runs*. Not a self-criticism document; a forward-looking checklist.
- **[reader_glossary_audit.md](reader_glossary_audit.md)** — audit log of glossary additions. Session 12's seven entries each have a section (which chapter triggered it, why a standalone entry was needed, what the entry does). Future audits append below the marker line.

### Repo-root working docs

- **[ANCIENT_TEXTS_READING_GUIDE.md](ANCIENT_TEXTS_READING_GUIDE.md)** — primary-source reading order for the 12-cluster verification, between Sessions 7 and 8.
- **[start_session_08.md](start_session_08.md)** — brief for Session 8 (drafted in a session-planning chat). Reference-only now that Session 8 has run; the falsification rules and pre-registration discipline in this file landed verbatim in [session_08.md](sessions/session_08.md).
- **[start_session_13_book_audit.md](start_session_13_book_audit.md)** — brief for the book-readability audit. Filename frozen at "13" because the queue position shifted; the audit ran as Session 12. The brief itself stays current — Session 13 will use it again as the authoritative reference for the four summary files (`mistakes_made.md`, `summary_for_a_reader.md`, `improvements.md`, `reader_glossary_audit.md`).
- **[project_state.md](project_state.md)** — the Session 10 project-level audit document. Working doc, not chapter prose. Compares chapter framing against session evidence; surfaces the bridge problem; lists five options A–E. Decision was Option C, executed across Sessions 11–13.

---

## How to use this index

- **Starting a new chat?** Upload this file + [01_working_agreement.md](01_working_agreement.md) + [02_project_brief.md](02_project_brief.md) + [research_plan_wholeness.md](research_plan_wholeness.md) + the most recent session record + the book *Thinking in Wholes*.
- **Looking for a definition?** Check [05_glossary.md](05_glossary.md).
- **Looking for what we did last?** Check [session_14.md](sessions/session_14.md). First session of the post-book project — local LLM stack stood up on the user's Mac in two phases on the same day (LM Studio first, then **Ollama** after engine bugs); classification-via-prompt added as a second analytical primitive alongside the Sessions 7–9 embeddings pipeline. Methods acquisition, not a finding. The next investigation question has not been chosen.
- **Looking for the personal story?** Read `/book/` in order.
- **Looking for project direction?** Read [research_plan_wholeness.md](research_plan_wholeness.md).
- **Looking for the current hook?** The Wholeness Investigation closed at Session 9. Two findings stand on their own: the country-scale residual fall (Chapters 5–6) and the cross-era Reddit↔James phenomenology resonance (Chapters 7–9). The two halves do not connect statistically — see Chapter 10 for the lessons-learned account. Sessions 11–13 wrapped the book. Session 14 (May 2026) is the first session of the post-book project: a local LLM analysis stack is now running on the user's Mac (**Ollama** serving `qwen2.5:14b` on `localhost:11434`, after a Phase-A attempt on LM Studio was abandoned for engine bugs), adding classification-via-prompt as a second analytical primitive alongside the embedding pipeline. The next investigation question is not yet chosen.

---

*Keep this file updated. Every new file added = one new line here.*
