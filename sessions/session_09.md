# Session 9 — Record

*The Wholeness Investigation continues. First five-corpus matrix. Reddit lands and breaks the wholeness-register interpretation. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

Get the modern lay-language voice into the embedding pipeline. Sessions 7 and 8 both hit HTTP 403 against Reddit's anonymous JSON endpoint and deferred Reddit each time. Session 9 fixes that by streaming the `sentence-transformers/reddit-title-body` Hugging Face dataset (Pushshift-sourced, mid-2010 → mid-2021, pre-quality-filtered) and filtering to `subreddit == "Meditation"`. With Reddit in the matrix, run three pre-registered tests, the second of which directly attacks Session 8's open question — was the modern↔position-12 lift a *wholeness-register* signal or a *Victorian-English translation-register* artefact?

## What actually happened

The pre-registered predictions, written before the tests:

> *Test 1 — Reddit-as-modern-lay-voice landing. Descriptive, no falsifiable prediction. Reported via mean cross-source cosines and top-N pairs.*
>
> *Test 2 — Translation-register confound retest. IF the modern↔pos-12 lift from Session 8 is a wholeness-register signal, Reddit (post-2010 modern English) will show paired-diff > 0 toward pos-12 ancient passages, with magnitude in the same band as tinw (+0.0154) and ackoff (+0.0176). IF the lift is a Victorian-English / Legge-1899 translation-register artefact, Reddit's paired-diff will be near zero or negative, while James's lift remains.*
>
> *Test 3 — H3 cross-era resonance, full version. Aggregate paired-diff across all four modern corpora is expected to remain positive (the Session 8 result was robust to bootstrap CI), but the magnitude may shift if Reddit dilutes or amplifies it.*

**Test 2 produced a clean falsification of the wholeness-register interpretation.** Reddit's paired-difference toward position-12 ancient passages came back at **−0.0045** — *negative*, with only 42% of Reddit chunks paired-positive. The other three modern corpora landed where Session 8 reported them: tinw +0.0154, ackoff +0.0176, james +0.0127, all 70%+ paired-positive. Reddit, written in modern conversational English with no Victorian-prose register and no formal book/lecture cadence, sits below zero. Whatever the lift toward position-12 is, it is not wholeness-language reaching across eras. It is something the formal-English-prose corpora share that Reddit doesn't.

The fetch worked but produced fewer posts than targeted. Streaming `sentence-transformers/reddit-title-body` and filtering to subreddit Meditation hit only 81 Meditation rows in the first 500,000 rows scanned (the safety bound), of which 76 fit the 20–300 word window. Reddit r/Meditation is a sparse subreddit relative to the dataset's overall composition, and the dataset is sorted by something other than density. Seventy-six is enough for the paired-difference test (n=76 chunks vs n=4 position-12 passages produces meaningful per-chunk cosines) but smaller than the 300-target the bundle initially proposed. The session record carries the limitation honestly.

Test 3 ran on all 1,820 modern chunks (tinw + ackoff + james + reddit). Aggregate paired-diff +0.0122, bootstrap 95% CI [+0.0111, +0.0134], sign-flip permutation p = 0.0000. Reddit dilutes the Session 8 number from +0.0130 to +0.0122, but the aggregate effect is still strongly positive — because tinw, ackoff, and james between them contribute 1,744 of the 1,820 chunks. The aggregate test was always going to survive Reddit; what it tells us is that tinw, ackoff, and james all have what Reddit doesn't.

## The data

| Corpus | Source | Chunks (20–300 words) | Within-source mean cosine |
|---|---|---|---|
| *Thinking in Wholes* (2026) | `data/raw/thinking_in_wholes_2026.md` | 124 | +0.176 |
| Ackoff lecture | `data/raw/ackoff_lecture_systems_age.txt` | 34 | +0.237 |
| William James, *Principles of Psychology* Vol. 1 (1890) | Project Gutenberg #57628 | 1,586 | +0.255 |
| **Reddit r/Meditation (modern lay voice)** | **HF `sentence-transformers/reddit-title-body`, subreddit=='Meditation'** | **76** | **+0.336** |
| Ancient Voices (15 verified passages) | `ancient_voices/passages/` | 15 | +0.253 |

Total: 1,835 chunks. Reddit has the highest within-source coherence (+0.336) — meditation-prose discourse is tight, even tighter than James's sustained psychology textbook. Pipeline: identical to Session 8. Code in [notebooks/session_09_embeddings.py](../notebooks/session_09_embeddings.py).

## Findings

### 1. Where Reddit lands (descriptive)

Reddit's mean cosine to each other corpus tells a clear story:

| Pair | Mean cosine | n_pairs |
|---|---|---|
| reddit ↔ james | **+0.1364** | 120,536 |
| reddit ↔ ackoff | +0.0480 | 2,584 |
| reddit ↔ tinw | +0.0450 | 9,424 |
| reddit ↔ ancient | **+0.0428** | 1,140 |

Reddit is closer to James 1890 than to anything else modern. James's `Principles of Psychology` is, in significant part, a book about inner experience — attention, perception, the stream of consciousness, the feeling of effort. Modern r/Meditation prose is, in significant part, posts about inner experience — distraction during sitting, the "stop my mind from wandering" question, the feeling of breath. Different prose register, same subject matter. The model picks up the topical overlap.

Four of the top-five Reddit↔James pairs hit the same James paragraph (chunk #810):

> *"When I try to remember or reflect, the movements in question, instead of being directed towards the periphery, seem to come from the periphery inwards and feel like a sort of withdrawal from the outer world…"*

That paragraph in James is about the phenomenology of introspection. The Reddit posts paired with it describe sitting meditation, redirecting attention inward, the felt sense of withdrawing from external thought. Real semantic resonance. James 1890 phenomenology lands on top of 2010s meditation-experience prose because both are first-person reports of attention turned inward. This is the cleanest cross-era finding the project has produced — clearer than Session 7's james↔tinw on systems language, because both sides here are talking about the same kind of moment.

Reddit is much further from tinw and ackoff (+0.045 / +0.048). The systems-thinking modern register has different concerns (organisations, methods, lineages) than the introspective-meditation modern register. They share the word "meditation" loosely (Reddit talks about doing it; tinw mentions it as one of the practices the book recommends in passing) but not much more.

Reddit↔ancient is the lowest cross-source mean in the entire matrix. Reddit is essentially orthogonal to formal scholarly translations of ancient texts. This is consistent with what shows up next.

### 2. The translation-register confound retest

| Modern corpus | Mean paired-diff | Median | % positive | n |
|---|---|---|---|---|
| Thinking in Wholes 2026 | **+0.0154** | +0.0156 | 75.8% | 124 |
| Ackoff lecture | **+0.0176** | +0.0161 | 79.4% | 34 |
| James 1890 | **+0.0127** | +0.0124 | 69.5% | 1,586 |
| **Reddit r/Meditation** | **−0.0045** | **−0.0063** | **42.1%** | **76** |

Reddit is the outlier. Three formal-English-prose corpora — a 2026 systems book, a 20th-century lecture, an 1890 psychology textbook — all sit in the +0.012 to +0.018 band relative to position-12 ancient passages. Reddit sits *below zero*. The majority of Reddit chunks (58%) are *closer* to the wider ancient sample than to the four position-12 passages.

The wholeness-register interpretation of the Session 8 lift fails this test. If the lift had been a register that modern wholeness language shares with the oldest texts, Reddit — written in modern English by people doing actual meditation — should have shown the lift too. It didn't. What tinw, ackoff, james, and the position-12 ancient passages share is therefore something else. The cleanest reading is **formal-English-prose register**: sustained paragraph-length argumentation, abstract conceptual vocabulary, the cadence of published written work. Reddit is short, conversational, question-form, first-person personal experience. The model places it in a different region of the geometry, and that region is no closer to position-12 than to position-11 or position-13 or wider ancient sample.

The top-five Reddit↔position-12 pairs are all Reddit↔I-Ching-Hexagram-12, in the 0.21 to 0.27 cosine range — much lower than the 0.46 to 0.54 range of James↔iching-12 in Session 8. The same hexagram pulls in different modern sources to different degrees. James gets pulled hard. Reddit barely registers. The pull is about how the source is written, not about what the source is.

This is what the cross-era resonance result from Session 8 actually was, then: a register match between formal English prose and a 19th-century scholarly translation of an ancient wisdom text. Real, replicable, statistically robust — and not a finding about wholeness language transmitting across civilisations. The finding is closer to "Hexagram 12 in Legge 1899 reads in formal Victorian English, and any modern formal-English corpus will sit closer to it than to scholarly translations from the 1900s, 1920s, or 1980s." That's a translation-style observation, not a wholeness observation.

### 3. The aggregate cross-era test still holds, marginally diluted

Across all 1,820 modern chunks, paired-diff +0.0122, bootstrap 95% CI [+0.0111, +0.0134], sign-flip p = 0.0000. The aggregate result is robust because tinw + ackoff + james contribute 1,744 of the 1,820 chunks and the formal-prose register dominates. The Session 8 finding wasn't a fluke; it just doesn't mean what its first interpretation suggested.

If the corpora were balanced — say 100 chunks per corpus — Reddit's negative paired-diff would weigh much heavier and the aggregate could land near zero. The aggregate is therefore not a clean H3 test. The per-corpus breakdown is the honest read.

### 4. The 2D landscape — the picture Sessions 7 and 8 were missing

![Full landscape — three modern corpora, Reddit r/Meditation, and 15 ancient passages](../book/images/chapter_09_full_landscape.png)

Five corpora, one frame, finally. The most striking visual fact is Reddit's isolation. The 76 r/Meditation chunks form a tight green cluster on the left side of the chart, completely separated from everything else by a wide gap. James 1890 (red) covers the right two-thirds of the plot in a sustained cloud. Thinking in Wholes (blue) and Ackoff lecture (purple) cluster together at the bottom, slightly below the main James mass. The ancient passages (orange shapes) cluster in the middle of the chart, near the boundary between James and tinw/ackoff.

The position-12 stars, position-11/13 control diamonds, and pyramid-texts wider squares are all crowded together in the central ancient knot — same as Session 8, the cluster does not separate by position. One ancient outlier, ham-13, sits up in the James cloud — a Hammurabi law about witnesses that lands in James-prose territory in the projection (likely an artefact of UMAP working harder to preserve local structure when a 76-point Reddit cluster is added; the underlying cosine to James didn't change).

Reddit's separation is the chart-level statement of Test 2's result. The model treats r/Meditation prose as its own register, sufficiently different from formal published written English that it doesn't sit anywhere near the ancient cluster, the systems-thinking cluster, or the bulk of the James cloud. Reddit is closer to James than to anything else modern, but James is so large that Reddit doesn't sit *inside* James either — the green cluster is its own neighbourhood.

## What this means for the investigation

The Wholeness Investigation's hook is *naming what's in the residual.* Phase 3's strategy was to attack the question through language: if the residual is a wholeness/connection register that the WHR's six factors don't cover, then the language of wholeness should be measurably present in some corpora and not others. Three sessions in, what we have is:

- **Session 7** found a James 1890 ↔ Thinking in Wholes 2026 cross-era resonance on systems language. Real semantic resonance, not surface vocabulary.
- **Session 8** tested whether ancient texts also showed that resonance via a position-twelve cluster hypothesis. The cluster failed falsification. A small aggregate cross-era lift toward position-12 passages survived, with all top qualitative pairs being James↔I-Ching-Hexagram-12.
- **Session 9** put modern lay-language meditation prose in the matrix and tested whether it also showed the lift. It didn't. Reddit's paired-diff went negative. The cross-era lift is therefore not wholeness-register. It is formal-English-prose register meeting Legge's formal Victorian-English translation of one specific I Ching hexagram.

H3 — *the language of wholeness in modern writing is reaching for a register the oldest texts already used* — is now in trouble in its strong form. The strong form said the register transmits across civilisations through some property of wholeness/connection language. The data say what transmits is formal-English-prose register, and the closest match in the ancient corpus happens to be a 19th-century scholarly translation. That's not a cross-civilisation finding; it's a translator-era finding.

A weaker H3 might still survive — perhaps the systems-thinking register and the introspective-attention register both exist as distinguishable modern voices, and one of them (the James↔Reddit phenomenology pairs) carries the project's investigative weight better than the other. Phase 3 has now shipped one really clean cross-era result that the project should hold onto: **a 1890 psychology textbook and 2010s meditation posts describe the felt experience of attention turning inward in semantically adjacent prose.** That's a finding about how introspective experience is described, not about wholeness language. It's also one of the more interesting things to come out of the language work so far.

The candidate name "the residual is wholeness language reaching back across eras" has been falsified in its first form. Two open candidate names remain: (i) the residual is the introspective-attention register that grew between James 1890 and Reddit 2020 and the WHR's six factors don't capture — testable, but needs different instruments than embeddings; (ii) the residual is something else the language work hasn't surfaced yet, which Sessions 10 (WVS) and 11 (BERTopic) might. Phase 3 has two sessions left and has not yet named the residual. It has, however, cleared two candidates honestly.

## Caveats

1. **76 Reddit posts is small.** The session targeted 300 and hit a safety bound at 500,000 rows scanned. r/Meditation is sparse in the dataset (~1 row per 6,000). A future session that needs more Reddit can lift the safety bound, switch to OAuth-based PRAW for live access, or use a different mirror. The 76-post sample is sufficient for the paired-difference test (the per-chunk diff is well-defined for n=76 vs the four pos-12 passages, which is what the test uses) but the per-corpus mean of −0.0045 has a noisier confidence interval than the larger corpora's.
2. **The HF dataset cuts off mid-2021.** Five-year-old Reddit prose is recognisably "modern lay-language" but is missing the post-pandemic tail. Not load-bearing for this session's finding (the negative paired-diff is large enough that the 2021 cutoff is unlikely to flip it), but worth flagging for any later session that wants to argue something about contemporary lay-language register.
3. **The Session 8 cross-era result wasn't *wrong* — its interpretation was.** Aggregate paired-diff held up; the receipts hold up. What changed is the explanation. Session 8 left two interpretations open (wholeness-register or translation-register confound). Session 9 falsifies the first.
4. **MiniLM modern-English bias.** Same as Sessions 7 and 8. The four position-12 passages are scholarly English translations from 1899, 1903, 1921, and 1983. Embedding sensitivity to translator era is a real and unmeasured factor; the within-position-12 cluster failure in Session 8 may itself partly reflect translator-era heterogeneity rather than content-position non-meaningfulness.
5. **UMAP is for the eye.** The Reddit isolation in the 2D projection is consistent with the matrix (mean Reddit↔others all in 0.04–0.14 range vs internal +0.34) but the visual separation is more dramatic than the cosine numbers strictly justify. Don't read the projection as a magnitude statement.
6. **"Formal-English-prose register" is a hypothesis, not a fitted model.** Section 2 describes what tinw/ackoff/james share that Reddit doesn't. That description is well-supported by the paired-diff numbers and the visual separation, but the project hasn't directly measured a "register feature" the way it measured cosines. A Session 11 BERTopic pass could test whether the topics tinw/ackoff/james share with Hex 12 are the same topics, or whether the resemblance is purely stylistic.

## Status at end of session

- Five-corpus matrix: 1,835 chunks across 384-dim vector space. First time the modern lay-language voice is in.
- Reddit fetch via Hugging Face streaming worked. 76 r/Meditation posts loaded. The Sessions 7–8 deferral is closed.
- Test 2 (translation-register confound retest): **wholeness-register interpretation falsified.** Reddit's paired-diff toward pos-12 came in negative (−0.0045, 42.1% positive) while the three formal-prose corpora all sit in the +0.012 to +0.018 band. The Session 8 cross-era lift is a formal-English-prose register effect, not a wholeness-language effect.
- Test 1 found a strong content-level resonance: r/Meditation prose ↔ James 1890 phenomenology of introspection, top pairs at cosines 0.58–0.61, four of five hitting the same James paragraph (#810).
- Test 3 (aggregate): paired-diff +0.0122, CI [+0.0111, +0.0134], p = 0.0000. Robust but dominated by formal-prose corpora; not a clean H3 test in this form.
- Pipeline lives in [notebooks/session_09_embeddings.py](../notebooks/session_09_embeddings.py).
- Chapter 9 written. Image saved to `book/images/chapter_09_full_landscape.png`. This record written.
- 00_index.md updated for Session 9, Chapter 9, the new image, the new notebook.
- No new glossary entries — Session 9's terms (paired-difference, register, formal prose) all sit comfortably under existing entries or are general terms, not project-specific anchors.

---

## Raw outputs (receipts)

### Models in this session

- **Embedding pipeline run:** `sentence-transformers/all-MiniLM-L6-v2` (22M parameters, 384-dim) on Google Colab T4, executed by the user from [notebooks/session_09_embeddings.py](../notebooks/session_09_embeddings.py).
- **Drafted this session record and chapter 9:** Claude Opus 4.7 (1M context) in Claude Code (this session, May 2 2026).
- **Verification (citation grep, image visual check, prediction-order check):** Claude Opus 4.7 in Claude Code (this session).

### Pipeline summary

```
MODEL: all-MiniLM-L6-v2
RANDOM_SEED: 42
VECTOR DIM: 384
TOTAL CHUNKS: 1835    (tinw=124, ackoff=34, james=1586, reddit=76, ancient=15)
REDDIT SOURCE: HF dataset sentence-transformers/reddit-title-body,
              streamed and filtered to subreddit=='Meditation', body 20–300 words
ANCIENT BREAKDOWN: position-12 n=4, position-11 n=3, position-13 n=3, wider n=5
Embedding wallclock on Colab T4: 4.1 s
```

### Reddit fetch trace

```
Streaming sentence-transformers/reddit-title-body, filtering subreddit==Meditation, target 300...
  scanned 100,000 rows | Meditation rows seen: 15 | kept (20–300w): 13 | 4s
  scanned 200,000 rows | Meditation rows seen: 38 | kept (20–300w): 34 | 10s
  scanned 300,000 rows | Meditation rows seen: 42 | kept (20–300w): 38 | 16s
  scanned 400,000 rows | Meditation rows seen: 55 | kept (20–300w): 51 | 23s
  scanned 500,000 rows | Meditation rows seen: 80 | kept (20–300w): 75 | 30s
  Hit safety bound 500,000 rows; stopping early.
Reddit r/Meditation posts loaded: 76  (scanned 500,661 rows, 81 Meditation rows seen)
```

r/Meditation density in the dataset: ~1 row per 6,180. The safety bound stopped the scan at 76 posts; 81 Meditation rows total were observed.

### Pre-registered predictions (printed BEFORE the tests in the same Colab cell)

```
Test 1 — Reddit-as-modern-lay-voice landing.
  Descriptive, no falsifiable prediction. Reported via mean cross-source
  cosines and top-N pairs.
Test 2 — Translation-register confound retest.
  IF the modern↔pos-12 lift from Session 8 is a wholeness-register
  signal, Reddit (post-2010 modern English) will show paired-diff > 0
  toward pos-12 ancient passages, with magnitude in the same band
  as tinw (+0.0154) and ackoff (+0.0176). IF the lift is a Victorian-
  English / Legge-1899 translation-register artefact, Reddit's paired-
  diff will be near zero or negative, while James's lift remains.
Test 3 — H3 cross-era resonance, full version.
  Aggregate paired-diff across all four modern corpora is expected to
  remain positive (the Session 8 result was robust to bootstrap CI),
  but the magnitude may shift if Reddit dilutes or amplifies it.
```

### Test 2 — Translation-register confound retest (full output)

```
Per-corpus paired-difference (mean_to_pos12 − mean_to_wider):
  tinw  : mean=+0.0154  median=+0.0156  pct_positive=0.758  n=124
  ackoff: mean=+0.0176  median=+0.0161  pct_positive=0.794  n=34
  james : mean=+0.0127  median=+0.0124  pct_positive=0.695  n=1586
  reddit: mean=-0.0045  median=-0.0063  pct_positive=0.421  n=76
```

Reddit is below zero. Wholeness-register interpretation falsified.

Top-5 Reddit↔position-12 pairs (the falsification target):

```
[1] cos=+0.2682   reddit#1816   ↔   ancient/iching-12
[2] cos=+0.2549   reddit#1750   ↔   ancient/iching-12
[3] cos=+0.2425   reddit#1765   ↔   ancient/iching-12
[4] cos=+0.2349   reddit#1787   ↔   ancient/iching-12
[5] cos=+0.2074   reddit#1778   ↔   ancient/iching-12
```

All five top pairs are reddit↔I-Ching-Hex-12 — same hexagram that dominated Session 8's James pairs — but at cosines 0.21–0.27 vs Session 8's 0.46–0.54 for James. The same source pulls modern corpora in proportional to their formal-prose register.

### Test 3 — Aggregate cross-era resonance (full output)

```
modern chunks tested: 1820  (across tinw/ackoff/james/reddit)
overall paired diff (mean)             : +0.0122
bootstrap 95% CI on paired-diff mean   : [+0.0111, +0.0134]
sign-flip permutation p (one-sided)    : 0.0000
```

Robust but dominated by formal-prose corpora.

### Test 1 — Reddit landing (full output)

```
Mean within-Reddit cosine: +0.3356  (n=76 chunks, n_pairs=2850)

Mean Reddit ↔ each other corpus:
  reddit ↔ tinw    : +0.0450  (n_pairs=9424)
  reddit ↔ ackoff  : +0.0480  (n_pairs=2584)
  reddit ↔ james   : +0.1364  (n_pairs=120536)
  reddit ↔ ancient : +0.0428  (n_pairs=1140)
```

Reddit's tightest external link is to James 1890 (+0.1364). The clean cross-era finding is the Reddit↔James phenomenology resonance.

Top-5 Reddit↔James pairs:

```
[1] cos=+0.6097   reddit#1747   ↔   james#810
[2] cos=+0.6021   reddit#1795   ↔   james#810
[3] cos=+0.5956   reddit#1755   ↔   james#810
[4] cos=+0.5883   reddit#1756   ↔   james#646
[5] cos=+0.5793   reddit#1819   ↔   james#810
```

Four of five pairs hit the same James paragraph (#810) — phenomenology of inward attention. Real semantic resonance, 130 years apart.

Top-5 Reddit↔Ackoff pairs (much weaker, for contrast):

```
[1] cos=+0.3216   reddit#1776   ↔   ackoff#127  (open question / method of inquiry)
[2] cos=+0.3127   reddit#1819   ↔   ackoff#140  (frustration / parts vs whole)
[3] cos=+0.3060   reddit#1754   ↔   ackoff#149  (childhood meditation / choice)
[4] cos=+0.3042   reddit#1795   ↔   ackoff#140  (mental paths / parts vs whole)
[5] cos=+0.3033   reddit#1769   ↔   ackoff#127  (open question / method of inquiry)
```

Reddit↔Ackoff and Reddit↔TinW peak at ~0.32–0.47, well below the Reddit↔James 0.58–0.61 range. Modern systems-thinking prose is not where Reddit lives.

### Top within-Reddit pairs (sanity check)

```
[1] cos=+0.7925   reddit#1797 ↔ reddit#1809   (meditation retreat sittings)
[2] cos=+0.7915   reddit#1756 ↔ reddit#1807   (focusing / mind wandering)
[3] cos=+0.7902   reddit#1763 ↔ reddit#1807   (focusing / breath / wandering)
[4] cos=+0.7299   reddit#1763 ↔ reddit#1808   (breath control / new meditator)
[5] cos=+0.7239   reddit#1755 ↔ reddit#1780   (sitting experience / sensations)
```

Coherent sanity. The model recognises meditation discourse as one register internally.

### Reference cosines (full matrix)

```
Within-source mean cosines:
  tinw    +0.1756  (n_pairs=7,626)
  ackoff  +0.2373  (n_pairs=561)
  james   +0.2545  (n_pairs=1,256,905)
  reddit  +0.3356  (n_pairs=2,850)
  ancient +0.2528  (n_pairs=105)

Cross-source mean cosines:
  ackoff   ↔ tinw    +0.1673  (n_pairs=4,216)
  ackoff   ↔ james   +0.1451  (n_pairs=53,924)
  ackoff   ↔ reddit  +0.0480  (n_pairs=2,584)
  ackoff   ↔ ancient +0.0643  (n_pairs=510)
  james    ↔ tinw    +0.1091  (n_pairs=196,664)
  james    ↔ reddit  +0.1364  (n_pairs=120,536)
  reddit   ↔ tinw    +0.0450  (n_pairs=9,424)
  ancient  ↔ tinw    +0.0557  (n_pairs=1,860)
  ancient  ↔ james   +0.1129  (n_pairs=23,790)
  ancient  ↔ reddit  +0.0428  (n_pairs=1,140)
```

### Chart

[`book/images/chapter_09_full_landscape.png`](../book/images/chapter_09_full_landscape.png) — UMAP 2D projection of the 1,835 × 384 vector space. Modern corpora as round dots in four colours (tinw blue, ackoff purple, james red, reddit green). Ancient passages as amber shapes with three markers (★ position 12, ◆ position 11/13 control, ▪ wider sample). Each ancient point labelled. Reddit's green cluster sits visibly isolated on the left side — the chart-level statement of Test 2's result.

### Code

[`notebooks/session_09_embeddings.py`](../notebooks/session_09_embeddings.py) — full pipeline. Forks Session 8's script. Replaces the broken anonymous-Reddit-API fetch with a streaming Hugging Face load. Adds the translation-register confound retest (per-corpus paired-difference table). Same UMAP chart code, now five corpora in one frame.

### Verification commands run before commit

```bash
# Number consistency: same headline numbers across files
grep -nE "0\.0045|0\.0122|0\.0154|0\.0176|0\.0127|0\.1364|0\.6097|0\.3356|0\.0118|0\.0142|76 |1,835|1835" sessions/session_09.md book/chapter_09.md

# Citation grep on chapter prose against the book file
grep -inE "the book (says|argues|calls|claims|describes|writes)" book/chapter_09.md

# Image existence + visual verification
ls -la book/images/chapter_09_full_landscape.png

# Pre-registered prediction order in session record
grep -n "PRE-REGISTERED\|pre-registered prediction\|pre-registered predictions" sessions/session_09.md

# Cross-references
grep -n "session_09\|chapter_09" 00_index.md
```
