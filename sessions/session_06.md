# Session 6 — Record

*A process audit, not a finding session. No new data was loaded. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

After Sessions 4 and 5 closed cleanly, two things felt off about the work that produced Chapter 6 and the chart-fix commits. First: the chart placements in Chapter 6 broke the book's setup → image → walkthrough rhythm in three places. Second: a phrase ("measurement trap — the tendency to mistake the map for the territory") was attributed in the chapter to *Thinking in Wholes*, but the phrase doesn't appear in the book. Both came out of conversations that used Claude Sonnet 4.6 — a smaller, faster sibling of the Opus model the project usually relies on for careful prose.

The session opens by asking three questions:

1. What exactly did the smaller model get wrong, and why?
2. Is it true that AI models "get worse over time" the way users sometimes claim, or are we projecting onto a more specific phenomenon?
3. What goes into the standing process so this doesn't happen again?

This is a process record. The Wholeness Investigation does not advance this session.

## What was wrong, specifically

Four issues in Chapter 6, all caught and fixed in commit `1483826`:

**Three image placements off the chapter's own convention.** Earlier chapters (3, 4, 5) follow a clean rhythm — a sentence or two of setup, then the image, then a walkthrough. Chapter 6 broke that three times.

- The labelled residual-vs-HDI scatter (image 3) was placed after a paragraph about "the residual collapsed in all 38 countries" but the chart actually visualises the r=0.11 finding from the next paragraph. The image was attached to the wrong claim.
- The HDI-groups boxplot (image 4) appeared before the line that introduced what a boxplot of HDI-change groups was. Image first, explanation second.
- The H1 health scatter (image 5) was sandwiched between two paragraphs making the same point. *"But health alone doesn't close the gap. No single factor does."* (before the image) and *"The post-2019 wellbeing decline is multi-causal."* (after the image) say the same thing in different words.

None of these were factually wrong. They were narrative-flow wrong.

**One fabricated citation.** The chapter's closing paragraph attributed a phrase directly to the book:

> *"The book Thinking in Wholes calls this kind of failure a measurement trap — the tendency to mistake the map for the territory, to believe that what we can count is what exists."*

Verified by grep: neither *"measurement trap"* nor *"mistake the map for the territory"* appears anywhere in `data/raw/thinking_in_wholes_2026.md`. The book makes a related point in its chapter 7 — *"They measure what machines measure — output, efficiency, profit. They ignore what social systems require — trust, purpose, the quality of the relationships between people"* — but that is not the phrase that landed in the chapter. The chapter put a different sentence in the book's mouth.

This is the kind of mistake that breaks the project's central promise. The whole point of citing the book at all is that the data and the book are being held to each other. A fabricated citation is a small lie that corrodes the trust the rest of the chapter depends on.

The fix was small. Three image moves, one rewritten sentence, one citation replaced with verbatim language from the book. Nine lines of diff. But the easy fix is not the interesting part. The interesting part is **why this kind of mistake happens with smaller models on this kind of task** and **whether the wider claim that AI models degrade over time is real.**

## Why a smaller model gets citations wrong on a long source

The local failure is well-documented and not mysterious. Larger transformer language models are systematically more reliable than smaller ones at **factual recall against a long source document.** This is published in multiple places. The Vectara hallucination leaderboard tracks fabrication rates across frontier models on summarisation; HalluLens (ACL 2025) benchmarks the same shape; the Frontiers in AI hallucination survey (2025) puts hallucination rates across modern frontier models in a 15–52% band depending on the task, with citation fabrication climbing to 94% in adversarial prompting. Across all of these the pattern is the same: hallucination falls as model parameters and training compute rise, and citation fabrication is one of the failure modes most sensitive to model size.

Sonnet 4.6 is not a degraded Opus. It is a smaller architecture deliberately tuned for speed and cost. Asked to write a chapter that quotes a 372-line book, the model's job is, at one level, search-then-quote. A smaller model — like a person under time pressure who hasn't quite read the book carefully — produces a *plausible-sounding* phrase rather than the actual one. *"Measurement trap"* sounds like the kind of phrase a book on systems thinking would use. It just isn't one this book uses. The model was generating the *texture* of the source rather than retrieving the source.

This is exactly the failure mode the published evidence predicts when smaller models are put on long-document citation tasks.

## Is it true that models "get worse over time"?

Two things are true at the same time.

**The empirical record on weight-level model regression is mixed but real.** The canonical academic study is Chen, Zaharia, and Zou (2023), *"How is ChatGPT's behavior changing over time?"* — Stanford and UC Berkeley. They evaluated GPT-3.5 and GPT-4 on seven tasks across two timepoints (March and June 2023). On prime-number identification, GPT-4 dropped from **84% accuracy in March to 51% in June** — a 33-percentage-point fall on the same questions. On other tasks the same model improved. The behaviour is real, measurable, and direction-mixed. Models do drift between releases.

**The system around the model can shift even when the model doesn't.** What a user touches through a product is the *system* — model + system prompt + safety filters + routing + caching + throttling + context handling. Any of those can change without the model itself changing. The clearest recent example for this project is Anthropic's own postmortem published April 23, 2026, six days before this session.

Anthropic identified three distinct issues affecting Claude Code in March and April 2026. None of them affected the API directly; all three affected Claude Code specifically — the same product the Sonnet 4.6 work in this project ran through:

| | Bug | Window | What it did |
|---|---|---|---|
| 1 | Reasoning-effort default lowered from `high` to `medium` for latency | March 4 – April 7 | Users reported Claude felt "less intelligent" |
| 2 | Prompt caching bug cleared thinking history every turn instead of once | March 26 – April 10 | Forgetfulness, repetitive answers, faster quota drain |
| 3 | System prompt added a 25-word limit on text between tool calls | April 16 – April 20 | Coding quality measured 3% lower on internal evals |

All three resolved by April 20, 2026. The Session 5 work in this repo committed on April 27, after all three fixes. So the chapter-6 errors caught in this audit are **not** directly attributable to those bugs.

But the three bugs do illustrate the wider point. The chapter-6 errors are explained by *the smaller model on a long-citation task* — the model-size effect that the size-scaling literature predicts. The Anthropic episode is a different effect: the *non-model parts of the system* changing without the model itself changing. Both produce the user-visible experience "the AI got worse." They have different mechanisms.

The honest answer to *"do models get worse over time?"* is therefore: model weights, once shipped under a name and version, are stable; what users experience is not just the weights; system-level changes can and do measurably degrade product behaviour without anyone meaning to; and the size of the model serving any given request matters a great deal. Users who want stable behaviour need to track the system, not the brand.

A separate version of the question — "do companies *deliberately* lower model capability after users are locked in?" — is harder to substantiate from the published evidence. What is documented: companies ship cheaper, smaller sibling models alongside flagships; default routing under load can silently degrade what a free or cheap tier user experiences; specific bugs and changes can degrade behaviour for weeks before being caught. What is not well documented from public sources: deliberate post-hoc weight-level downgrades by major frontier vendors. The honest framing is that the *commercial incentives push toward silent system-level changes that look like degradation*, even when no individual decision was "let's make the product worse."

## What gets added to the standing process

Three changes, going into `CLAUDE.md` so the next session inherits them.

**1. Citation grep before commit.** Any phrase in any chapter that follows the form *"the book says…"* or *"the book argues…"* or *"the book calls this…"* gets grepped against `data/raw/thinking_in_wholes_2026.md` before it leaves the working tree. If the exact phrase is not in the book, either pull a real quote from the book or rephrase the sentence in the chapter author's own voice. Putting words in the book's mouth that the book did not say is the cleanest possible self-betrayal of a project whose central claim is *trace everything back.*

**2. Model identity in session receipts.** Every session record now names which model class drafted the prose and which verified it. This becomes part of the receipts, not a footnote.

**3. The asymmetric-pair pattern.** Where it can be arranged, prose drafted by a smaller model gets read by a larger one before commit. Smaller models are well-suited to code generation, structured analysis, and routine pipeline work. Larger models are better-suited to careful citation, long-document recall, and voice consistency in a sustained book. Use both deliberately, not interchangeably.

## Caveats

1. The *size-causes-citation-failure* framing in this record is broadly supported by the published literature but not absolute. Larger models also fabricate, just less. The verification habit is the actual fix; "use a bigger model" is not enough on its own.
2. The *"models get worse over time"* framing is more contested than this record might suggest. The fairer reading: published benchmark numbers for a fixed model name and version are stable; the experience users get from a product is not just the model and can drift; the gap between those facts is where the controversy and most of the user complaints live.
3. The label "lower model" is doing a lot of work. Sonnet 4.6 is not a degraded Opus 4.7. It is a different size class with different strengths. Calling it "lower" is colloquial; calling it "smaller" is more accurate and lines up with the literature.
4. This session has a sample size of one chapter. Generalising from one chapter's mistakes to "smaller models can't write careful prose" would over-claim. What this session does is set up the verification habit so that future sample-of-one events get caught earlier.

## Status at end of session

No new images. No new processed data. No new chapter. Three updates to existing files:

- `book/chapter_06.md` — already fixed in commit [`1483826`](https://github.com/zzeeshann/data-science-journey/commit/1483826) (preceding this record).
- `CLAUDE.md` — updated with the three verification habits and updated current-state pointers.
- `00_index.md` — updated to add session_06 and refresh the "what we did last" pointer.

Six sessions, six chapters. The book is current. The Wholeness Investigation resumes in Session 7, which still does what Session 6 was originally planned to do — embeddings and language. Session 7 loads `thinking_in_wholes_2026.md`, the Ackoff lecture, the William James 1890 text, and at least one Reddit corpus, embeds all four with a Hugging Face model, and asks whether the language of wholeness vs fragmentation is shifting in the years the WHR data says something changed.

---

## Raw outputs (receipts)

### Models in this session

- **Drafted Chapter 6 prose:** Claude Sonnet 4.6 (in earlier conversations on April 27, 2026)
- **Audited and corrected Chapter 6:** Claude Opus 4.7, in Claude Code (this session, April 28, 2026)
- **This session record:** Claude Opus 4.7

### Issues caught in chapter 6 (commit 1483826)

```
1. Image 3 (residual_hdi_labelled) — placed BEFORE the prose
   it illustrated. Moved one paragraph later, with a one-line
   walkthrough sentence added.
2. Image 4 (hdi_groups_boxplot) — placed BEFORE its setup
   line. Setup line moved to before the image.
3. Image 5 (h1_health_scatter) — bracketed by two paragraphs
   making the same point. The pre-image redundancy moved to
   become the post-image walkthrough.
4. Book misattribution — phrase 'measurement trap' attributed
   to the book. Verified by grep that the phrase does not
   appear in data/raw/thinking_in_wholes_2026.md. Replaced
   with verbatim language from the book's chapter 7.
```

### Verification command that caught the misattribution

```bash
grep -i "measurement trap\|map for the territory" \
  data/raw/thinking_in_wholes_2026.md
# (no output)
```

That command, run before any chapter ships, is now part of the standing process.

### Anthropic Claude Code issues (March–April 2026), per the April 23 postmortem

```
Issue 1: Reasoning-effort default lowered from 'high' to 'medium'
         March 4 – April 7, 2026
         Affected: Claude Code (Sonnet 4.6, Opus 4.6)

Issue 2: Prompt caching bug — thinking history cleared every turn
         instead of once
         March 26 – April 10, 2026
         Affected: Claude Code (Sonnet 4.6, Opus 4.6)

Issue 3: System prompt 25-word verbosity limit (3% coding-quality drop
         on internal evals)
         April 16 – April 20, 2026
         Affected: Claude Code (Sonnet 4.6, Opus 4.6, Opus 4.7)

API: Unaffected by all three.
All three resolved by April 20, 2026.
This project's Session 5 commits landed April 27, after all fixes.
```

## Sources

- [How is ChatGPT's behavior changing over time?](https://arxiv.org/abs/2307.09009) — Chen, Zaharia, Zou, 2023 (the canonical academic study on between-release model drift; GPT-4 prime-number accuracy fell 84% → 51% over three months on the same questions)
- [An update on recent Claude Code quality reports](https://www.anthropic.com/engineering/april-23-postmortem) — Anthropic engineering, April 23, 2026 (the three Claude Code regressions detailed above)
- [Vectara hallucination leaderboard](https://github.com/vectara/hallucination-leaderboard) — public benchmark of LLM hallucination rates on summarisation
- [HalluLens: LLM Hallucination Benchmark](https://aclanthology.org/2025.acl-long.1176.pdf) — ACL 2025
- [Survey and analysis of hallucinations in large language models](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full) — Frontiers in AI, 2025 (15–52% hallucination band; 94% citation fabrication in adversarial conditions)
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://research.trychroma.com/context-rot) — Chroma research (long-context degradation patterns)
