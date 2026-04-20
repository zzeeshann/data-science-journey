# 🚀 Start Session 4 — The Wholeness Investigation Begins

*Upload this file along with [00_index.md](00_index.md), [01_working_agreement.md](01_working_agreement.md), [02_project_brief.md](02_project_brief.md), [research_plan_wholeness.md](research_plan_wholeness.md), [sessions/session_03.md](sessions/session_03.md), and the book itself: [data/raw/thinking_in_wholes_2026.docx](data/raw/thinking_in_wholes_2026.docx). Then say "start Session 4".*

---

## Important — read this first

The project changed direction at the end of Session 3. The old plan was: continue the PubMed-vs-James-style histogram comparisons and add more text data points. **That plan is dead.**

The new direction: a multi-session research investigation into whether the worldview shift described in *Thinking in Wholes* (2026) shows up in real data on how humans and societies are doing. Country-scale data. Real Hugging Face models. Four testable hypotheses. 6-10 sessions. The full plan is in [research_plan_wholeness.md](research_plan_wholeness.md). Read it before doing anything else.

## Where we left off

End of Session 3. First two-point comparison done (PubMed vs James 1890). Pipeline works for both modern structured data and historical unstructured text. Project is moving from Phase 1 (count words) to a real research investigation across multiple sessions.

The book *Thinking in Wholes* sharpened sub-question 2 from "how has the language of consciousness shifted" to **"is the worldview shift the book describes — from machine-thinking to systems-thinking — visible in real data on how humans and societies are doing?"**

Four hypotheses to test:
- **H1** — Growth and development have decoupled.
- **H2** — Connection predicts wellbeing better than wealth.
- **H3** — The language of wholeness is rising in modern writing.
- **H4** — Cultures vary systematically in wholeness vs machine framing.

## Session 4's job

**Country-scale wellbeing baseline.** Load the World Happiness Report data. ~150 countries × 10+ years × happiness, social support, GDP, freedom, trust. Make the first cross-country comparison chart. Begin testing H1 and H2.

**The first big question:** is happiness actually correlated with GDP, or has the book's claim — that connection matters more than wealth — got real data behind it?

Concrete output:
- A scatter plot of GDP-per-capita vs happiness across all countries, with outliers labelled by name.
- A correlation number (Pearson's r) for GDP vs happiness, and for social support vs happiness.
- An honest read of which countries break the "richer = happier" assumption, and in which direction.

## New skills introduced in Session 4

- Loading structured tabular data (CSV from Kaggle or Our World in Data).
- Pearson correlation (one number that summarises a relationship).
- Scatter plots with country labels.
- Working with multi-country, multi-year data.

## Shape of the session (same rhythm as Session 3)

1. One Colab cell at a time. Explain, run, paste output, discuss.
2. Get the data loaded and looked at honestly before measuring anything.
3. Make the first chart. Look. Say what we actually see.
4. Don't try to test all of H1 in one session — start it.
5. Close with session_04.md, chapter_05.md, chart in /book/images/, updated 00_index.md and 05_glossary.md if new terms came up.
6. Deliver one bundle for Claude Code at the end.

## Reminders for the assistant (me, in the next chat)

- Beginner who knows some coding. Step by step. One cell at a time. **Do not dump four cells at once.**
- User's Colab is free-tier, one active session. Memory is ephemeral — `df` from a previous session will be gone on reopen. Re-run cells from the top.
- Push back when the user is wrong. Push back when I'm wrong too.
- Definitions go in [05_glossary.md](05_glossary.md), never redefined in chapters.
- Book voice is literary and records what actually happened. Session record is the diary with receipts.
- Image filenames match the chapter: `chapter_05_something.png`.
- Use the user's own screenshots and outputs as-is. Don't regenerate things already generated.
- **Cut the cheerleading.** No "good work today", no "great catch." The user wants honest engagement, not praise. Treat them as a peer.
- The plan is ambitious but the pace stays patient. Session 4 starts H1, doesn't finish it.
- If a session goes long, split it. Don't rush to finish.
- The book *Thinking in Wholes* is the **lens**, not a data point. We measure the world *through* its categories (wholeness, connection, development, system). We do not just compare its word counts to other texts.

## Data source for Session 4 (probable)

- World Happiness Report on Kaggle: `unsdsn/world-happiness` or similar
- Or via Our World in Data: https://ourworldindata.org/happiness-and-life-satisfaction
- Or via the official report PDFs and supplementary data: https://worldhappiness.report/data/

The first thing the assistant should do in Session 4 is decide which source is cleanest and most current — likely a quick web search at session start.

---

*End of kickoff file. The investigation begins.*
