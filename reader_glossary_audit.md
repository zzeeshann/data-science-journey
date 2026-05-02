# Reader Glossary Audit

*Working document, kept current after every readability audit. Lists every glossary entry the audits have added, the chapter that triggered it, and why a standalone definition was needed instead of relying on inline prose.*

*This file is the audit's record of what got added. The entries themselves live in [`05_glossary.md`](05_glossary.md).*

---

## Session 12 — seven new entries

The Session 12 readability audit (the 14-year-old pass) added seven new glossary entries, each because a chapter used the term in a way a beginner reader couldn't resolve from context alone. Inline definitions in chapter prose remained unchanged where they were sufficient; entries were added only where the inline gloss didn't cover what the term actually means or where a chapter introduced the term cold.

### 1. Bootstrap confidence interval (CI)

**Triggered by:** [Chapter 8, line 15](book/chapter_08.md). *"The bootstrap ninety-five-percent confidence interval was [+0.0118, +0.0142], cleanly excluding zero."*

**Why an entry was needed.** The chapter used the term as if the reader knew what it meant. *Confidence interval* on its own might be guessable, but *bootstrap* requires the resampling-with-replacement procedure to make sense, and that procedure isn't visible in the chapter prose. A reader who doesn't know how a bootstrap CI is constructed can't tell why "cleanly excluding zero" matters.

**What the entry does.** Describes the resample-with-replacement procedure in three sentences, names what the 95% range actually contains (the middle 95% of resamples), and uses Session 8's actual numbers as the worked example.

### 2. p-value (statistical significance)

**Triggered by:** [Chapter 6, line 17](book/chapter_06.md) (*"moderate, statistically significant"*) and [Chapter 8, line 11](book/chapter_08.md) (*"with one-sided p of 0.55"*). The first occurrence is in chapter 6, but the term is used multiple times across chapters 6, 8, and 9 with values ranging from p = 0.015 (significant) through p = 0.062 (borderline) to p of 0.55 (not significant).

**Why an entry was needed.** The chapter prose says *"statistically significant"* and *"borderline significant"* and *"p of 0.55"* without ever defining what p actually measures. A reader who doesn't already know the conventional 0.05 cut-off can't interpret any of those phrases.

**What the entry does.** Defines p as the probability under the null, names the conventional 0.05 / 0.10 / 0.01 thresholds, and uses Session 5 and Session 6's actual numbers (p = 0.015 significant; p = 0.062 borderline) as anchored examples.

### 3. Paired-difference test

**Triggered by:** [Chapter 8, line 15](book/chapter_08.md). *"The paired difference between mean cosine to the four position-twelve ancient passages and mean cosine to the eleven non-position-twelve ancient passages came out to +0.0130."*

**Why an entry was needed.** The chapter explains the comparison inline ("between mean cosine to A and mean cosine to B") but never says why *paired* matters or what the per-corpus mean represents. The "paired-positive" percentages later in the same paragraph (75.8%, 79.4%, 69.5%) compound the issue if the reader doesn't know the test gives one signed value per chunk.

**What the entry does.** Explains the per-chunk procedure (each chunk acts as its own control), names why the *paired* word matters (per-chunk noise cancels), references the bootstrap CI and sign-flip permutation as the reliability checks, and uses Session 8's per-corpus numbers plus Session 9's negative Reddit value as worked examples.

### 4. Register (linguistic)

**Triggered by:** [Chapter 8, line 17](book/chapter_08.md) (*"the same prose register"*) and [Chapter 9, line 15](book/chapter_09.md) (*"formal-English-prose register"*). The term is also used in the broader phrase *"wholeness register"* and *"translation register"* across both chapters.

**Why an entry was needed.** *Register* in this linguistic-stylistic sense isn't the everyday meaning of the word, and the chapters use it as if it were a known technical term. A reader carries everyday register meanings (musical register, cash register) and may miss the specific stylistic-context sense the chapters intend. The wholeness-register-vs-translation-register distinction in Chapter 9 is the load-bearing concept of the entire Session 9 falsification, and that distinction depends on the reader carrying the right meaning.

**What the entry does.** Defines register as the style-of-writing-or-speech sense, contrasts a few examples (Victorian Bible translation vs. 2020s Reddit post), explains why embedding models can produce register matches that look like content matches, and uses Session 9's negative Reddit paired-difference as the worked example.

### 5. Sign-flip permutation

**Triggered by:** [Chapter 8, line 15](book/chapter_08.md). *"The sign-flip permutation p was effectively zero."*

**Why an entry was needed.** *Permutation test* already had a glossary entry (Session 8 introduced it), but *sign-flip* permutation is a specific variant — the version used for paired-difference reliability — and the standard permutation entry doesn't describe it. A reader who clicked through to *permutation test* would find a description of the position-twelve cluster test (sample-and-shuffle), not the per-chunk-sign-flip procedure used here.

**What the entry does.** Describes the per-chunk-sign-flip procedure specifically (flip each chunk's signed paired-difference at random), names the null hypothesis it tests (differences are exchangeable, mean is zero), explains why the resulting p collapses to effectively zero when the observed mean is far from zero, and uses Session 8's three-corpora p = 0.0000 result as the worked example.

### 6. Subreddit & Pushshift

**Triggered by:** [Chapter 9, line 3](book/chapter_09.md). *"`sentence-transformers/reddit-title-body`, seven million Pushshift-sourced Reddit posts spanning mid-2010 to mid-2021, pre-filtered for quality… filtering the records to subreddit equals 'Meditation'."*

**Why an entry was needed.** *Subreddit* might be familiar to a reader who uses Reddit but isn't if the reader doesn't. *Pushshift* is a research-data term most readers won't have encountered; it explains why a 2010–2021 dataset exists at all and why the project couldn't fetch fresh data. Both terms appear in the same paragraph, so one combined entry kept the alphabetical block uncluttered.

**What the entry does.** Defines both terms in one entry, explains the 2023 Reddit API change that ended Pushshift's public service and why the Hugging Face mirror is the canonical research source now, and uses Session 9's actual fetch (76 r/Meditation posts after a 500k-row stream-scan) as the worked example.

### 7. Vector / vector space

**Triggered by:** [Chapter 7, line 5](book/chapter_07.md) (*"a vector — that a neural network produces from a piece of text"*) and [Chapter 7, line 7](book/chapter_07.md) (*"the vector space doesn't really use the negative half"*). The terms also appear in chapters 8, 9, and 10.

**Why an entry was needed.** *Vector* is defined inline at chapter 7, line 5 as "a list of numbers" — that's enough for a literal definition. *Vector space*, however, is used several times without ever being explained as a geometric world; the reader is left carrying "a list of numbers" through phrases like "embedded into the same vector space" and "live in its own neighbourhood of the geometry." A standalone entry was needed to make the geometric framing legible.

**What the entry does.** Defines vector as a list of numbers (echoing chapter 7's inline definition), then defines vector space as the geometric world those lists live in, and links the geometric framing to cosine similarity. Names the high-dimensional version (384 numbers per chunk for `all-MiniLM-L6-v2`) and acknowledges that humans can't picture 384 dimensions but the metaphor still carries the maths.

---

## What this audit chose not to add

A few terms were considered and left as inline-only because the chapter prose defined them well enough on first use:

- **Embedding** — chapter 7, line 5 already had a glossary entry; the audit just added the cross-link.
- **Cosine similarity** — chapter 7, line 7 already had a glossary entry; cross-link added. The chapter's inline scale anchor (*"Two paragraphs of meditation prose come back at 0.7 or 0.8. Two paragraphs that share nothing in common come back at 0.05 or 0.10"*) is the canonical scale reference all later chapters lean on.
- **UMAP** — already had a glossary entry; never explicitly named in chapter prose (only referenced as *"the 2D projection"*), so no cross-link was added.
- **Selection bias** — used in chapter 8 and chapter 10, but the surrounding prose explains the concept inline (Session 8's *"any seven things selected by a rule will look more similar to each other than seven things sampled at random"* is the inline gloss).
- **Streaming** (a dataset) — used in chapter 9 only; one inline parenthetical gloss (*"reading records one at a time from the cloud rather than downloading the full file"*) was enough.

The lean-glossary rule held: only add a standalone entry when the inline definition isn't enough on its own. Seven entries was the right count.

---

## Future audit log

Subsequent audits append below this line. Keep entries in chronological order; don't merge them with Session 12's list above.
