# Start Session 08 — The Oldest Voices

*Drafted in a session-planning conversation, not by Claude Code. Read this at the start of Session 8 and follow it. If anything here conflicts with `01_working_agreement.md` or `CLAUDE.md`, those win.*

---

## Goal

Point Session 7's embedding pipeline at the oldest writing humans have. Two specific tests, both falsifiable:

**Test 1 — The 12-cluster, quantified.** Across seven texts from civilisations with no confirmed direct contact (Gilgamesh Tablet 12, Enuma Elish 1:12, Hammurabi Law 12, Descent of Inanna ~line 12, I Ching Hexagram 12, Pyramid Texts Spell 12, Ugaritic KTU 1.12), are the seven "12" passages semantically closer to each other than to position-11 and position-13 passages from the same texts? If yes, the cluster survives a falsification attempt. If no, the cluster is selection bias and the project says so plainly.

**Test 2 — Cross-era resonance.** Are the modern wholeness texts (chunks of *Thinking in Wholes*, James 1890, Ackoff lecture, Reddit r/Meditation) semantically closer to the ancient threshold passages than to randomly-sampled ancient non-threshold passages? This is a first concrete test of the conjecture that drove H3: that the language of wholeness in modern writing is reaching for a register the oldest texts already mapped.

This is where Ancient Voices enters the project as a corpus, not as a sub-investigation. There is no separate session log, no separate hypotheses, no separate book. The work is logged in `sessions/session_08.md`. The chapter is `book/chapter_08.md`.

## What this is not

- Not the full H3 test — that's Session 9 (Reddit zero-shot) and Session 11 (topic modelling). This is a focused empirical test of one specific claim.
- Not a comprehensive ancient-text survey. The corpus is deliberately narrow: the 12-cluster + controls + a small wider sample. Larger ancient-text work, if warranted, comes after Session 12 synthesis.
- Not a translation project. The user has done verification work between sessions to pull authoritative translations into `ancient_voices/passages/`. This session reads what's there, not the originals.

## The data

By the time this session starts, `ancient_voices/passages/` should contain at minimum:

**The 12-cluster (7 files):**
- `gilgamesh_tablet_12.txt`
- `enuma_elish_1_line_12.txt`
- `hammurabi_law_12.txt`
- `inanna_descent_line_12.txt`
- `iching_hexagram_12.txt`
- `pyramid_texts_spell_12.txt`
- `ugaritic_ktu_1_12.txt`

**The controls (14 files — positions 11 and 13 from the same seven texts):**
- `gilgamesh_tablet_11.txt`, `gilgamesh_tablet_13.txt` (or nearest equivalents — Gilgamesh has 12 tablets so position 13 doesn't exist; use Tablet 11 only and note the asymmetry in the chapter)
- And so on for the other six. Where a position doesn't exist (Hammurabi has 282 laws so 11 and 13 both exist; I Ching has 64 hexagrams so both exist; etc.), include both.

**A small wider sample (10–20 files):** randomly-selected positions from the same seven texts — not 11, 12, or 13 — to provide a baseline for "ancient writing in general" rather than "ancient writing near the cluster position."

Format for each passage file: see `ancient_voices/passages/README.md`.

If verification is incomplete when this session starts: do not run the test on partial data. Fall back to whichever subset is verified, write the limitation into the session record, and run the test as far as the data permits. Do not synthesise missing passages. Do not work from Claude's memory of what the passage probably says.

## The procedure

1. **Reuse the embedding pipeline from Session 7.** Same model (`all-MiniLM-L6-v2`), same chunking (paragraph-level), same DataFrame structure. Add a `corpus` column value `"ancient"` and a `position` column (`11`, `12`, `13`, or `other`) for the ancient passages.

2. **Compute the within-12 similarity matrix.** For the seven "12" passages, mean pairwise cosine similarity. Call this `sim_12`.

3. **Compute the controls.** For each of positions 11 and 13, the mean pairwise similarity across whichever passages exist at those positions. Call them `sim_11` and `sim_13`. Also compute the mean similarity between each "12" passage and its same-text-position-11 (and position-13) neighbours — `sim_12_to_11` and `sim_12_to_13`.

4. **Permutation test.** Pool all the ancient passages (positions 11, 12, 13, and the wider sample). Sample seven at random, take their mean pairwise similarity, repeat 10,000 times. Look at where `sim_12` falls in that distribution. If it's above the 95th percentile, the cluster is statistically distinguishable from random. If not, it isn't.

5. **Cross-era test.** For each chunk in the modern corpus, find its top-5 nearest neighbours in the ancient corpus. Compute the mean cosine similarity from each modern chunk to (a) the seven "12" passages specifically, and (b) the wider ancient sample. If modern wholeness-laden chunks are reliably closer to the "12" passages than to the wider sample, that's a positive cross-era resonance signal. If not, it isn't.

6. **One chart.** A 2D projection (UMAP) of the combined modern + ancient embedding space, coloured by corpus and shaped by ancient-position (12 vs control vs wider). Save to `book/images/chapter_08_cross_era.png`. Visual gut-check on whether the "12" passages cluster.

## Caveats already baked into the corpus

These are known going in. The chapter must surface them honestly; they aren't problems to solve, they're features of the data the project is upfront about.

- **Gilgamesh has only 12 tablets.** No Tablet 13 exists. Run the test on whichever controls exist per text; the asymmetry is part of the result, not a flaw in it.
- **I Ching Hexagram 11 (T'ai / Peace) is the explicit yin-yang complement of Hexagram 12 (Pi / Standstill).** They are paired in the source structure. Hexagram 11 is *not* a neutral baseline — its closeness to Hexagram 12 is built into the I Ching itself. The chapter must say so, and the permutation test should be reported both with the I Ching position-11 included and excluded (sensitivity check).
- **Descent of Inanna does not use conventional line numbering.** The "~line 12" is approximate and the position-11 / position-13 controls for Inanna are similarly approximate. The chapter says so. The file's `NOTES` header documents which verses were chosen.
- **Ugaritic KTU 1.12 is fragmentary.** What's embedded is a scholarly reconstruction. Damaged sections are marked `[…]` in the file. The result for the Ugaritic passages is therefore softer evidence than for, say, the I Ching — flag this in the chapter when discussing per-text contributions.
- **Translation choice affects embeddings.** A passage in Sandars's 1972 prose Gilgamesh sits in a different vector neighbourhood than the same passage in George's 1999 verse translation. The corpus uses one scholarly translation per text consistently. Translation-sensitivity is a Tier 2 concern for a later session, not a Session 8 deliverable.

## Falsification rules

- **The pre-registered prediction is that the cluster exists.** Write the prediction into the session record before running the permutation test. This is a published-test-after-the-fact concern: writing "we predicted the cluster would survive" only after seeing it survive is not falsification, it's storytelling.
- **If `sim_12` is below the 50th percentile of the permutation distribution, write that as the headline finding.** "The 12-cluster does not survive falsification." Chapter 8 leads with that. The investigation accepts the result and moves on.
- **If the cross-era test produces null results, write that.** Modern wholeness language not being closer to ancient threshold passages than to random ancient passages is a real finding — it tells us the resonance was in the human eye and not in the language itself.
- **Borderline results get reported as borderline.** A permutation p-value of 0.04 with a corpus this small is noisy. Mark for re-test in a later session with more passages rather than overclaim a marginal result.

## What gets written

**`sessions/session_08.md`** — full session record per the format in `CLAUDE.md`. Pre-registered prediction at the top of "What actually happened." Permutation test results. Cross-era test results. Chart filepath. The asymmetry list (which texts had which controls). Model identity in receipts.

**`book/chapter_08.md`** — narrative chapter. Open by picking up Chapter 7's closing line. Walk the reader through what the 12-cluster is and why "selection bias" is the obvious worry. Walk through the falsification design in plain English (what counts as "the cluster being real" before we look at the data). Then the result. Then the cross-era test, in the same shape. Close honestly — whatever the result, it advances the investigation.

If the cluster survives: Chapter 8 is the chapter where ancient texts enter the book as a real presence. Sessions 9–12 can pull from them.

If the cluster does not survive: Chapter 8 is the chapter where the cluster is filed as selection bias. The wider Ancient Voices corpus in `passages/` stays — it's still useful for testing other things (cross-era resonance might still hold even if 12-specific clustering doesn't). The book gains credibility, not loses it, by killing a thread that didn't survive.

**Glossary** entries to add: **Twelve-cluster**, **Falsification (in this project's sense)**, **Permutation test**, **UMAP** (if used). Plus an entry for **Ancient Voices** explaining what the corpus is and where it lives.

**Index** updated: Session 8 line, Chapter 8 line, new image filename, new corpus folder.

## Things to avoid

- Inserting a passage Claude "remembers" instead of one verified between sessions. The chapter cites only what's in `ancient_voices/passages/`.
- Reading interpretive meaning into the cosine numbers. The numbers are what the model produced. Whether they mean what we hope is the falsification test's job.
- Padding the chapter with comparative-mythology speculation (Campbell, Eliade, Jung). The project's standard is empirical and traceable. Lenses come from `data/raw/thinking_in_wholes_2026.md` and the Ackoff lecture, not from speculative theorists imported just for this chapter.
- Treating a borderline result as a positive one. If the permutation p-value is 0.04 with seven passages, that's noisy. Say so. Mark for re-test in a later session with more passages.

## Status going in

- Session 7 has produced a working embedding pipeline. The function names and module layout from Session 7 are reused here.
- Verified passages are in `ancient_voices/passages/`. If they aren't, the session pauses to verify or runs on whatever subset is ready, with the limitation explicit.
- Hypotheses unchanged: H1 partial, H2 inconclusive, H3 partly tested by this session via cross-era resonance, H4 untested.
- The Wholeness Investigation hook — "name what is in the residual" — is what this session is for. The 12-cluster is a candidate name. The session tests whether the candidate is real.
