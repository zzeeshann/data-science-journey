# Book Audit — Findings

*Session 12 cold-read of every chapter. The 14-year-old test: would a smart, curious teenager with no statistics or NLP background get stuck on this sentence?*

*Findings only. Patches applied chapter-by-chapter in the same session and recorded against each line. Anything left as **deferred** is named in `sessions/session_12.md` with a reason.*

---

## Chapter 1 — Why I'm Doing This

**Light pass.** The chapter is first-person, plain English, no statistics. It already links to `02_project_brief.md` and `04_roadmap.md`.

- L22: *"My real setup is four things: my laptop for reading and writing, Google Colab for compute, Hugging Face for models and data…"* — *Google Colab* and *Hugging Face* are introduced cold here but explained in chapter 2 with glossary links. Add glossary cross-links inline so a reader who starts at chapter 1 can resolve them on the spot.

No scale anchors needed (no statistics). No voice drift. No implicit assumptions that would block a 14-year-old.

## Chapter 2 — First Contact

**Light pass.** Already glossary-links *parameters*, *tokens*, *Google Colab*, *Hugging Face*, *prompt engineering*, *LLMs are bad at numbers*, *tool use*. No statistics. No scale anchors needed.

- L19: *"3.42 GB downloaded"* — fine, plain.
- L29: *"Jean-Paul Sartre's concept of the absurd is closely related to Albert Camus'."* — quoted from the model, marked as the model's mistake.
- No voice drift.

## Chapter 3 — First Measurement

**Light pass.** First-person, episodic. Numbers are word counts (plain), no statistical concepts.

- L11: *"a 2008 study about feeding schoolchildren in Iran — anthropometric indices, p-values"* — *p-values* is dropped in passing as a vocabulary marker, not a result the reader has to interpret. Borderline. The brief says don't define trivial things; the reader gets the point ("a structured background-methods-results-conclusion shape") without needing a p-value definition. **Decision: leave as-is.** A glossary entry for `p-value` will exist after chapter 6 patches; if the reader bounces back here later, they can resolve it.
- L13: *"Average abstract: 205 words. Shortest: 46. Longest: 373."* — fine, plain numbers.
- L15: PubMed histogram caption, no scale needed.
- No voice drift.

## Chapter 4 — Two Shapes on One Page

**Light pass.** First-person episodic; word-count numbers only.

- L13: *"Average paragraph length: 172 words… PubMed's average was 205."* — fine.
- L19: *"a 966-word paragraph"* — fine.
- L23: *"the project's working agreement calls this *the sense of drift*"* — internal phrase, fine in context.
- No voice drift.

## Chapter 5 — What the Model Can't See

**Full pass starts here.** This is where the dense statistics begin.

- L3: *"Social support and income came out tied — 0.812 and 0.799 — which is to say the first question did not get a first answer. A thousandth of a point is not a winner."* — These are **Pearson correlations** (r-values). The chapter doesn't say so. A 14-year-old has no scale for whether 0.8 is high or low for a correlation. **Patch: add one anchor sentence on first appearance. "These are Pearson correlations on the −1 to +1 scale; in cross-country survey data, anything above 0.7 counts as a strong relationship."**
- L3: *"correlations"* — link to existing `05_glossary.md#pearson-correlation` on first use.
- L7: *"7.16… 6.69… nearly half a point gone in six years… roughly the gap between Denmark and Slovenia"* — already self-anchored. The Cantril ladder is named without a glossary link though. Link to `05_glossary.md#cantril-ladder`.
- L13: *"Dystopia + residual"* — link to `05_glossary.md#dystopia--residual` on first use.
- L13: *"the line of zero net change"* — fine inline.
- L19: *"line of best fit"* and *"line of zero net change"* — *line of best fit* exists in glossary; can leave because the diagonal is described in plain language.
- L19: *"Ninety-nine percent… ninety-eight percent"* — plain.
- L21: *"0.94 points… 0.84 points… 0.10 points"* — these are factor-contribution units, scale anchored by chapter 5's earlier "half a point ≈ Denmark–Slovenia gap." Acceptable.
- L23: implicit assumption *"by construction, it is anything that moves between countries and years and affects how people rate their lives and is not one of: income, number of people you can count on…"* — defines residual implicitly here. Cross-link to `05_glossary.md#residual`.
- L25: *"the book *Thinking in Wholes* argues"* — citation grep red flag? This is an *interpretive* paraphrase about the book's overall argument, not a quoted attribution to a specific phrase. The Session 6 grep pattern catches "the book says/argues/calls/claims/describes/writes" — *argues* is on the list. **Verify against the book.** [grep needed]
- Voice: chapter 5 is the bridge between the early personal voice and the dense Phase-2 voice. Reads well. No drift to smooth.
- **Implicit assumption**: the chapter assumes the reader knows that a regression model has *predicted* and *measured* parts and a residual is the leftover. The end of L23 explains it well enough in plain English ("anything that moves between countries and years and affects how people rate their lives and is not one of…") but a glossary cross-link to `residual` on first use would help.

## Chapter 6 — The Dashboard That Couldn't See the Drop

**Full pass.**

- L5: *"thirty years of Human Development Index data — 206 countries, every year from 1990 to 2023"* — link *Human Development Index* to `05_glossary.md#human-development-index-hdi` on first use.
- L7: HDI explanation is good inline; defines composite, range, history.
- L11: *"the global mean HDI climbed from 0.617 to 0.753"* — HDI is on a 0–1 scale; scale-anchor present implicitly via "between zero and one" in L7. Acceptable.
- L17: *"the correlation between GDP-factor changes and HDI changes came out at 0.32 — moderate, statistically significant"* — needs a scale anchor. **Patch:** brief one-sentence anchor for what "moderate" means on a correlation, AND link to `05_glossary.md#pearson-correlation`. Also flag *statistically significant* as a term — patch by adding glossary entry for `statistically significant` / `p-value`.
- L21: *"Filter to countries where the GDP factor rose but HDI moved less than 0.005 — essentially flat. Thirty-eight countries fit."* — fine.
- L27: *"the correlation came out at r=0.11, not statistically significant"* — leverages the anchor from L17. Fine.
- L31: *"the slope through them is barely there — that's the 0.11"* — fine.
- L39: *"Only when you control for GDP does HDI start to look relevant (p=0.062, borderline significant)"* — *p-value* needs a glossary entry. **Patch.**
- L41: *"Health was the strongest signal at −0.306"* — negative correlation; scale already established. Fine in context.
- L49: *"0.941 in 2019, dipped to 0.930 during COVID, and recovered to 0.946 by 2023"* — fine, anchored by HDI's 0–1 range.
- L53: *"This is the failure mode the book *Thinking in Wholes* keeps returning to: when institutions measure what machines measure…"* — Session 6 grep flag (*"the book… returns to"*). Not on the literal grep list, but interpretive paraphrase in the same family. **Verify against the book.**
- Voice: dense, sustained Phase-2 voice. Consistent with chapters 5 and 7. No drift.

## Chapter 7 — What the Model Heard

**Full pass.** This chapter is the explicit example in the brief: *"Top Ackoff↔TinW pair hits cosine 0.80…"*

- L5: *"Every paragraph becomes 384 numbers, and no individual number means anything legible."* — *embedding* is defined inline in L3–5. Cross-link to `05_glossary.md#embedding` on first use.
- L7: *"To compare two pieces of text, the standard move is cosine similarity — a single number between minus one and plus one… Two paragraphs of meditation prose come back at 0.7 or 0.8. Two paragraphs that share nothing in common come back at 0.05 or 0.10."* — **Excellent. This IS the scale anchor for cosines.** It is exactly what the brief requested. The patch is to make sure the link to `05_glossary.md#cosine-similarity` is on this first use, and that subsequent cosines in chapters 8 and 9 either inherit this anchor or get their own. Currently no cross-link present in chapter 7. **Patch: add cross-link.**
- L7: *"vector"* / *"vector space"* — used here without explanation. The reader can carry it on the geometric metaphor in L5–7 ("the geometry between vectors is what carries the signal"). Borderline. **Decision:** add a short glossary entry for `vector / vector space` because chapters 8 and 9 use the term too.
- L9: *"all-MiniLM-L6-v2"* — this is the sentence-transformer model name. Glossary entry exists at `05_glossary.md#sentence-transformer`. **Patch:** cross-link.
- L9: *"Colab T4"* — *T4* and *Google Colab* both have glossary entries. Cross-link.
- L11–13: *"cosine 0.84… 0.81… 0.75"* and *"0.80"* — first use of cosines as result numbers. The chapter has the scale-anchor sentence at L7 ("0.7 or 0.8 / 0.05 or 0.10") which already covers this. Acceptable.
- L13: *"'a social system has purposes of its own, its parts have purposes of their own, and it's part of a larger system which has purposes of its own'"* — quoted from the Ackoff lecture. Source is in `data/raw/ackoff_lecture_systems_age.txt`. Verify.
- L17–27: cosine 0.5376 + the two long quotes from James and *Thinking in Wholes*. Source verification needed (citation grep).
- L29: *"The shared vocabulary is real… Verdict: meaningful resonance, not a vocabulary trick."* — falsification check; glossary anchor `falsification` exists. Cross-link.
- L31: *"cosine 0.58"* — covered by L7 anchor.
- L35: UMAP. Glossary entry exists. Cross-link.
- Voice: clean, sustained. No drift.

## Chapter 8 — The Oldest Voices

**Full pass.** Densest statistics chapter.

- L3: *"falsification was the point of the test"* — cross-link `falsification`.
- L5: *"KTU 1.12 is the twelfth tablet in the Dietrich/Loretz/Sanmartín museum catalogue"* — KTU explained inline. Fine.
- L7–9: *"permutation"*, *"null distribution"* — `permutation test` exists; `null distribution` is mentioned inside the permutation entry. **Patch:** cross-link `permutation test` on first use.
- L11: *"sim_12 of +0.2310 sits at the forty-fifth percentile of the null distribution, with one-sided p of 0.55"* — needs a scale anchor for *percentile-of-null* + p-value. **Patch:** one sentence: *"the forty-fifth percentile of the null means forty-five per cent of random samples produce a number lower than this and fifty-five per cent produce a number higher; for a finding to count as significant the conventional bar is the ninety-fifth percentile or higher (p ≤ 0.05)."* Then cross-link `permutation test` and (new) `p-value / statistically significant`.
- L13: *"+0.65… +0.58"* — these are cosines. The scale anchor from chapter 7 has not been carried forward; chapter 8 is its own first cosine appearance for a fresh reader. **Patch:** add a brief one-sentence anchor or backlink to chapter 7's anchor. Lighter option: one sentence — *"On the cosine scale (introduced in Chapter 7), 0.65 is high — these are the most-similar pairs anywhere in the ancient corpus."*
- L15: *"the paired difference between mean cosine to the four position-twelve ancient passages and mean cosine to the eleven non-position-twelve ancient passages came out to +0.0130. The bootstrap ninety-five-percent confidence interval was [+0.0118, +0.0142], cleanly excluding zero. The sign-flip permutation p was effectively zero."* — three terms in one sentence: **paired difference**, **bootstrap 95% CI**, **sign-flip permutation**. All three need either glossary entries or inline explanations. The chapter has zero anchor for what +0.0130 means as a paired-difference value. **Patch:** add three glossary entries; add ONE inline anchor sentence in the chapter explaining what a paired-difference measures and roughly what scale to expect (a positive number means the modern texts sit closer to position-12 passages on average than to other ancient passages; values above ~0.01 with a tight bootstrap CI are reliable in this kind of dataset).
- L15: *"75.8 per cent of *Thinking in Wholes* chunks are paired-positive, 79.4 per cent of Ackoff, 69.5 per cent of James"* — *paired-positive* needs an inline gloss. The glossary entry on paired-difference can carry this.
- L17: *"cosines from 0.54 down to 0.46"* — covered by chapter 7 anchor (or new chapter 8 anchor).
- L17: *"translation register"* / *"prose register"* — `register` not in glossary. Used four times in this chapter and again in chapter 9. **Patch:** add glossary entry for `register`.
- L21: UMAP — already linked? Check.
- L23: *"naming what's in the residual"* — referencing back to chapter 5; fine.
- Voice: dense Opus-style. Consistent.

## Chapter 9 — Reddit Lands

**Full pass.**

- L3: *"`sentence-transformers/reddit-title-body`, seven million Pushshift-sourced Reddit posts spanning mid-2010 to mid-2021, pre-filtered for quality. Streaming that dataset, filtering the records to subreddit equals 'Meditation,' took thirty seconds and 500,000 rows scanned to surface 76 posts that fit the 20-to-300 word window."* — three terms: **Pushshift**, **subreddit**, **streaming dataset**. **Patch:** add glossary entry for `subreddit / Pushshift`. *Streaming dataset* can be inline-anchored ("streaming = reading a record at a time without downloading the full file").
- L5: *"mean cosine 0.336 within source — is actually higher than any of the formal corpora's"* — needs scale-context. The within-corpus cosine is a meaningful number for the meditation-discourse density. The chapter says "the internal coherence of the Reddit cluster is actually higher than any of the formal corpora's" which gives relative context, but for a first-time reader the absolute number 0.336 sits unanchored. Borderline. **Decision:** acceptable because the comparative framing carries the meaning.
- L7: *"mean cosine with James 1890 came in at 0.1364 — about three times higher than its mean cosine with *Thinking in Wholes* (0.0450) or the Ackoff lecture (0.0480)"* — anchored by the comparison. Fine. **Patch:** cross-link `cosine similarity` on first use in this chapter.
- L11: *"chunk #810"* — chunk numbering; reader carries it from "1,586 of James 1890" in chapter 7. Fine.
- L13: *"Reddit's paired-difference toward position-twelve ancient passages, computed exactly as Session 8 computed the others: −0.0045. The number is *negative*."* — relies on the glossary entry for *paired-difference* (added in chapter 8 patches). Cross-link on first use in this chapter.
- L15: *"58 per cent of them — are *closer* to the wider ancient sample"*, *"+0.0154… +0.0176… +0.0127… +0.012 to +0.018 band"* — covered by paired-difference anchor.
- L15: *"register"* — covered by chapter 8 patches once `register` is added.
- L17: *"transmission of wholeness language across civilisations"* — interpretive, not a quote. Fine.
- L19: full landscape image. UMAP cross-link inherited.
- L23: *"the connection between the two halves is rhetorical, not statistical"* — Session 11 patch. Stays.
- Voice: dense Opus prose, consistent with chapters 7 and 8.

## Chapter 10 — What I Got Wrong, and How I Caught It

**Light-to-medium pass.** This chapter is sustained reflective prose, no new statistics, and was just written in Session 11.

- L9: *"99% of countries… 98%… 38 of 129 countries"* — references back to chapter 5 / chapter 6. Fine.
- L11: *"top pairs at cosines 0.58 to 0.61"* — chapter 10 is its own context. The cosine scale-anchor lives in chapter 7. A reader who starts here cold has no scale. **Patch:** chapter 10 is the lessons-learned summary; readers may approach it standalone. Add a one-clause inline anchor on first cosine: *"…on the cosine-similarity scale where two paragraphs paraphrasing each other sit around 0.7 and two unrelated paragraphs sit near 0.05–0.10…"*
- L11: *"the structural 'position-twelve cluster'… selection bias"* — *selection bias* is used without explanation. Borderline; reader probably carries it on context. **Decision:** leave inline.
- L17–21: *"unit-of-analysis"* — defined fully in L19 with the country/paragraph contrast. Fine.
- L25: *"the unit I am measuring, and does that unit match the question I am trying to answer?"* — clean lesson. Fine.
- L29: *"a `grep` against the source document"* — *grep* is technical but used in passing as a search verb; reader carries it from context. Fine.
- L31–37: three habits. Clean prose.
- L43: *"Session 12 reads every chapter as if a beginner is encountering it"* — meta-reference to this very session. Fine.
- Voice: reflective, the chapter's own register. Consistent with itself; deliberately distinct from chapters 5–9 (lessons-learned has its own tone, which Session 11 chose deliberately).

---

## Cross-cutting items (apply once)

### New glossary entries to add (alphabetical block, before "## The mental division for this project")

1. **Bootstrap confidence interval** (or **Bootstrap CI**). 95% CI via resampling. ~3–6 sentences.
2. **Paired-difference test**. Per-source mean of (similarity-to-X − similarity-to-Y), tested with bootstrap and sign-flip permutation. ~3–6 sentences.
3. **p-value / statistically significant**. The bar at p ≤ 0.05; what "moderate," "statistically significant," and "borderline" mean colloquially. ~3–6 sentences.
4. **Register** (linguistic). Formal academic English vs. conversational lay register; why it matters in cross-corpus comparison. ~3–6 sentences.
5. **Sign-flip permutation**. The signed-rank style test used to put a p on the paired-difference. ~3–6 sentences.
6. **Subreddit / Pushshift**. What r/Meditation is; what Pushshift was/is and why a Hugging Face mirror was the only viable source. ~3–6 sentences.
7. **Vector / Vector space**. The list of numbers and the geometric space; how cosine similarity uses both. ~3–6 sentences.

### Cross-cutting cross-links to add (terms already in glossary, missing link on first use)

- Chapter 1: `Google Colab`, `Hugging Face` (first introduction at L22).
- Chapter 5: `Pearson correlation` (L3), `Cantril ladder` (L7), `Dystopia + residual` (L13), `residual` (L23).
- Chapter 6: `Human Development Index (HDI)` (L5), `Pearson correlation` (L17 — although chapter 5 introduced it, chapter 6 introduces a fresh number; safer to link first occurrence here too, or rely on chapter 5's link if reading in order — *defer to chapter 5 link only* to avoid clutter).
- Chapter 7: `embedding` (L3), `cosine similarity` (L7), `T4` (L9), `sentence-transformer` (L9), `falsification` (L29), `UMAP` (L35).
- Chapter 8: `falsification` (L3), `permutation test` (L7), `UMAP` (L21).
- Chapter 9: `cosine similarity` (L7), (new) `paired-difference` (L13), (new) `register` (L15), (new) `subreddit/Pushshift` (L3).
- Chapter 10: anchor sentence for cosines on first use (L11).

### Citation grep verification (Session 6 precedent)

Before commit, grep for "the book (says|argues|calls|claims|describes|writes|returns to)" against `data/raw/thinking_in_wholes_2026.md`:
- Chapter 5 L25: *"the book *Thinking in Wholes* argues that most of what is wrong in modern life comes from treating connected things as if they were separate"*. Verify.
- Chapter 6 L53: *"the failure mode the book *Thinking in Wholes* keeps returning to"*. Verify.

### Voice-drift check

Re-read 5 → 10 in sequence after patching.
- Expected: chapters 5 & 6 sit slightly apart from 7–9 (different drafting eras) but the gap is small.
- Chapter 10 is deliberately a different register (reflective lessons-learned). Stays distinct.
- Chapters 1–4 are the personal-episodic voice. Stays distinct from 5–10.

No global voice rewrite is intended. Light touches only on opening/closing sentences if any chapter sounds jarring once the cross-links and anchors are in.
