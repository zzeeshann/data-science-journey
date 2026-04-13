# Session 2 — Record

*What actually happened. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Decisions made

- **Chose sub-question 2** from [02_project_brief.md](../02_project_brief.md): how the language of consciousness shifted from religious to neuroscientific over the last 200 years. Picked on practical grounds — the data is the easiest to get, has a clear time axis, and every phase of the roadmap fits naturally onto it.
- **GitHub repo** set up: https://github.com/zzeeshann/data-science-journey

## What I did

1. Opened a fresh [Colab](../05_glossary.md#google-colab) notebook, set runtime to T4 GPU.
2. Installed `datasets pandas matplotlib` — one line, ~10 seconds.
3. Loaded the first 1000 rows of `ccdv/pubmed-summarization` from [Hugging Face](../05_glossary.md#hugging-face). Got a dataset with two columns: `article` and `abstract`.
4. Printed the first abstract — a real medical study about a school nutrition programme in Iran. First time seeing actual data flow through code I ran.
5. Turned the dataset into a [pandas](../05_glossary.md#pandas) [DataFrame](../05_glossary.md#dataframe). Added a `word_count` column by splitting each abstract on spaces and counting.
6. Ran `.describe()` on word counts → mean 205, std 77, min 46, max 373.
7. Made my first chart — a [histogram](../05_glossary.md#histogram) of word counts using [matplotlib](../05_glossary.md#matplotlib).

## The observation

Modern science abstracts cluster between roughly 150 and 300 words, with the curve dropping off sharply past 300. That cliff is almost certainly the journals' word limit showing up in the data — you can see the rule in the shape.

A second, more honest observation: I (the assistant) predicted a tighter bell curve at Step 5. The actual chart was bumpier and wider than I implied. The std of 77 was already telling that story; I underplayed it. Lesson: when the data disagrees with the story, the data wins. That's the "sense of drift" applied to my own narration, not just to the model's output.

## What got added to the book

- [Chapter 03](../book/chapter_03.md) — first measurement.

## Decisions deferred

- Where to get the *old* religious/philosophical text for the comparison (next session).
- Whether to narrow PubMed to consciousness/neuroscience-specific papers, or keep it broad for now.

## Status at end of session

Sub-question chosen. GitHub live. First dataset loaded, first measurement taken, first chart made. The pipeline works end to end.

## What's next

Session 3: load a 19th-century text (likely from Project Gutenberg), measure it the same way, and put the two charts side by side. First real comparison.

---

## Raw outputs (receipts)

### Code: load the dataset

```python
from datasets import load_dataset
ds = load_dataset("ccdv/pubmed-summarization", split="train[:1000]")
print(ds)
```

Output:
```
Dataset({
    features: ['article', 'abstract'],
    num_rows: 1000
})
```

(Hugging Face also printed warnings about no `HF_TOKEN` — safe to ignore for public datasets.)

### Code: peek at the first abstract

```python
print(ds[0]['abstract'])
```

Output:
```
background : the present study was carried out to assess the effects of community
nutrition intervention based on advocacy approach on malnutrition status among
school - aged children in shiraz , iran.materials and methods : this case - control
nutritional intervention has been done between 2008 and 2009 on 2897 primary and
secondary school boys and girls ( 7 - 13 years old ) based on advocacy approach in
shiraz , iran . the project provided nutritious snacks in public schools over a
2-year period along with advocacy oriented actions in order to implement and promote
nutritional intervention . for evaluation of effectiveness of the intervention
growth monitoring indices of pre- and post - intervention were statistically
compared.results:the frequency of subjects with body mass index lower than 5%
decreased significantly after intervention among girls ( p = 0.02 ) . however ,
there were no significant changes among boys or total population . the mean of all
anthropometric indices changed significantly after intervention both among girls
and boys as well as in total population . the pre- and post - test education
assessment in both groups showed that the student 's average knowledge score has
been significantly increased from 12.5  3.2 to 16.8  4.3 ( p < 0.0001).conclusion :
this study demonstrates the potential success and scalability of school feeding
programs in iran . community nutrition intervention based on the advocacy process
model is effective on reducing the prevalence of underweight specifically among
female school aged children .
```

Note: text is already lowercased and has odd spacing around punctuation — that's pre-processing the dataset creators applied, not how the original paper looked.

### Code: word counts

```python
import pandas as pd
df = pd.DataFrame(ds)
df['word_count'] = df['abstract'].str.split().str.len()
print(df['word_count'].describe())
```

Output:
```
count    1000.000000
mean      205.144000
std        77.603386
min        46.000000
25%       146.000000
50%       215.000000
75%       265.000000
max       373.000000
Name: word_count, dtype: float64
```

### Code: histogram

```python
import matplotlib.pyplot as plt
df['word_count'].hist(bins=30)
plt.title('Word count of PubMed abstracts (n=1000)')
plt.xlabel('Words per abstract')
plt.ylabel('Number of abstracts')
plt.show()
```

Output: see [`/book/images/chapter_03_histogram.png`](../book/images/chapter_03_histogram.png).
