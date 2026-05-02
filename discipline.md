# Discipline — The Rules This Project Follows

*Required reading at the start of every session. Read this immediately after [CLAUDE.md](CLAUDE.md), before anything else.*

*The disciplines below were learned the hard way across thirteen sessions. Each one has a specific catch behind it — see [`mistakes_made.md`](mistakes_made.md) for the lineage. They are not bureaucratic; they are the project's accumulated "do this and the next investigation goes well" knowledge.*

*Drift response: stop and name it, then ask. Spelled out in §4 below.*

---

## §1 — Reading order at the start of every session

Every Claude (or other AI assistant) picking this repo up in a new session reads in this order:

1. [`CLAUDE.md`](CLAUDE.md) — operational brief: current state, mechanics, what's next.
2. **This file** — the disciplines.
3. [`01_working_agreement.md`](01_working_agreement.md) — collaboration norms (voice, tone, end-of-session ritual).
4. [`00_index.md`](00_index.md) — the map of every file.
5. The most recent `sessions/session_NN.md` — what just happened.
6. The current investigation's plan file (currently [`research_plan_wholeness.md`](research_plan_wholeness.md), or whichever plan file the next investigation produces).
7. [`02_project_brief.md`](02_project_brief.md) — what the project is (read once per fresh chat).

If any of files 1–6 is missing, stop and ask before proceeding.

---

## §2 — The disciplines

Twenty-two rules, organised by phase. Numbered for reference (when Claude flags a drift, it cites the rule by number).

### Pre-session (planning)

**1. Write the unit of analysis at the top of every session brief, in one sentence, before any code runs.**
*Example:* *"This session measures one number per country."* Or *"This session measures one number per paragraph pair."* No session starts without this. The single biggest lesson the project produced — see [Chapter 10](book/chapter_10.md). If a session would link two units, see rule 2.

**2. The bridge between two units is a separate piece of the brief — built deliberately, not assumed.**
If a session would connect country-scale data to text-level data (or any two unit types), the brief must specify the dataset and analysis that has both units in it. No session claims a cross-unit finding without a cross-unit dataset. The mistake this catches is the entire reason Chapter 10 exists.

**3. Distinguish exploratory sessions from confirmatory ones in the brief.**
Exploratory: *"What does the data look like?"* No prediction required. Confirmatory: *"Test prediction X."* Prediction must be written before data is generated. Both modes are valid; mark which is which up front. Don't retroactively claim exploration was confirmation.

**4. For confirmatory sessions, write the prediction down before the data is generated.**
The prediction lives in the brief, dated. After the test runs, accept whatever the data produces. Don't rephrase the hypothesis to fit the result. See [`05_glossary.md#falsification`](05_glossary.md#falsification).

### During session (methodological)

**5. Verify catalogue numbers refer to structural positions before treating cross-source comparisons as meaningful.**
A digit is not a structural position. Catalogue indices, scholarly numberings, and authored sequences are different things even when they share a number. Spend a verification session on primary sources before the analysis session. The Session 8 catalogue-vs-position discovery is the cleanest example.

**6. Plan sample sizes for the comparison being made, not the corpus availability.**
Decide what comparison the session is making, work out the n that comparison needs to be statistically interpretable, and *then* find the corpus. Don't run a 4-vs-11 paired test because that's what fits in the corpus.

**7. Order corpus loading thoughtfully — first-loaded shapes the framing.**
Loading order is a methodological choice, not a logistical accident. If a corpus fails to load, decide whether to defer the session or run it without and report the gap honestly.

### Before commit (verification block — must run every commit)

**8. Reproduce headline numbers from the actual data files.**
Don't take prose at its word. Write quick Python (`python3 <<EOF` inline or a `/tmp/verify.py`) to recompute the correlation, the country count, the filter outcome before commit.

**9. Cross-check files for internal consistency.**
Same number quoted across session record, chapter, index, commit message? When a brief claims "no change" to a file, did it actually change?

**10. Open chart images visually with the Read tool.**
No PDF artefacts, no UI chrome, no watermarks. Values shown in the chart must match the prose claims about them. The Session 5 chart-fix episode (commits `68230bf` → `70d49f2`) is the cautionary precedent.

**11. Verify all cross-references resolve.**
Every `05_glossary.md#anchor` referenced from any chapter must resolve to a real heading. Every `![](images/file.png)` must point to a file that exists.

**12. Citation grep before commit.**
For any phrase like *"the book says…"*, *"the book argues…"*, *"the book calls this…"*, *"the book describes…"*, or any direct quote attributed to *Thinking in Wholes*, run `grep` against [`data/raw/thinking_in_wholes_2026.md`](data/raw/thinking_in_wholes_2026.md) first. If the exact phrase isn't there, either pull a real quote or rephrase in the chapter author's own voice. The Session 6 fabricated quote in Chapter 6 is the cautionary precedent.

**13. Bridge grep before commit.**
For any chapter sentence linking two findings, verify a corresponding session record entry exists showing the statistical link. If no such entry exists, either build the link or remove the claim. The Session 10 unit-of-analysis audit is the cautionary precedent.

**14. Cold-read every chapter touched in this session, once before commit.**
The 14-year-old test: a smart, curious teenager with no statistics or NLP background reading the chapter cold should not get stuck on any sentence. Scale-anchor every dense statistic on first use; glossary-anchor every technical term on first use. The Session 12 readability audit is the precedent.

**15. Use the asymmetric-model-pair pattern.**
Smaller models (Sonnet class): well-suited to code generation, structured analysis, routine pipeline work. Larger models (Opus class): better-suited to careful citation, long-document recall, voice consistency, prose audits. For any prose asserting a specific source quote, run a larger model over it before commit. Hallucination rates fall as model parameters rise; citation fabrication is one of the failure modes most sensitive to model size.

### Plan and hypothesis files

**16. Don't rewrite original wording in plan files. Append dated status notes.**
The plan is a record of how the project was thought of at a specific moment, not a fresh rewrite. When original wording drifts from what was actually tested, append a dated status note (e.g. *"Status (Session 9 result, 2026-04-29): drifted from original wording; tested as cross-era resonance, not temporal rise."*). Same logic as the Session 11 chapter-patches: surgical changes preserve the record of how the work evolved.

### End of session ritual (per [`01_working_agreement.md`](01_working_agreement.md))

**17. Write `sessions/session_NN.md` with raw outputs at the bottom.**
Header `# Session NN — Record`. Sections in order: Goal · What actually happened · The data · Findings · What this means for the investigation · Caveats · Status at end of session · Raw outputs (verification commands, model identity, key code blocks for future verification). Don't bury process failures.

**18. Update or add a book chapter if the session produced something readable.**
One image inline if it's the punchline. Sustained prose preferred over bullets in mature chapters (Chapter 3+). No scaffolding lines (*"(Draft — edit freely)"*, *"(End of Chapter NN)"*).

**19. Update [`00_index.md`](00_index.md).**
Every new file added = one new line. Session bullets get a one-line summary of the *finding*, not just the title.

**20. Update [`05_glossary.md`](05_glossary.md) for new terms.**
Sessions 1–3 entries are chronological/topical and stay put. Sessions 4+ entries form an alphabetical block immediately before the closing "## The mental division for this project" section. Each entry: 3–6 sentences, plus the *"First used in [session_NN.md]"* link.

**21. Note model identity in session receipts.**
Every session record names which model class drafted the prose and which verified it. This is part of the receipts, not a footnote. *"Drafted by Claude Opus 4.7 (1M context) in Claude Code, [date]. Verification by [same / different model]."*

**22. Commit and push.**
Multi-paragraph commit message per [`CLAUDE.md`](CLAUDE.md) HEREDOC pattern. One-line title. One paragraph of context. Bulleted what-changed list. Co-Authored-By line. If a `git push` 400s on a large file, use `git -c http.postBuffer=524288000 push origin main`.

---

## §3 — The asymmetric-model-pair pattern (expanded)

Rule 15 references this; spelling it out because it is a standing recommendation across all sessions, not a single-step check.

| Job | Model class to use | Rationale |
|---|---|---|
| Code generation, embedding pipelines, data wrangling | Sonnet class (4.6 or current equivalent) | Fast, capable on structured tasks, cost-efficient |
| Drafting session records, draft chapters, glossary entries | Sonnet class | Fast, fluent, accurate on structured prose |
| Auditing prose for citation accuracy, bridge claims, voice consistency | Opus class (4.7 or current equivalent, 1M context preferred) | Lower hallucination rate, larger context window, sharper at long-document recall |
| Cold-reading chapters before commit | Opus class | Catches readability gaps and fabricated phrases that smaller models can ship |
| Final commit-message authoring on multi-file changes | Either, but verified by the larger | Ensures the commit narrative matches the actual diff |

The published evidence on this asymmetry is consistent (HalluLens, Vectara hallucination leaderboard, Frontiers in AI 2025 survey, Anthropic April 23 2026 Claude Code postmortem): hallucination rates fall as model parameters and training compute rise, and citation fabrication is one of the failure modes most sensitive to model size. See [`sessions/session_06.md`](sessions/session_06.md) for the full reasoning and sources.

---

## §4 — Drift response

When Claude detects that a discipline is being broken — by user instruction, by Claude's own working momentum, or by anything else — Claude follows this protocol:

1. **Stop.** Do not continue the action that triggers the drift.
2. **Name the drift.** State which rule (by number from §2) is being broken, in one sentence.
3. **Cite the precedent.** Point at the session record or chapter where the rule originates (e.g. *"This is rule 13 — bridge grep — see Session 10 audit."*).
4. **Ask.** Three options for the user: *(a) fix the drift and proceed*, *(b) override the rule explicitly and proceed*, *(c) pause this session and reconsider.*
5. **Wait for an explicit answer.** Don't continue silently.

### What counts as a drift trigger

Concrete examples (not exhaustive):

- A session is starting but no unit of analysis is written down → rule 1.
- A claim is being made that links two units without a statistical bridge → rules 2, 13.
- A chapter sentence asserts *"the book says/argues/calls"* without grep verification against the source → rule 12.
- A commit is being staged without the verification block having run → rules 8–14 collectively.
- A plan file is being rewritten instead of status-noted → rule 16.
- An exploratory session result is being framed as a confirmation → rules 3, 4.
- A cosine, correlation, p-value, or paired-difference lands in a chapter without a scale anchor on first use → rule 14.
- A heavier-model audit is being skipped on a prose claim with a specific source quote → rule 15.
- A session is ending without `session_NN.md`, `00_index.md`, or commit happening → rules 17, 19, 22.

### Override syntax

The user retains final authority. To override a rule explicitly:

- *"Override rule X."* — Suspends rule X for this specific action only. Default re-engages on the next session unless the rule is amended.
- *"Skip the verification block."* — Suspends rules 8–14 for this commit. Use sparingly; the rule exists because the cost of one bad commit exceeds the cost of running the verification block ten times.
- *"This is exploratory, no prediction needed."* — Suspends rule 4 for this session. Marks the session as exploratory in the brief.
- *"Pause this session."* — Stops the work in progress. Claude writes whatever partial session record is appropriate, commits the in-progress state under a `[WIP]` title, and waits.

Override silently — i.e. just continuing past Claude's stop without an explicit answer — is not an option. Claude waits.

### What Claude will not refuse to do

- Skipping a chapter image visual check on a session that produced no charts.
- Citation grep on a session that produced no chapter prose.
- Bridge grep on a session that adds no chapter sentences linking findings.
- Cold-read on a session that touched no chapters.

Rules apply to the work that's actually being done. Skipping a verification step that has nothing to verify is not drift.

---

## §5 — Amending this file

These disciplines are not frozen. They were learned across thirteen sessions and will be refined across future ones.

To amend: any session that produces a new discipline (because a new mistake was caught and a new habit was adopted to prevent recurrence) appends the new rule to §2 in the appropriate phase block, with a one-line note in the session record stating *"Discipline amended: rule N added to discipline.md."* Renumber subsequent rules if needed.

To remove a rule: don't, except in the rare case where two rules have collapsed into one or a rule has been superseded. In that case, leave the original rule's number intact and add a note pointing at its replacement. Like the plan-file status-note discipline (rule 16), the historical record matters.

The Session 13 wrap-up established the initial twenty-two rules. The first amendment will likely come from whichever investigation runs next.

---

*Last updated: Session 13, 2026-05-02. Twenty-two rules, three sections, drift protocol, amendment process.*
