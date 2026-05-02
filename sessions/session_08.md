# Session 8 — Record

*The Wholeness Investigation continues. First quantitative cross-era test. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

Reuse Session 7's embedding pipeline. Add the verified ancient-text corpus the user assembled between sessions in `ancient_voices/passages/`. Run the two pre-registered tests from [start_session_08.md](../start_session_08.md):

1. **The 12-cluster, falsified.** Across texts from civilisations with no confirmed direct contact, are the position-12 passages semantically closer to each other than to randomly-sampled passages from the same texts? A 10,000-iteration [permutation test](../05_glossary.md#permutation-test) decides.
2. **Cross-era resonance.** Are modern wholeness texts (Thinking in Wholes 2026, Ackoff lecture, James 1890) reliably closer to the position-12 passages than to the wider ancient sample?

Pick up Chapter 7's closing line — *"The next session points the same tool at the oldest writing we have."*

## What actually happened

The pre-registered predictions, written before running the tests, were:

> *Test 1 — sim_12 will fall above the 95th percentile of the permutation distribution (one-sided p < 0.05). Sensitivity: result reported both with and without iching_hexagram_11 in the pool.*
>
> *Test 2 — across modern chunks, paired-difference (mean cosine to position-12) − (mean cosine to wider ancient) will have a positive mean with 95% bootstrap CI excluding zero.*

The tests ran on a 1,759-chunk vector space (the 1,744 modern chunks from Session 7 plus 15 ancient passages, embedded in 3.9 seconds on a Colab T4 by `all-MiniLM-L6-v2`).

**Test 1 failed its prediction. Test 2 passed.**

The 12-cluster does not survive falsification. The mean pairwise cosine across the four position-12 passages (sim_12 = +0.2310) sits at the 45th percentile of the null distribution — *below* the median of randomly-sampled four-passage pools from the same ancient corpus. Excluding the I Ching's hexagram-11 (the yin-yang complement of hexagram-12) as a sensitivity check shifts the percentile to 49.30 — same conclusion. Position-12-as-a-cluster is selection bias.

The cross-era resonance is real but small. Across all 1,744 modern chunks, the paired-difference (mean cosine to the four position-12 passages minus mean cosine to the eleven non-position-12 ancient passages) has a mean of +0.0130, with a 95% bootstrap CI of [+0.0118, +0.0142] that cleanly excludes zero. Sign-flip permutation p = 0.0000. All three modern corpora individually show the lift (tinw +0.0154 / ackoff +0.0176 / james +0.0127), with 69–79% of chunks paired-positive.

The two results pull in different directions. The position-12 passages do not form a coherent cluster among themselves — but modern wholeness texts are closer to them, on average, than to the rest of the ancient corpus. Reading the receipts shows why: the cross-era lift is dominated by I Ching Hexagram 12. All five top modern↔position-12 pairs are James↔iching-12.

## The data

| Text | Position 12 | Position 11 | Position 13 | Wider sample |
|---|---|---|---|---|
| Hammurabi (Johns 1903, PD) | Law 12 ✓ | Law 11 ✓ | Law 13 ✓ | — |
| Enuma Elish T1 (Budge 1921, PD) | line 12 ✓ | line 11 ✓ | line 13 ✓ | — |
| I Ching (Legge 1899, PD) | Hexagram 12 ✓ | Hexagram 11 ✓ ⚠ | Hexagram 13 ✓ | — |
| Inanna's Descent (Wolkstein & Kramer 1983, fair-use) | opening ✓ | — | — | — |
| Pyramid Texts (Faulkner et al., PD) | — | — | — | Unas 213, 217 |
| Gilgamesh (Langdon 1917, PD) | — | — | — | Pennsylvania OB Tablet II |
| Ugaritic (Yogev & Yona 2018; Keen 2010, fair-use) | — | — | — | KTU 1.4, KTU 1.23 |

⚠ I Ching Hexagram 11 (T'ai / Peace) is the explicit yin-yang complement of Hexagram 12 (Pi / Standstill). The two are paired in the source structure. The permutation test was reported both including and excluding iching_hex_11 from the null pool.

15 verified passage files. Four texts contributed to the position-12 cluster (n=4 passages, n_pairs=6). Three contributed wider-sample only — and the reason matters. Pyramid Texts Spell 12 in Faulkner's numbering is not in the public-domain Unas inscriptions; Standard Babylonian Gilgamesh Tablet 12 is paywalled in PD; **Ugaritic KTU numbers are museum catalogue indices in the Dietrich/Loretz/Sanmartín numbering, not content positions.** The bundle's "12-cluster" hypothesis assumed all the "12"s were comparable across texts. They aren't. KTU 1.12 isn't the twelfth section of the Ugaritic mythology; it's the twelfth tablet in a museum catalogue that begins with the Baal Cycle. The methodological point — surfaced in `ancient_voices/notes/ugaritic_ktu_1_12_NOTES.md` and made central to Chapter 8 — is that a hypothesis built on cross-text position numbers needs to verify the position numbers mean comparable things first.

Pipeline: identical to Session 7 (paragraph chunking for modern, one-chunk-per-file for ancient, `all-MiniLM-L6-v2`, L2-normalised, dot-product cosine matrix). Code in [notebooks/session_08_embeddings.py](../notebooks/session_08_embeddings.py).

## Findings

### 1. The 12-cluster does not survive falsification

| Statistic | Value |
|---|---|
| sim_12 (n=4 passages, n_pairs=6) | **+0.2310** |
| sim_11 (n=3 passages, n_pairs=3) | +0.1857 |
| sim_13 (n=3 passages, n_pairs=3) | +0.1437 |
| sim_12_to_11 (same-text adjacent pairs, n=3) | **+0.6518** |
| sim_12_to_13 (same-text adjacent pairs, n=3) | **+0.5847** |

Two readings of the table:

First, the position-12 mean (+0.2310) is not distinguishable from the position-11 mean (+0.1857) or the position-13 mean (+0.1437). The four position-12 passages share roughly the same level of mutual similarity as the position-11 passages do — which is "ancient texts in scholarly English translation, vaguely related register." There is no measurable thing about position 12 specifically.

Second — and this is the more revealing number — the same-text adjacent pairs (Hammurabi 11↔12, Enuma Elish 11↔12, I Ching 11↔12, and the same trios for 13) hit cosine +0.65 and +0.58 respectively. *Within* a text, adjacent passages cluster very tightly. Of course they do. They share author, register, vocabulary, narrative thread. The structural unit the model sees is "same text," not "same position number across texts."

The permutation test confirms it. Pooling all 15 ancient passages and sampling 4 at random ten thousand times, the null distribution of mean pairwise cosines has mean +0.2521 and standard deviation 0.096. The observed sim_12 of +0.2310 sits at the 45.35th percentile — *below* the null median. One-sided p = 0.5465. Excluding iching_hexagram_11 from the pool as a sensitivity check (since hex-11 is the structural complement of hex-12), the percentile shifts to 49.30, p = 0.5070. Same answer either way.

**The headline: the 12-cluster does not exist as a measurable property of these passages.** The pre-registered prediction is rejected. The cluster as originally framed was an artefact of selection — pre-picking position 12 from each text, then noticing those pre-picked passages share a cosine baseline that any other 4-passage selection from the same texts also shares.

### 2. Cross-era resonance survives, but as a smaller and narrower thing

| Modern corpus | Mean paired-diff | Median | % positive | n |
|---|---|---|---|---|
| Thinking in Wholes 2026 | +0.0154 | +0.0156 | 75.8% | 124 |
| Ackoff lecture | +0.0176 | +0.0161 | 79.4% | 34 |
| James 1890 | +0.0127 | +0.0124 | 69.5% | 1,586 |
| **All modern chunks** | **+0.0130** | — | — | 1,744 |

Bootstrap 95% CI on the overall paired-difference mean: [+0.0118, +0.0142]. Sign-flip permutation p (10,000 iterations): 0.0000. The lift is reliably positive. All three modern corpora individually show it. The pre-registered prediction is supported.

But the magnitude is modest — a paired difference of +0.013 in cosine space — and the qualitative receipts complicate the read. The top-5 modern↔position-12 pairs are *all* James↔iching-12:

> [1] cos=+0.5440 james#836 ↔ ancient/iching-12
> [2] cos=+0.4858 james#643 ↔ ancient/iching-12
> [3] cos=+0.4793 james#738 ↔ ancient/iching-12
> [4] cos=+0.4609 james#999 ↔ ancient/iching-12
> [5] cos=+0.4591 james#425 ↔ ancient/iching-12

I Ching Hexagram 12 in James Legge's 1899 translation is a long passage in formal late-Victorian English. James 1890 is a long psychology textbook in formal late-Victorian English. The cosine lift on the top pairs may be partly a translation-register match (Legge English meeting James English) rather than a cross-civilisation resonance on wholeness language specifically. The strongest qualitative signal in the data has a translation-style explanation that needs ruling out before the result can be claimed as cross-era.

The aggregate paired-difference test still holds. tinw and ackoff (modern English, post-1970) show roughly the same lift toward position-12 as James does, which suggests the effect isn't pure 1899↔1890 register matching. But the qualitative top pairs leave the question open.

### 3. The 2D landscape

![Cross-era embedding landscape — modern wholeness texts and 15 ancient passages](../book/images/chapter_08_cross_era.png)

Three corpora and 15 ancient orange shapes in one plot. James 1890 (red) covers most of the chart in a sustained cloud. Thinking in Wholes (blue) and Ackoff lecture (purple) sit together on the right edge. Thirteen of the fifteen ancient passages cluster tightly near (but not in) the tinw/ackoff group — the position-12 stars, the position-11/13 control diamonds, and the pyramid-texts wider squares all crowd into one knot, structurally indistinguishable. The two outliers — `gilgamesh-w` (the Pennsylvania Tablet II dream sequence) and `ugaritic-w` (the KTU 1.4/1.23 wider passages) — drift left into James's narrative-prose neighbourhood. Both are narrative excerpts in prose-poem English, which the model places adjacent to James's own sustained prose register, not the law-code / cosmogony / wisdom-literature register the rest of the ancient corpus shares.

The chart is consistent with the matrix. No visible position-12 separation. The model treats "ancient text in formal scholarly English translation" as one register, full stop.

## What this means for the investigation

The Wholeness Investigation's hook is *"name what's in the residual"* — the unmeasured thing that fell across 141 countries between 2019 and 2025. Phase 3 is the language-level attack on that question. Session 7 contributed an unplanned data point: a 19th-century psychologist already operating in the systems-thinking register on at least two specific paragraphs. Session 8 was supposed to extend that finding back five thousand years. It didn't.

The position-12 cluster as originally framed was selection bias. The four position-12 passages do not share a measurable semantic property the rest of the ancient corpus lacks. Hypothesis 3 is not advanced by the cluster falsification — but it is sharpened. The framing *"a register the oldest texts already used"* needs a different definition than "passage at structural position 12." If wholeness language is in the oldest texts, it is not at position 12 specifically; it is somewhere else, or it is distributed, or the register itself is too coarse for this kind of pre-registered position test.

The cross-era resonance result is real but compromised. Modern wholeness texts are closer to the position-12 passages than to the wider ancient sample, on average, with a tight bootstrap CI and a vanishing sign-flip p. But the top qualitative pairs are all James↔I-Ching-Hexagram-12, which raises the translation-register confound — Legge 1899 English meeting James 1890 English. To claim cross-era resonance as a wholeness-register finding rather than a 19th-century-English finding, Session 11 (BERTopic) or a later sensitivity session needs to control for translator-era and translator-style.

The catalogue-vs-position discovery is the most useful methodological output of the session. The bundle's H3 patch had embedded an assumption — that "position 12 across seven canonical texts" was a comparable thing — that verification reading dissolved. KTU 1.12 is a museum catalogue index, not a content position. Faulkner Spell 12 isn't inscribed in the Unas pyramid. Gilgamesh has only twelve tablets, and the Standard Babylonian Tablet 12 is the appended Sumerian source rather than a structurally-twelfth piece of the epic. The question *"is there something special about position 12 across civilisations?"* presupposed that position 12 means the same kind of thing across civilisations. It doesn't.

What this leaves Phase 3 with: Sessions 7 and 8 together produce a small but reliable cross-era cosine lift toward I Ching Hexagram 12, and a robust null on the broader 12-cluster. Session 9 still owes the modern lay-language voice (Reddit r/Meditation, this session also got HTTP 403). Session 11 still owes the proper modern-corpus topic-modelling pass. The investigation does not yet name the residual. It has filed one candidate name as selection bias, which is what falsification is for.

## Caveats

1. **The 12-cluster failure is the biggest finding, not a footnote.** Per the falsification rules in [start_session_08.md](../start_session_08.md): *"If sim_12 is below the 50th percentile of the permutation distribution, write that as the headline finding. The 12-cluster does not survive falsification."* The chapter and this record both lead with it.
2. **The cross-era lift is small (+0.013) and dominated by I Ching Hexagram 12.** All top-5 modern↔position-12 pairs are James↔iching-12. The effect could be a translation-register confound rather than a wholeness-register signal. tinw and ackoff (post-1970 modern English) showing the same lift makes the pure-Victorian-English explanation harder to sustain, but doesn't eliminate it.
3. **Catalogue-vs-position is now a confirmed methodological tension.** KTU numbers are museum indices. Pyramid Texts spell numbers are scholar's catalogue numbers (Faulkner numbering wasn't inscribed). The Gilgamesh Standard Babylonian Tablet 12 is the appended Sumerian source, not a structural twelfth. Three of the seven planned texts contribute wider-sample-only for this reason.
4. **n=4 for the position-12 set is small.** Six pairwise cosines is a small sample even for a permutation test. A negative result here is robust (it would take a much larger sim_12 to clear the 95th percentile of a small-n null), but if a future session adds verified PD passages from more texts, the test should be re-run.
5. **MiniLM trained on modern English** has the same translation-drift suppression as in Session 7. The four position-12 passages are in scholarly English translations from 1899, 1903, 1921, and 1983. Embedding sensitivity to translator era and translator style is real and unmeasured.
6. **Reddit r/Meditation still returns HTTP 403** in this session's run, as expected. n=0 logged. Session 9 picks up the access-path workaround.
7. **UMAP is for the eye, again.** The 2D distances on the chart are not the actual cosines. The visual confirmation that the position-12 stars don't separate from the controls is a triangulation with the matrix, not a finding on its own.

## Status at end of session

- 1,759 chunks embedded into a 384-dim vector space. The 15 verified ancient passages join the modern corpus from Session 7 in one matrix.
- Test 1 (12-cluster falsification): **null result.** sim_12 sits at the 45th percentile of the permutation distribution including iching_hex_11, 49th excluding. p = 0.5465 / 0.5070. The cluster does not survive.
- Test 2 (cross-era resonance): **positive but compromised.** Paired-diff +0.0130, 95% CI [+0.0118, +0.0142], sign-flip p = 0.0000. All three modern corpora show the lift. Top-5 qualitative pairs are James↔iching-12, raising the translation-register confound.
- Methodological discovery: position-number-across-texts is not a coherent comparison unit. Three of seven planned texts had to contribute wider-sample-only because their "12"s are catalogue indices or scholar's spell numbers rather than content positions.
- Pipeline lives in [notebooks/session_08_embeddings.py](../notebooks/session_08_embeddings.py). Reusable for any subsequent ancient-corpus extension.
- Reddit r/Meditation deferred to Session 9 (still 403).
- Chapter 8 written. Image saved to `book/images/chapter_08_cross_era.png`. This record written.
- Glossary updated with five entries: [Ancient Voices](../05_glossary.md#ancient-voices), [Falsification](../05_glossary.md#falsification), [Permutation test](../05_glossary.md#permutation-test), [Twelve-cluster](../05_glossary.md#twelve-cluster), [UMAP](../05_glossary.md#umap).
- `00_index.md` updated for Session 8, Chapter 8, the new image, and the new notebook.

---

## Raw outputs (receipts)

### Models in this session

- **Embedding pipeline run:** `sentence-transformers/all-MiniLM-L6-v2` (22M parameters, 384-dim) on Google Colab T4, executed by the user from [notebooks/session_08_embeddings.py](../notebooks/session_08_embeddings.py).
- **Drafted this session record and chapter 8:** Claude Opus 4.7 (1M context) in Claude Code (this session, May 2 2026).
- **Verification (citation grep, image visual check, cross-reference resolution, prediction-order check):** Claude Opus 4.7 in Claude Code (this session).

### Pipeline summary

```
MODEL: all-MiniLM-L6-v2
RANDOM_SEED: 42
VECTOR DIM: 384
TOTAL CHUNKS: 1759    (tinw=124, ackoff=34, james=1586, reddit=0, ancient=15)
ANCIENT BREAKDOWN: position-12 n=4, position-11 n=3, position-13 n=3, wider n=5
ANCIENT pos-12 members: hammurabi, enuma_elish, iching, inanna
Embedding wallclock on Colab T4: 3.9 s
```

### Pre-registered predictions (printed BEFORE the tests in the same Colab cell)

```
Test 1 — sim_12 will fall above the 95th percentile of the
  permutation distribution (one-sided p < 0.05). Sensitivity:
  result reported both with and without iching_hexagram_11 in the pool.
Test 2 — across modern chunks, paired-difference
  (mean cosine to position-12) − (mean cosine to wider ancient)
  will have a positive mean with 95% bootstrap CI excluding zero.
```

### Test 1 — 12-cluster falsification (full output)

```
sim_12       (n=4 passages, n_pairs=6) : +0.2310
sim_11       (n=3 passages, n_pairs=3) : +0.1857
sim_13       (n=3 passages, n_pairs=3) : +0.1437
sim_12_to_11 (same-text pairs, n=3)    : +0.6518
sim_12_to_13 (same-text pairs, n=3)    : +0.5847

Permutation — INCLUDING iching_hexagram_11 in pool
  pool size: 15, sample size: 4, n_perm: 10000
  sim_12 percentile in null distribution : 45.35
  one-sided p (perm_mean ≥ sim_12)       : 0.5465
  permutation mean ± std                 : +0.2521 ± 0.0961

Permutation — EXCLUDING iching_hexagram_11 from pool (sensitivity)
  pool size: 14, sample size: 4, n_perm: 10000
  sim_12 percentile in null distribution : 49.30
  one-sided p (perm_mean ≥ sim_12)       : 0.5070
  permutation mean ± std                 : +0.2443 ± 0.0963
```

Both versions of the test put sim_12 below the median of the null distribution. The cluster does not survive falsification.

### Test 2 — Cross-era resonance (full output)

```
modern chunks tested: 1744  (tinw=124, ackoff=34, james=1586)
per-corpus paired-difference (mean_to_pos12 − mean_to_wider):
  tinw  : mean=+0.0154  median=+0.0156  pct_positive=0.758  n=124
  ackoff: mean=+0.0176  median=+0.0161  pct_positive=0.794  n=34
  james : mean=+0.0127  median=+0.0124  pct_positive=0.695  n=1586
overall paired diff (all modern chunks)   : mean=+0.0130
bootstrap 95% CI on paired-diff mean      : [+0.0118, +0.0142]
sign-flip permutation p (one-sided)        : 0.0000
```

Lift is reliably positive, all three modern corpora individually contribute, magnitude is small.

### Top 5 modern ↔ position-12 pairs (qualitative receipts)

```
[1] cos=+0.5440   james#836   ↔   ancient/iching-12
    A: "_In each kind of self, material, social, and spiritual, men distinguish between
       the immediate and actual, and the remote and potential,_ between the narrower
       and the wider view, to the detriment of the former and advantage of the latter…"
    B: "In Phî there is the want of good understanding between the (different classes of)
       men, and its indication is unfavourable to the firm and correct course of the
       superior man. We see in it the great gone and the little come…"

[2] cos=+0.4858   james#643   ↔   ancient/iching-12
[3] cos=+0.4793   james#738   ↔   ancient/iching-12
[4] cos=+0.4609   james#999   ↔   ancient/iching-12
[5] cos=+0.4591   james#425   ↔   ancient/iching-12
```

All five top pairs are James 1890 ↔ I Ching Hexagram 12 (Legge 1899). Translation-register confound flagged in Findings §2.

### Reference cosines (within and across sources)

```
Within-source mean cosines:
  tinw    +0.1756  (n_pairs=7,626)
  ackoff  +0.2373  (n_pairs=561)
  james   +0.2545  (n_pairs=1,256,905)
  ancient +0.2528  (n_pairs=105)
  reddit  n/a (n=0)

Cross-source mean cosines:
  ackoff  ↔ tinw    +0.1673  (n_pairs=4,216)
  ackoff  ↔ james   +0.1451  (n_pairs=53,924)
  ackoff  ↔ ancient +0.0643  (n_pairs=510)
  james   ↔ tinw    +0.1091  (n_pairs=196,664)
  ancient ↔ tinw    +0.0557  (n_pairs=1,860)
  ancient ↔ james   +0.1129  (n_pairs=23,790)
```

Ancient↔james (+0.1129) is the highest ancient↔modern mean — consistent with the qualitative top-5 receipts being dominated by James pairs, and the chart's two ancient outliers (gilgamesh-w, ugaritic-w) drifting into the James cloud.

### What Reddit returned

```
reddit top   -> HTTP 403
reddit top   -> HTTP 403   (top-month variant)
reddit hot   -> HTTP 403
reddit new   -> HTTP 403
posts pulled: 0
```

Same as Session 7. Session 9's first task.

### Chart

[`book/images/chapter_08_cross_era.png`](../book/images/chapter_08_cross_era.png) — UMAP 2D projection of the 1,759 × 384 vector space. Modern corpora as round dots in three colours (tinw blue, ackoff purple, james red). Ancient passages as amber shapes with three markers (★ position 12, ◆ position 11/13 control, ▪ wider sample). Each ancient point labelled.

### Code

[`notebooks/session_08_embeddings.py`](../notebooks/session_08_embeddings.py) — full pipeline. Forks Session 7's script. Adds the ancient corpus loader, the 12-cluster falsification block (with sensitivity rerun), the cross-era paired-difference block (with bootstrap CI and sign-flip p), and the combined-corpus UMAP chart.

### Verification commands run before commit

```bash
# Number consistency: same headline numbers across files
grep -nE "0\.2310|0\.0130|0\.5465|0\.5070|0\.5440" sessions/session_08.md book/chapter_08.md

# Citation grep on chapter prose against the book file
grep -inE "the book (says|argues|calls|claims)" book/chapter_08.md

# Image existence + visual verification
ls -la book/images/chapter_08_cross_era.png

# Glossary anchors resolve
grep -n "^## " 05_glossary.md | grep -iE "twelve|falsif|permutation|umap|ancient"

# Pre-registered prediction order in session record
grep -n "PRE-REGISTERED\|pre-registered\|Test 1 — 12-cluster\|TEST 1" sessions/session_08.md

# Cross-references
grep -n "session_08\|chapter_08\|chapter_08_cross_era" 00_index.md
```
