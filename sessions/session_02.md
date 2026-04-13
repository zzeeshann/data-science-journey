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
5. Turned the dataset into a [pandas](../05_glossary.md#pandas) DataFrame. Added a `word_count` column by splitting each abstract on spaces and counting.
6. Ran `.describe()` on word counts → mean 205, std 77, min 46, max 373.
7. Made my first chart — a histogram of word counts using [matplotlib](../05_glossary.md#matplotlib).

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
