# CLAUDE.md — Operational brief for Claude Code

If you're a Claude Code agent picking up this repo in a new session, read this file first. It's the operational handoff. The project content and voice rules live elsewhere.

## Reading order at the start of a session

1. **This file** — current state, mechanics, what's next.
2. **[discipline.md](discipline.md)** — the rules. Twenty-two disciplines + drift-response protocol. Required reading. If a session is about to violate a rule (or already has), Claude stops, names the rule by number, cites the precedent, and asks before continuing.
3. **[01_working_agreement.md](01_working_agreement.md)** — how we work. Voice, setup, end-of-session ritual. Source of truth on conduct.
4. **[00_index.md](00_index.md)** — the map of every file in the repo.
5. **The active investigation's plan file** — currently none. The Wholeness Investigation closed at Session 9 and the book closed at Session 13. [`research_plan_wholeness.md`](research_plan_wholeness.md) remains as historical record. The next investigation will produce its own plan file when chosen.
6. **The most recent file in `sessions/`** — what just happened. Currently [`sessions/session_13.md`](sessions/session_13.md).
7. **[02_project_brief.md](02_project_brief.md)** — what the project is. Multi-year investigative ambition. Read once; do not reintroduce the retracted six-month/job framing.
8. **The active investigation's lens text** — for the wholeness investigation that was [`data/raw/thinking_in_wholes_2026.md`](data/raw/thinking_in_wholes_2026.md). Future investigations may use a different lens; check the active plan file when one exists.

If a question is about which rules apply or whether a step is required → `discipline.md`.
If a question is about voice, scope, or working style → `01_working_agreement.md`.
If a question is about content or where the project is going → the active plan file + the latest session record.
If a question is about mechanics (commits, force-adds, file conventions, verification specifics) → this file.

---

## Where the project is right now

**State:** The Wholeness Investigation closed at Session 9. Sessions 10–13 wrapped the book. The book is now a complete, conclusive artefact — ten chapters, thirteen session records, glossary, plan, audit notes, and four summary files at repo root ([`mistakes_made.md`](mistakes_made.md), [`summary_for_a_reader.md`](summary_for_a_reader.md), [`improvements.md`](improvements.md), [`reader_glossary_audit.md`](reader_glossary_audit.md)). The project itself stays open. Session 14 (2026-05-11) opened the post-book project: a **local LLM analysis stack** now runs on the user's M4 Pro Mac — LM Studio + Qwen 2.5 14B Instruct MLX 4-bit + Jupyter, driven via the `localhost:1234` OpenAI-compatible API. Capability acquisition, not a finding. The next investigation question has not been chosen.

**Two findings the existing book documents:**
- *Country-scale (Chapters 5–6).* Across 141 countries between 2019 and 2025, the WHR's six measured factors rose in 99% of countries while the unexplained residual fell in 98%. Session 5 ruled out HDI stagnation: 38 of 129 countries showed GDP up, HDI flat, residual collapsing. Neither income nor development metrics can see what's falling. The country-scale work in this book does not name what does.
- *Text-level (Chapters 7–9).* Cross-era embedding work produced one positive finding (Reddit r/Meditation ↔ William James 1890 phenomenology of introspection at cosines 0.58–0.61, four of five top pairs hitting James paragraph #810) plus two clean falsifications (the structural position-twelve cluster filed as selection bias; the wholeness-register interpretation falsified by Reddit's negative paired-difference).

**The two halves do not connect statistically.** The connecting word "residual" is metaphorical across them. Chapter 10 names this as the project's central methodological lesson; the bridge-grep habit (discipline rule 13) was added to standing process to prevent recurrence.

**Last session committed:** [Session 14](sessions/session_14.md) — local LLM stack stood up on the user's Mac (LM Studio + Qwen 2.5 14B + Jupyter); AG News 50-article validation at 92% accuracy as a tutorial-grade sanity check; project's analytical toolkit now has two primitives — embeddings (Sessions 7–9, runs on Colab+T4) and LLM-classification-via-prompt (Session 14, runs on user's Mac).

**Next session:** When the user is ready, the next investigation question gets picked — fresh sub-question pick, Sessions-4-onward style. Discipline rules 1–4 (unit-of-analysis, statistical-bridge-up-front, exploratory-vs-confirmatory marking, pre-registration) apply from session zero. The new investigation will produce its own plan file when the question is named. Either or both analytical primitives are available; which one fits depends on the question.

### Hypotheses status (Wholeness Investigation, closed at Session 9)

From [`research_plan_wholeness.md`](research_plan_wholeness.md), with Session 11's dated status notes folded in:

| | Hypothesis | Final status |
|---|---|---|
| **H1** | Growth and development have decoupled | Partial. r = 0.32 globally between GDP-factor change and HDI change; not a global decoupling. 38 of 129 countries fit the strict "GDP up, HDI flat" pattern. |
| **H2** | Connection predicts wellbeing better than wealth | Inconclusive. Social support r = 0.812 vs GDP r = 0.799 in 2025 cross-section; 0.013 gap is at noise level. |
| **H3** | The language of wholeness is rising in modern writing | Drifted from original wording. Sessions 7–9 tested cross-era resonance and per-corpus paired-differences, not temporal rise in modern writing. The Session-7 1890↔2026 finding survived; Session-9 Reddit↔James phenomenology survived; the wholeness-register interpretation of the Session-8 cross-era lift was falsified. |
| **H4** | Cultures vary systematically in wholeness vs machine language | Not started. The original plan deferred this to Phase 4; the Wholeness Investigation closed before Phase 4 ran. |

---

## Workflow shift, April 2026

Earlier sessions delivered work as zip bundles from a separate planning chat (with a `CLAUDE_CODE_INSTRUCTIONS.md` brief at the top). **From now on, development happens directly in Claude Code.** Zip bundles are deprecated.

What changes in practice:
- Each session is run inside Claude Code from start to finish.
- The user sets the goal, you do the work, you write the receipts as you go.
- The end-of-session ritual in `01_working_agreement.md` still applies — write `session_NN.md` with raw outputs, update the chapter if there's one, save images to `book/images/`, update `00_index.md`, append any new glossary terms, commit + push.
- **Do NOT create `start_session_NN.md`** files for future sessions. Those (when they exist) are drafted in a separate session-planning conversation with the user, not by Claude Code.

---

## Mechanical conventions

### Commit messages

Multi-paragraph. One-line title that captures the change. Then 1–3 paragraphs of context (what + why). Then a bulleted what-changed list. End with the Co-Authored-By line.

Pass via HEREDOC for clean formatting:

```bash
git commit -m "$(cat <<'EOF'
Title line — one line, no period

One paragraph of context: what was the situation, what shifted,
why this commit exists. Two or three sentences.

- Concrete change one
- Concrete change two
- Concrete change three

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

### Gitignore force-add pattern

`data/raw/*` and `data/processed/*.csv` are gitignored, but specific files are tracked anyway by force-adding. This keeps the casual mess out while letting deliberate parked sources and processed datasets live in the repo.

Currently force-tracked:
```
data/raw/hamming_lecture_01_1995.txt
data/raw/ackoff_lecture_systems_age.txt
data/raw/thinking_in_wholes_2026.md
data/raw/WHR26_Data_Figure_2.1.xlsx
data/raw/HDR25_Composite_indices_complete_time_series.csv
data/raw/james_principles_psychology_1890.txt
data/raw/deepseek_local_llm_guide_2026_05_11.html
data/raw/deepseek_local_llm_guide_2026_05_11.md
data/processed/whr2025_clean.csv
data/processed/whr_changes_2019_2025.csv
data/processed/session_05_merged.csv
```

To add a new tracked data file: `git add -f data/raw/whatever.csv`. The book *Thinking in Wholes* lives in the repo as `.md` not `.docx` (renders directly on GitHub).

### Pushing big files

If a `git push` 400s out (`HTTP 400` / `unexpected disconnect while reading sideband packet`), the cause is usually a single large file (>1 MB) hitting the default HTTP buffer. Fix:

```bash
git -c http.postBuffer=524288000 push origin main
```

This came up with the 2 MB HDI source CSV.

### File conventions

| File | Convention |
|---|---|
| `sessions/session_NN.md` | Header `# Session NN — Record`. Sections in order: Goal · What actually happened · The data · Findings · What this means for the investigation · Caveats · Status at end of session · Raw outputs (receipts). Receipts at the bottom = raw correlations, means, code blocks for future verification. Don't bury process failures — see the "A note on the charts" section in `sessions/session_05.md` as the precedent. |
| `book/chapter_NN.md` | Header `# Chapter NN — Title`. **No scaffolding lines** ("(Draft — edit freely)", "(End of Chapter NN)" closers — those have all been removed). Sustained prose preferred over bullets in mature chapters (Ch 3+). Every `![alt](images/file.png)` must point to a real file. Numbers must reproduce from data files in the repo. |
| `book/images/chapter_NN_*.png` | Image filenames carry the chapter number. Charts referenced from chapter prose go here. |
| `00_index.md` | Every new file added to the repo = one new line here. Session bullets get a one-line summary of the *finding*, not just the title. The hook paragraph at top gets refreshed when the working frame shifts. |
| `05_glossary.md` | Sessions 1–3 entries are in chronological/topical order — preserve. Sessions 4+ form an alphabetical block immediately before the closing "## The mental division for this project" section. Each entry: `## Term`, paragraph, "First used in [session_NN.md](sessions/session_NN.md)" link. |

---

## Verification habits ("don't trust")

*The full numbered version of these lives in [`discipline.md`](discipline.md) §2 (rules 8–14). The summary below is the operational reminder; for drift response and override syntax see `discipline.md` §4.*

The user's standing instruction is **"verify, don't trust."** Apply this whenever you're about to commit a non-trivial finding, or when asked to "double check":

1. **Reproduce the headline numbers from the actual data files.** Write quick Python (`python3 <<EOF` inline or a `/tmp/verify.py`) to recompute the correlation, the country count, the filter outcome. Don't take prose at its word.
2. **Cross-check files for internal consistency.** Same number quoted across session record, chapter, index, commit message? When a brief claims "no change" to a file, did it actually change?
3. **Open chart images visually with the `Read` tool.** Verify no PDF artefacts, no UI chrome, no watermarks, and that the values shown in the chart match the prose claims about them.
4. **Verify cross-references.** Every glossary anchor referenced from a chapter (e.g. `#prompt-engineering-small-form`) must resolve to a real heading. Every `![](images/file.png)` must point to a file that exists.
5. **If anything fails: stop, report, ask before committing.** Don't push to fix it later — fix it before the commit lands.
6. **Citation grep before commit.** Whenever a chapter contains a phrase of the form *"the book says…"*, *"the book argues…"*, *"the book calls this…"*, or any direct quote attributed to *Thinking in Wholes*, grep it against `data/raw/thinking_in_wholes_2026.md` first. If the exact phrase isn't in the book, either pull a real quote from the book or rephrase the sentence in the chapter author's own voice. Putting words in the book's mouth that the book did not say is the cleanest possible self-betrayal of a project whose central claim is *trace everything back.*
7. **Note model identity in session receipts.** Every session record names which model class drafted the prose and which verified it. This is part of the receipts, not a footnote.

The Session 5 chart-fix episode (commits `68230bf` → `70d49f2` → addendum in `sessions/session_05.md`) is the cautionary precedent for visual verification. The Session 6 audit (commits `1483826` and `sessions/session_06.md`) is the cautionary precedent for citation verification — a fabricated *"measurement trap"* attribution to the book that grep would have caught in two seconds. Both are logged as process failures so they don't recur.

## Model use — the asymmetric-pair pattern

*Discipline rule 15. Full table of which class to use for which job lives in [`discipline.md`](discipline.md) §3.*

Where it can be arranged, prose drafted by a smaller model gets read by a larger one before commit. Smaller models (Sonnet class) are well-suited to code generation, structured analysis, and routine pipeline work. Larger models (Opus class) are better-suited to careful citation, long-document recall, and voice consistency in a sustained book. Use both deliberately, not interchangeably.

The Session 6 audit was an instance of this pattern: Sonnet 4.6 drafted Chapter 6 in earlier sessions; Opus 4.7 caught the four issues in Claude Code on April 28. The published evidence on this is consistent (HalluLens, Vectara hallucination leaderboard, Frontiers in AI 2025 survey): hallucination rates fall as model parameters and training compute rise, and citation fabrication is one of the failure modes most sensitive to model size. See `sessions/session_06.md` for the full reasoning and sources.

---

## When uncertain

If the right call depends on the user's voice or scope decision, ask one concise question rather than guessing.

If it's a mechanics question (where to put a file, what to name a column, how to phrase a commit message), make a defensible call and note it in the session record.

The user values directness and dislikes over-questioning.

---

*Keep this file current. When a convention changes, update it here so the next session inherits the change.*
