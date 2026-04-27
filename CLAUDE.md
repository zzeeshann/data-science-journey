# CLAUDE.md — Operational brief for Claude Code

If you're a Claude Code agent picking up this repo in a new session, read this file first. It's the operational handoff. The project content and voice rules live elsewhere.

## Reading order at the start of a session

1. **This file** — current state, mechanics, what's next.
2. **[01_working_agreement.md](01_working_agreement.md)** — how we work. Voice, setup, end-of-session ritual. Source of truth on conduct.
3. **[00_index.md](00_index.md)** — the map of every file in the repo.
4. **[research_plan_wholeness.md](research_plan_wholeness.md)** — the active investigation. Four hypotheses, session arc, the "name what is in the residual" hook.
5. **The most recent file in `sessions/`** — what just happened.
6. **[02_project_brief.md](02_project_brief.md)** — what the project is. Multi-year investigative ambition. Read once; do not reintroduce the retracted six-month/job framing.
7. **`data/raw/thinking_in_wholes_2026.md`** — the lens. Hypothesis source, not ground truth.

If a question is about voice, scope, or working style → `01_working_agreement.md`.
If a question is about content or where the project is going → `research_plan_wholeness.md` + the latest session record.
If a question is about mechanics (commits, force-adds, file conventions, verification) → this file.

---

## Where the project is right now

**Phase:** 2 of 5 (country-scale wellbeing/development) is complete. Phase 3 (embeddings) is next.

**Hook the investigation now orbits:** Across 141 countries between 2019 and 2025, measured factors in the World Happiness Report rose in 99% of countries while the unexplained residual fell in 98%. Session 5 ruled out HDI stagnation as the explanation — neither income nor development metrics can see what's falling. The rest of the investigation is trying to name it.

**Last session committed:** Session 6 (a process audit — caught and fixed lower-model errors in the Chapter 6 work, set up new verification habits and the asymmetric-pair pattern). The Wholeness Investigation did not advance this session.

**Next session:** Session 7 — embeddings and language. Per `research_plan_wholeness.md`, this is the project's first real NLP session (it was originally the planned scope for Session 6 before Session 6 became a process audit). Probable scope: load *Thinking in Wholes*, the Ackoff lecture, William James 1890, and a Reddit corpus or two; embed with a Hugging Face model; compare semantic similarity in the language of wholeness vs fragmentation across eras. Final scope is set in the next session-planning conversation.

### Hypotheses status

From `research_plan_wholeness.md`:

| | Hypothesis | Status |
|---|---|---|
| **H1** | Growth and development have decoupled | Tested in Session 5. Filed as partial pattern, not global law. 38 of 129 countries fit (GDP up, HDI flat, residual collapsing). |
| **H2** | Connection predicts wellbeing better than wealth | Surface-tested in Session 4 cross-section. Inconclusive at noise level (0.812 vs 0.799). Needs richer connection measure than WHR's one-question social-support proxy. |
| **H3** | The language of wholeness is rising in modern writing | Not tested. Phase 3 (Sessions 6–7). |
| **H4** | Cultures vary systematically in wholeness vs machine language | Not tested. Phase 4 (Sessions 8–9). |

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

Where it can be arranged, prose drafted by a smaller model gets read by a larger one before commit. Smaller models (Sonnet class) are well-suited to code generation, structured analysis, and routine pipeline work. Larger models (Opus class) are better-suited to careful citation, long-document recall, and voice consistency in a sustained book. Use both deliberately, not interchangeably.

The Session 6 audit was an instance of this pattern: Sonnet 4.6 drafted Chapter 6 in earlier sessions; Opus 4.7 caught the four issues in Claude Code on April 28. The published evidence on this is consistent (HalluLens, Vectara hallucination leaderboard, Frontiers in AI 2025 survey): hallucination rates fall as model parameters and training compute rise, and citation fabrication is one of the failure modes most sensitive to model size. See `sessions/session_06.md` for the full reasoning and sources.

---

## When uncertain

If the right call depends on the user's voice or scope decision, ask one concise question rather than guessing.

If it's a mechanics question (where to put a file, what to name a column, how to phrase a commit message), make a defensible call and note it in the session record.

The user values directness and dislikes over-questioning.

---

*Keep this file current. When a convention changes, update it here so the next session inherits the change.*
