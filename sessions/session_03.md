# Session 3 — Record

*What actually happened. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

First real two-point comparison on sub-question 2. Load a 19th-century text, measure it the same way as PubMed in Session 2, put the two histograms side by side.

## Decisions made

- **19th-century source:** William James, *The Principles of Psychology*, Volume 1 (1890), from Project Gutenberg. Chosen because James sits exactly on the hinge between philosophical introspection and the beginnings of scientific psychology — the right point on the timeline for sub-question 2.
- **Unit of comparison:** paragraph. A book isn't 1000 self-contained abstracts, so something had to be chosen. Paragraph is the closest analogue — one idea-sized unit of text. Not a perfect comparison (paragraphs are pieces of an argument; abstracts are self-contained), but defensible and honest.
- **Filter threshold:** 40+ words. Anything shorter is almost always a title, heading, footnote fragment, or index entry — not a real paragraph of James's prose.
- **Hamming lecture parked for a later session.** Saved to [`/data/raw/hamming_lecture_01_1995.txt`](../data/raw/hamming_lecture_01_1995.txt) as a candidate 20th-century data point. Does not belong in this session — Session 3's job is the first two-point comparison. Adding a third point before the first comparison is solid would break the plan.

## What I did

1. Opened a fresh [Colab](../05_glossary.md#google-colab) notebook.
2. Downloaded *The Principles of Psychology* Vol. 1 from Project Gutenberg as a `.txt` file (1,668,932 characters).
3. Opened the file in Python and looked at the first 1000 characters — all Project Gutenberg boilerplate, no actual James yet.
4. Found the `*** START OF...` and `*** END OF...` markers Gutenberg puts around every book. Start at character 928, end at character 1,650,455. Trimmed the wrapper. Book length: 1,649,427 characters of actual William James.
5. Split the book on blank lines (`"\n\n"`) to get candidate paragraphs. Got 2,650 pieces — too many, because titles, headings, and footnote fragments each end up as their own "piece".
6. Filtered out anything under 40 words. Kept 1,542 real paragraphs. Threw away 41% of the raw pieces — those were headings, single-line fragments, index entries, Gutenberg scraps.
7. Turned into a [pandas](../05_glossary.md#pandas) [DataFrame](../05_glossary.md#dataframe), added a `word_count` column (same pattern as Session 2).
8. Ran `.describe()`. Mean 172, std 118, min 40, max 966.
9. Made a side-by-side [histogram](../05_glossary.md#histogram) of PubMed (Session 2) vs James.
10. Saved as [`/book/images/chapter_04_comparison.png`](../book/images/chapter_04_comparison.png).

## The observation

The two distributions have almost the same mean (PubMed 205 vs James 172) but completely different shapes.

**PubMed is a hump with a cliff.** Rises from 50, peaks around 225-250 words, falls off, stops dead at ~370. Constrained by journal word limits.

**James is a ramp with a long tail.** Biggest spike at 50-100 words, slides steeply down, dribbles off toward 900+. No ceiling.

Std tells the same story: PubMed 77.6 vs James 118. James has far more variation. PubMed's longest abstract is 373 words; James's longest paragraph is 966 — two and a half times longer.

**The finding:** modern scientific writing is flatter and more uniform, not necessarily shorter. PubMed writers write *to a length*. James wrote *to an idea*. The journal format constrains what can be said.

## Caveats I want on the record

1. **This is not yet a fair test of *consciousness* language.** PubMed (n=1000) is medical abstracts across all of medicine — cancer, nutrition, public health, whatever the dataset happened to include. Not narrowed to consciousness or neuroscience. James is one book on psychology. So what we actually compared is "modern medical writing in general" vs "one 1890 psychologist." The shape difference is real but it's about scientific form, not consciousness specifically.
2. **"PubMed" is loose.** I didn't load PubMed directly; I loaded `ccdv/pubmed-summarization` from Hugging Face, a pre-packaged subset someone else curated for ML research. The writers are real scientists, but the selection is opaque.
3. **Units aren't identical.** A paragraph is a piece of a flowing argument; an abstract is self-contained. The comparison is reasonable but not clean.
4. **The 40-word filter is a judgement call.** A different threshold would give a different shape. Logging it here so I can revisit.

## Sense-of-drift moment

I worked with a dataset called "PubMed" for two whole sessions without ever questioning whether it was really representative of PubMed. I took the label as the thing. I only caught it because I asked a basic question ("what *is* PubMed?") at the end of the session. Lesson: at the start of any new dataset, ask what it actually is, not what it's called. The label is not the thing.

## What got added to the book

- [Chapter 4](../book/chapter_04.md) — The first comparison.

## Decisions deferred

- Narrow PubMed to consciousness/neuroscience-specific abstracts (Session 4 candidate).
- Add a third data point on the timeline — Hamming 1995 is a strong candidate, already saved under [`/data/raw/`](../data/raw/).
- Clean James harder (footnotes, index) if it matters.

## Status at end of session

Two datasets, two measurements, first real comparison made. First finding on record. Pipeline now works for both modern structured data and historical unstructured text — the same pandas DataFrame on the other end either way.

## What's next

Session 4 options (pick one at the start of the session):
1. Narrow PubMed to consciousness/neuroscience papers and redo the comparison properly.
2. Clean James harder — strip footnotes and index — and see if the shape changes.
3. Add a third data point (Hamming 1995) between the two endpoints.

---

## Raw outputs (receipts)

### Code: download and open the book

```python
import urllib.request

url = "https://www.gutenberg.org/cache/epub/57628/pg57628.txt"
urllib.request.urlretrieve(url, "james.txt")

with open("james.txt", "r", encoding="utf-8") as f:
    raw = f.read()

print(f"The file has {len(raw):,} characters.")
print(raw[:1000])
```

Output:
```
The file has 1,668,932 characters.
---
﻿The Project Gutenberg eBook of The Principles of Psychology, Volume 1 (of 2)
    
This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online
at www.gutenberg.org. ...
[truncated — the first 1000 chars are all Gutenberg wrapper, no James yet]

*** START OF THE PROJECT GUTENBERG EBOOK THE PRINCIPLES OF PSYCHOLOGY, V
```

### Code: locate the markers

```python
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

start_position = raw.find(start_marker)
end_position = raw.find(end_marker)

print(f"Start marker found at character: {start_position}")
print(f"End marker found at character: {end_position}")
print(f"Total length of file: {len(raw)}")
```

Output:
```
Start marker found at character: 928
End marker found at character: 1650455
Total length of file: 1668932
```

### Code: trim the wrapper

```python
start_position = raw.find(start_marker)
start_position = raw.find("\n", start_position) + 1

book = raw[start_position:end_position]
book = book.strip()

print(f"Book length: {len(book):,} characters")
print(book[:500])
print(book[-500:])
```

Output (first 500):
```
THE PRINCIPLES OF PSYCHOLOGY

BY

WILLIAM JAMES

PROFESSOR OF PSYCHOLOGY IN HARVARD UNIVERSITY

IN TWO VOLUMES
VOL. I

NEW YORK
HENRY HOLT AND COMPANY
1918

                                  TO
                            MY DEAR FRIEND
                           FRANÇOIS PILLON.
                       AS A TOKEN OF AFFECTION,
                  AND AN ACKNOWLEDGMENT OF WHAT I OWE
                                TO THE
                        CRITIQUE PHILOSOPHIQUE.

PREFACE.

The trea
```

Output (last 500) — footnotes, ending with James signing off on footnote 617 in his own voice: `[617] Why not say 'know'?—-W. J.`

### Code: split and filter

```python
paragraphs = book.split("\n\n")
paragraphs = [p.strip() for p in paragraphs if p.strip()]
real_paragraphs = [p for p in paragraphs if len(p.split()) >= 40]

print(f"Pieces before filtering: {len(paragraphs)}")
print(f"Paragraphs after filtering (40+ words): {len(real_paragraphs)}")
```

Output:
```
Pieces before filtering: 2629
Paragraphs after filtering (40+ words): 1542
```

### Code: measure

```python
import pandas as pd
df_james = pd.DataFrame({"paragraph": real_paragraphs})
df_james["word_count"] = df_james["paragraph"].str.split().str.len()
print(df_james["word_count"].describe())
```

Output:
```
count    1542.000000
mean      172.407263
std       118.044719
min        40.000000
25%        86.000000
50%       140.000000
75%       225.000000
max       966.000000
Name: word_count, dtype: float64
```

### Code: the comparison chart

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(df["word_count"], bins=30, color="steelblue", edgecolor="white")
axes[0].set_title("PubMed abstracts, 2020s (n=1000)")
axes[0].set_xlabel("Words")
axes[0].set_ylabel("Count")

axes[1].hist(df_james["word_count"], bins=30, color="indianred", edgecolor="white")
axes[1].set_title("James, Principles of Psychology, 1890 (n=1542)")
axes[1].set_xlabel("Words")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("chapter_04_comparison.png", dpi=120, bbox_inches="tight")
plt.show()
```

Output: see [`/book/images/chapter_04_comparison.png`](../book/images/chapter_04_comparison.png).

### Gotcha: Colab sessions are ephemeral

First attempt at the chart cell threw `NameError: name 'df' is not defined`. Cause: the Session 2 PubMed data (`df`) was built in a different Colab session, which Colab had cleared when I closed it. The code was still in the notebook but the memory was gone. Fix: added three cells at the top of this notebook re-loading PubMed (install `datasets`, load `ccdv/pubmed-summarization`, build `df`), then **Runtime → Run all**. Lesson for the record: in Colab, *the notebook is the permanent record; memory is temporary*. Every fresh session starts with zero variables until the cells run.

### First paragraph of real James after filtering

```
The treatise which follows has in the main grown up in connection with
the author's class-room instruction in Psychology, although it is true
that some of the chapters are more 'metaphysical,' and others fuller of
detail, than is suitable for students who are going over the subject
for the first time. ...
[a long paragraph where James apologises for writing 1400 pages, quotes
Goethe in German, and tells beginners which chapters to skip]
```
