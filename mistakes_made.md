# Mistakes Made

*The project's mistakes-and-corrections record. Six entries, in the order they were caught. For each: what happened, where, how it was caught, what verification habit fixed it, what habit was added to standing process to prevent recurrence.*

*This file exists because the central claim of the investigation — trace everything back to its source — applies most strongly to the project's own work. Catching mistakes in writing, naming them, and folding the catch into the next session's discipline is what makes the rest of the work credible.*

---

## 1. Session 5 — chart artefacts in the first published chart

**What happened.** Session 5 produced six charts in [Julius AI](https://julius.ai), exported them as PDF, and screenshotted into PNG to embed into Chapter 6. The screenshotting introduced visible UI chrome (Julius watermarks, page edges) and one chart had its axis label cut off. The artefacts shipped in commit `68230bf` ("Session 5: H1 test").

**How it was caught.** The user opened the chart files visually after the commit landed and saw the artefacts.

**The fix.** Re-exported the six charts as clean PNGs directly from Julius and replaced the originals in commit `70d49f2` ("Fix Session 5 charts: replace PDF crops with clean Julius exports"). An addendum was added to [`sessions/session_05.md`](sessions/session_05.md) recording the failure rather than burying it.

**Habit added to standing process.** *Open chart images visually with the Read tool before commit.* Verifying that no PDF artefacts, no UI chrome, no watermarks shipped, and that the values shown match the prose claims about them. Listed in [`CLAUDE.md`](CLAUDE.md) as one of the verify-don't-trust habits.

---

## 2. Session 6 — fabricated quote attributed to *Thinking in Wholes*

**What happened.** Chapter 6 (drafted in an earlier session by Sonnet 4.6) contained the phrase *"the measurement trap — the tendency to mistake the map for the territory,"* attributed to *Thinking in Wholes*. The phrase does not appear in the source book. A 2-second `grep` against [`data/raw/thinking_in_wholes_2026.md`](data/raw/thinking_in_wholes_2026.md) would have returned no hits. It was carried into the committed chapter as if it were a real attribution.

**How it was caught.** Session 6 was a deliberate process audit run by Opus 4.7 in Claude Code. Reading Chapter 6 cold, the auditor flagged the phrase as not feeling like book voice and ran the `grep`. No hit. The misattribution was confirmed and fixed in commit `1483826` ("Chapter 6: fix image placement and book misattribution").

**The fix.** Removed the fabricated phrase from Chapter 6. Added the citation-grep step to standing verification process. Documented the model-class asymmetry in [`sessions/session_06.md`](sessions/session_06.md): smaller models (Sonnet class) draft cleanly but hallucinate citation language at a rate larger models do not, and the cross-check is now structural rather than ad-hoc.

**Habit added to standing process.** *Citation grep before commit.* Whenever a chapter contains a phrase of the form *"the book says…"*, *"the book argues…"*, *"the book calls this…"*, or any direct quote attributed to *Thinking in Wholes*, grep it against the source book first. If the exact phrase isn't there, either pull a real quote or rephrase in the chapter author's own voice. Listed in [`CLAUDE.md`](CLAUDE.md). The same habit caught both the chapter 5 and chapter 6 paraphrases on the Session 12 audit pass — both verified honest.

---

## 3. Session 8 — catalogue-vs-position discovery

**What happened.** The Session 8 plan, drafted before the session ran, treated "position twelve" as a comparable structural unit across seven ancient texts: Hammurabi Law 12, Enuma Elish line 12, I Ching hexagram 12, Inanna's Descent passage 12, Pyramid Texts Spell 12, Gilgamesh Tablet 12, Ugaritic KTU 1.12. The hypothesis assumed all seven were the same kind of thing (the twelfth section of a numbered work) and that asking whether they cluster in embedding space was a coherent question.

Three of the seven turned out not to be that kind of thing. KTU 1.12 is the twelfth tablet in the Dietrich/Loretz/Sanmartín *museum catalogue index* — the digit twelve is an archive number, not a position. Faulkner's Pyramid Texts Spell 12 is a twentieth-century scholarly numbering of a spell that isn't carved at any structural position twelve in the original Unas pyramid. Gilgamesh Tablet 12 is an appended Sumerian source distinct from the eleven-tablet Standard Babylonian work — adding it to the cluster is asking whether an appendix shares a property with the main text that gave it the appendix.

**How it was caught.** Verification reading between Sessions 7 and 8, using [`ANCIENT_TEXTS_READING_GUIDE.md`](ANCIENT_TEXTS_READING_GUIDE.md), surfaced the discrepancy on each text individually. The user did the reading; the methodological problem became visible by going back to the primary sources rather than trusting the catalogue numbers in modern indices.

**The fix.** The hypothesis was narrowed honestly. The four texts that *do* have a comparable position-twelve unit (Hammurabi, Enuma Elish Tablet 1, I Ching, Inanna) became the position-twelve set. The other three were folded into the analysis as a *wider sample of ancient prose*, not part of the cluster claim. The session ran on fifteen verified passages instead of the planned seven, with the discrepancy named openly in both [`sessions/session_08.md`](sessions/session_08.md) and Chapter 8 itself.

**Habit added to standing process.** *Verify what kind of unit a numbering scheme refers to before treating cross-source comparisons as meaningful.* A digit isn't a structural position. Catalogue indices, scholarly numberings, and authored sequences are different things even when they share a number. Listed implicitly in the [`ancient_voices/passages/README.md`](ancient_voices/passages/README.md) format spec, which now requires the citation header to disambiguate.

---

## 4. Session 9 — pre-registered prediction the data rejected

**What happened.** Session 9 ran with a pre-registered interpretation of Session 8's small cross-era lift toward position-twelve ancient passages: that the lift was a *wholeness-register* signal — modern wholeness language reaching across eras for the same intellectual move the oldest texts already had. The prediction was that Reddit, the modern lay-meditation voice, would also show the lift if the wholeness-register reading was correct.

The data rejected the prediction cleanly. Reddit's paired-difference toward position-twelve came in at −0.0045 (negative; 42 per cent positive) while the three formal-prose corpora sat in the +0.012 to +0.018 band. The wholeness-register interpretation is falsified. What the cross-era lift actually shows is a formal-English-prose register effect, not a transmission of wholeness language.

**How it was caught.** This is not a mistake in the same sense as the previous three. The prediction was written down before Session 9 ran. The data was generated. The result rejected the prediction. The discipline did exactly what it was supposed to do.

**The fix.** Filed the wholeness-register interpretation as not-the-answer in [`sessions/session_09.md`](sessions/session_09.md) and Chapter 9. The filed-as-rejected interpretation is a real output of the project; it narrows what the cross-era lift can mean.

**Habit added to standing process.** *Pre-registration discipline.* Write the prediction down before the data exists. Accept whatever the test produces. Don't rephrase the hypothesis after the fact to fit the result. Listed in the [`05_glossary.md#falsification`](05_glossary.md#falsification) entry, which Session 8 first introduced and Session 9 stress-tested.

---

## 5. Session 10 — the unit-of-analysis bridge problem

**What happened.** This is the largest mistake the project surfaced and the reason Chapter 10 exists.

The Wholeness Investigation was framed across nine sessions as one continuous question: *what is in the residual the WHR cannot see across 141 countries between 2019 and 2025?* Sessions 4–6 measured residuals at the country-year unit and produced the first finding. Sessions 7–9 measured cosines at the paragraph-pair unit and produced a different set of results. The chapters' framing connected them as if the second half was answering the question the first half opened — Chapter 5 said *"the rest of this investigation is going to try to name"* the residual; Chapter 7 called the cross-era pair finding *"the first piece of language-level evidence the investigation has produced"* toward that question; Chapter 9 said *"two candidate names have been filed"* and *"two sessions remain to surface a third."*

There was no statistical bridge between the two halves. The country-scale work had no text features. The text-level work had no countries. The connecting word *"residual"* was being used metaphorically, not as a shared variable. The chapters' framing claimed an empirical link the project had not built.

**How it was caught.** The user asked, mid-conversation, *"are we even doing correct investigation? are we even doing something?"* That question triggered Session 10 — a project-level audit that read all nine session records and nine chapters cold and compared chapter framing against session evidence. The audit was written up in [`project_state.md`](project_state.md) and surfaced five options for what to do next. Decision: Option C (honest close).

**The fix.** Session 11 wrote [`book/chapter_10.md`](book/chapter_10.md) — the lessons-learned chapter — and applied six surgical patches to the rhetorical-bridge sentences across Chapters 5, 6, 7, 9, and the index hook paragraph. The numbers stayed; the framing claims were removed or replaced with unit-honest versions. [`research_plan_wholeness.md`](research_plan_wholeness.md) got dated status notes on each of the four hypotheses reflecting what the evidence actually showed vs. the original wording.

**Habit added to standing process.** *Bridge grep before commit.* Any sentence in a chapter that links two findings should have a corresponding session record entry showing the statistical link. If no such entry exists, either build the link or remove the claim. Documented in Chapter 10. The discipline is the same shape as Session 6's citation grep: read your own writing and ask whether the data supports it.

The deeper habit, also from Chapter 10: *write the unit of analysis at the top of every session brief, in one sentence, before any code runs.* If a session would need to bridge two units, the bridge is a separate piece of the brief — built deliberately, not assumed.

---

## 6. Session 11 — preserving original wording in the plan rather than rewriting it

**What happened.** When Session 11 patched [`research_plan_wholeness.md`](research_plan_wholeness.md), there were two options: rewrite the four hypotheses to reflect what was actually tested (cleaner-looking plan), or preserve the original wording and add dated status notes underneath each (visibly drift-aware plan). The first approach would have made the plan look like everything was always known; the second leaves the drift visible.

**How it was caught.** This isn't a mistake — it's a decision the session deliberately recorded as a caveat in [`sessions/session_11.md`](sessions/session_11.md), point 3. Future readers of the plan will see status notes that say things like *"Status (Session 9 result, 2026-04-29): drifted from original wording; tested as cross-era resonance, not temporal rise."* Some readers will wonder why the original wording is preserved at all.

**The reasoning.** The plan is a record of how the project was thought of at Session 3, not a fresh rewrite. Rewriting the plan to look like the work always knew what it was doing erases the actual epistemic motion of the project. The dated status notes are how the plan stays honest without becoming an after-the-fact narrative.

**Habit added to standing process.** *Patch with dated status notes, don't rewrite plan files.* When original wording in a planning document drifts from what was actually tested, append a dated status note rather than editing the original. Same logic as the chapter-patches in Session 11: surgical changes preserve the record of how the work evolved.

---

## What this list demonstrates

Six mistakes, six catches. Three caught by reading prose against source files (Sessions 5, 6, 12-during-the-audit), one caught by reading primary sources against catalogue numbers (Session 8), one caught by writing down a prediction and accepting the rejection (Session 9), one caught by the user asking the right uncomfortable question at the right moment (Session 10).

The discipline that made this list possible is the same discipline the chapters describe: trace everything back. Every commit has a verifiable source. Every claim in a chapter has a session record. Every session record has raw outputs at the bottom. When the discipline catches something — like the bridge problem — the project widens the discipline, names what changed, and folds the new habit into the standing process so the next session inherits it.

This file is one of the most useful things in the repo. It demonstrates the verify-don't-trust process working in practice across a multi-session investigation, and it gives the next investigation a checklist of failure modes to watch for from the start.
