# 📖 Glossary

*Single source of truth for concepts. Every chapter and session record links here instead of redefining.*

---

## Parameters

The internal dials of an LLM — the size of its brain. Picture a mixing board with billions of knobs, each set to some number. When you give the model a sentence, it flows through all the knobs and each one slightly reshapes the signal. Training = slowly turning all the knobs to the right positions by showing billions of examples.

**"Llama 3.2 1B"** = 1 billion knobs. Claude has vastly more. More parameters → finer distinctions, better-placed references, less blurring of similar ideas.

Not literally neurons — the analogy is loose. A parameter is just a number in memory.

## Tokens

A token is roughly ¾ of a word. The **context window** is how many tokens a model can hold in attention at once. A 1M-token context ≈ 750,000 words ≈ a bookshelf.

**Parameters = size of brain. Tokens = size of notepad in front of brain.** Independent.

## GPU

Graphics Processing Unit. Originally built to draw video game graphics fast — turns out the same chip is brilliant at the maths AI needs. A normal chip (CPU) does things one-at-a-time-but-clever. A GPU does thousands-at-once-but-simple. AI work is the second kind.

Without a GPU, loading a language model takes many minutes or just fails. With one, seconds.

## T4

The specific GPU model Google lends out for free in Colab. Made by Nvidia, a few years old, modest by 2026 standards but genuinely useful — enough for small-to-medium AI models and real datasets. The reason this whole project is possible on a 2016 MacBook.

## Google Colab

A computer I rent from Google, for free, running in my browser. Google keeps the computer in a data centre; I control it through a web page. A **Colab notebook** is a page with two kinds of boxes — code cells (Python, Shift+Enter runs it) and text cells (notes).

Free tier includes a **T4 GPU**, which is what's needed for AI work and what my 2016 Mac doesn't have. Enable it: Runtime → Change runtime type → T4 GPU → Save.

**Colab memory is ephemeral.** When you close a notebook session (or it times out), every variable is wiped. The *code* persists, but the *data it loaded* does not. To keep working, re-run the cells from the top, or use **Runtime → Run all**. Free tier gives one active session at a time.

## Hugging Face

The GitHub of AI models. A website where the open-source AI world publishes:
- **Models Hub** — thousands of LLMs, loadable with one line of Python.
- **Datasets Hub** — ready-to-use datasets, loadable with one line.
- **Spaces** — mini-apps where you can try models in your browser.

The Python library `transformers` is how you use them in code.

## Project Gutenberg

A free online library of books whose copyright has expired — roughly, anything published before about 1928 in the US. 70,000+ books, downloadable as plain text. This project's source for pre-20th-century material.

Every Gutenberg file wraps the actual book in boilerplate — a copyright notice at the top and a license at the bottom. The book proper sits between two marker lines: `*** START OF THE PROJECT GUTENBERG EBOOK ...` and `*** END OF THE PROJECT GUTENBERG EBOOK ...`. Cleaning = finding those markers and keeping only what's between them.

## Pandas

The standard Python library for handling tables of data. Think Excel, but driven by code. Nicknamed `pd` when imported. Almost everything in data work passes through pandas at some point.

## DataFrame

The pandas word for a table. Rows and columns, just like a spreadsheet. You can add new columns, filter rows, run calculations across a column in one line. The basic unit of data work in Python.

## Matplotlib

The standard Python library for making charts. Nicknamed `plt` when imported. Not pretty by default, but it works everywhere and every other charting library is built on top of it or compared to it.

## Histogram

A bar chart of how often each value range appears. Split your data into "bins" (e.g. 30 equal-width buckets), count how many data points fall in each, draw a bar for each bucket. Tells you the *shape* of your data — bell-curve, lopsided, two humps, flat.

## List comprehension

Python shorthand for "make a new list by doing something to each item in an old list." Written with square brackets:

```python
# Keep only paragraphs with 40+ words
real_paragraphs = [p for p in paragraphs if len(p.split()) >= 40]
```

Read left-to-right: *"for each `p` in `paragraphs`, if the word count is 40 or more, keep `p`."* Replaces a three-line for-loop with one clean line. Everywhere in real Python.

## Right-skewed distribution

A distribution where most values are low, a few are very high, and the mean is dragged higher than the median. The chart looks like a ramp starting tall on the left and trailing off to the right. Happens when there's **no ceiling** on the high end — writers who can write paragraphs as long as they want, incomes with no upper limit, reaction times where most are fast but occasionally one is very slow.

Opposite: a **constrained** distribution like PubMed abstracts, where a hard word limit cuts off the high end and produces a humpy shape with a cliff.

Mean vs median is the tell. If mean ≫ median, right-skewed. If mean ≈ median, roughly symmetric.

## Prompt engineering (small-form)

The same model gives wildly different output depending on how you wrap the ask. Instruct models expect chat format:
```python
messages = [{"role": "user", "content": "Your question here"}]
```
Without this wrapping, the model may just echo the question. With it, the model answers.

## Why LLMs are bad at numbers

LLMs predict the next most-likely token based on text patterns. Math isn't pattern-matching; it's exact rule-following. When an LLM "does math" it's *guessing* what the answer looks like. Sometimes right, often quietly wrong.

Reasoning-focused models (o-series, DeepSeek-R1, Claude's reasoning modes) are *less* unreliable but not reliable. Fine-tuning on math helps but doesn't fix the structural limit.

## Tool use (function calling / agents)

The real fix to the math problem. The LLM doesn't do the math — it **writes Python code**, **hands it to a real interpreter**, and **reads the result back**.

- You ask: *"What's the average sentiment?"*
- LLM writes: `df['sentiment'].mean()`
- Python runs it, returns `0.742`.
- LLM reports: *"Average sentiment is 0.742."*

Nothing hallucinated. The number came from real execution. LLM is the brain, Python is the calculator. This is how all serious 2026 AI systems work. "Agents" = LLMs with tools attached.

## Ancient Voices

A deliberately narrow corpus of verified primary-source passages from civilisations with no confirmed direct contact, kept in `ancient_voices/passages/` as one `.txt` file per passage. Each file carries a citation header — text, position, translator, source URL, language, date — and a body of the passage in a single human translation. Translations are public-domain where possible (Hammurabi from Johns 1903, Enuma Elish from Budge 1921, I Ching from Legge 1899) and explicit fair-use research excerpts where no PD English translation exists (Inanna's Descent, Ugaritic). Used as the fourth corpus in the Session 8 embedding pipeline alongside *Thinking in Wholes*, the Ackoff lecture, and James 1890. First used in [session_08.md](sessions/session_08.md).

## Bootstrap confidence interval (CI)

A way to put error bars around a statistic when its true distribution is unknown. The procedure: resample the dataset *with replacement* many times (typically 1,000–10,000 times), recompute the statistic on each resample, and use the resulting distribution as a stand-in for the unknown true one. The 95% confidence interval is the range from the 2.5th to the 97.5th [percentile](#permutation-test) of that distribution: 95 per cent of the resamples produced a value inside it. If the interval cleanly excludes zero, the statistic is reliably non-zero. Session 8 used a bootstrap CI on the cross-era [paired-difference](#paired-difference-test) of +0.0130 and got [+0.0118, +0.0142] — both endpoints comfortably above zero, so the lift is real, not noise. First used in [session_08.md](sessions/session_08.md).

## Cantril ladder

A survey instrument the Gallup World Poll and World Happiness Report use to measure subjective wellbeing. Respondents are asked to imagine a ladder with steps numbered 0 to 10, where the top step represents the best possible life for them and the bottom step the worst possible life, and to say which step they currently stand on. The country score reported each year is a three-year average of responses. First used in [Session 4](sessions/session_04.md).

## Cosine similarity

A single number between −1 and +1 that measures how close two vectors point in the same direction. Computed as the dot product of two vectors divided by the product of their lengths — geometrically, the cosine of the angle between them. +1 means the same direction (very similar), 0 means orthogonal (unrelated), −1 means opposite directions. For text [embeddings](#embedding) the value is almost always between 0 and 1 because the vector spaces these models produce don't really use the negative half. The standard way to ask "how semantically close are these two pieces of text" once both have been embedded. First used in [session_07.md](sessions/session_07.md).

## Dystopia + residual

A single column in the World Happiness Report. It combines two things: the *Dystopia constant*, a time-invariant reference benchmark representing a hypothetical worst country (so every real country's contribution is positive), and the *residual*, which is the part of each country's happiness score that the six measured factors — GDP, social support, health, freedom, generosity, corruption — cannot explain. Because the Dystopia constant does not change over time, the *change* in this column between years is the *change in residual*: any year-over-year movement is the model's unexplained-component movement. Session 4 found this column fell in 98% of countries between 2019 and 2025 while measured factors rose in 99%, pointing to a systematic global variable the WHR model does not capture. First used in [Session 4](sessions/session_04.md).

## Embedding

A list of numbers — a vector — that a neural network produces from a piece of text such that pieces of text with similar meaning produce similar vectors. The model has been trained on billions of sentences in a way that gradually shapes the geometry of its output space: paragraphs about meditation end up near each other, paragraphs about tax policy end up near each other, and the two clusters end up far apart. Once you have an embedding for every piece of text in a corpus, you can ask quantitative questions about meaning that previously required reading: "which paragraphs are closest to this one?", "which corpora overlap?", "what's the unusual neighbour of this passage?" The vector itself is opaque — for [all-MiniLM-L6-v2](#sentence-transformer) it's 384 numbers per chunk, and no individual number means anything legible. The geometry between vectors is what carries the signal. First used in [session_07.md](sessions/session_07.md).

## Falsification

In this project's sense: writing the prediction down before running the test, then accepting whatever the test produces — including outcomes that contradict the prediction. The opposite of running the test, seeing the result, and *then* deciding what counts as "expected." A pre-registered prediction sitting next to a null result is data the project keeps; a result interpreted only after the fact is storytelling. Borderline outcomes are reported as borderline rather than nudged into one column. Session 8 wrote two pre-registered predictions, ran two tests, and reported a rejection on one ([twelve-cluster](#twelve-cluster)) and a support on the other (cross-era resonance). First used in [session_08.md](sessions/session_08.md).

## H1 (growth ≠ development hypothesis)

The first of the four hypotheses in the Wholeness Investigation: that economic growth (rising GDP) does not automatically produce human development (rising HDI), and that the countries where the two have decoupled are the same countries showing the largest falls in the happiness residual. Session 5 found H1 partially confirmed — 38 of 129 countries showed GDP up, HDI flat — but not a global law. The GDP–HDI correlation remained 0.32 globally. See [session_05.md](sessions/session_05.md).

## Human Development Index (HDI)

A composite index published annually by the United Nations Development Programme (UNDP) that measures human development across three dimensions: health (life expectancy at birth), education (mean and expected years of schooling), and standard of living (gross national income per capita, log-scaled). Ranges from 0 to 1. Designed as a counterweight to GDP-only thinking — its foundational argument is that income without health and education is not real development. First used in [session_05.md](sessions/session_05.md).

## Inner join (data merge)

A merge operation that keeps only rows present in both datasets. When Session 5 merged the WHR change panel (141 countries) with the HDI time series (206 countries) on country name, the result was 129 countries — only those appearing in both files. Countries dropped in the merge are typically ones where the naming convention differed between the two sources (e.g. "United States of America" vs "United States"). Always check what the merge dropped before drawing conclusions from the merged dataset. First used in [session_05.md](sessions/session_05.md).

## Line of best fit

A straight line drawn through a scatter of points that minimises the squared distance between the line and the points (ordinary least squares). The simplest way to summarise a two-variable relationship with one line. In Python: `slope, intercept = np.polyfit(x, y, 1)` — the `1` means "degree-1 polynomial," i.e. a line. First used in [Session 4](sessions/session_04.md).

## OLS (ordinary least squares)

The standard method for fitting a straight line through a scatter of points by minimising the sum of squared vertical distances between each point and the line. Produces a slope (how much Y changes per unit of X), an intercept, and a [p-value](#p-value-statistical-significance) (the probability of seeing a slope this large by chance if the true slope were zero). In Session 5, OLS of HDI change on GDP-factor change gave slope = 0.037, p = 0.015. First used in [session_05.md](sessions/session_05.md).

## p-value (statistical significance)

The probability of seeing a result as extreme as the one observed if there were no real effect — purely by chance under the null hypothesis. The conventional cut-off is p ≤ 0.05: a result with p of 0.05 means that, if there were truly no effect in the world, you'd see a number this big about one time in twenty by random variation. *Statistically significant* is the everyday name for "p below 0.05." *Borderline significant* is the everyday name for p between 0.05 and 0.10 — interesting but not conclusive. *Highly significant* is p ≤ 0.01 (one in a hundred), and p effectively zero (≤ 0.001) is the strong-evidence case. Session 5's GDP↔HDI correlation came in at r = 0.32, p = 0.015 (significant); Session 6's controlled HDI relationship at p = 0.062 (borderline). First used in [session_05.md](sessions/session_05.md).

## Paired-difference test

A per-source comparison of similarity to two reference groups. For each chunk in a source corpus, compute its mean [cosine similarity](#cosine-similarity) to group A and to group B, then take the difference (mean-to-A minus mean-to-B). The corpus's *paired-difference* is the mean of those per-chunk differences. A positive number means chunks in the source sit closer, on average, to group A than to group B; a negative number means the opposite. The "paired" word is the point: each chunk is its own control, so per-chunk noise (some chunks happen to sit far from everything) cancels out cleanly. Reliability is checked with a [bootstrap CI](#bootstrap-confidence-interval-ci) and a [sign-flip permutation](#sign-flip-permutation). Session 8 measured each modern corpus's paired-difference toward the four position-12 ancient passages versus the eleven other ancient passages: the formal-prose corpora landed between +0.012 and +0.018, with 70–80% of chunks paired-positive. Session 9 added Reddit at −0.0045 and falsified the wholeness-register reading. First used in [session_08.md](sessions/session_08.md).

## Panel data

A dataset with both a cross-section dimension (e.g. country) and a time dimension (e.g. year), so each row is an observation of one unit at one time. The World Happiness Report file is a country × year panel: 2,116 rows ≈ 150 countries × 14 years. Opposite of a pure cross-section (one moment, many units) or a pure time series (one unit, many moments). Panels let you ask questions neither a cross-section nor a time series alone can answer — like "did social support rise in the UK while happiness fell?" First used in [Session 4](sessions/session_04.md).

## Pearson correlation

A single number between −1 and +1 that summarises how tightly two variables move together in a straight-line relationship. +1 = perfect positive line, 0 = no linear relationship, −1 = perfect negative line. Invariant under positive linear transforms, so scaling or shifting either variable doesn't change *r*. Does **not** capture non-linear relationships and is vulnerable to outliers — see the Venezuela moment in [Session 4](sessions/session_04.md), where dropping one broken row shifted *r* from +0.745 to +0.799. In pandas: `df['a'].corr(df['b'])`.

## Permutation test

A way of asking *"could this number have come up by chance?"* by re-running the calculation thousands of times on randomly-shuffled or randomly-resampled data, building a *null distribution* of what the calculation produces under chance, and seeing where the real number falls within it. If the real number sits at the ninety-ninth percentile of the random distribution, fewer than one per cent of random arrangements would produce something that extreme — strong evidence the real number isn't chance. If it sits at the fiftieth, the real arrangement is indistinguishable from chance. Session 8 used a 10,000-iteration permutation test on the [twelve-cluster](#twelve-cluster) by pooling all fifteen ancient passages, sampling four at random ten thousand times, and asking where the observed sim_12 fell in the resulting null distribution. It fell at the forty-fifth percentile. First used in [session_08.md](sessions/session_08.md).

## Register (linguistic)

The style of writing or speech expected in a particular context, distinct from grammar or vocabulary in isolation. A 19th-century scientific textbook, a Victorian Bible translation, a 2020s Reddit post, and a 1990s lecture transcript all use English but in very different *registers* — formal academic prose, formal devotional translation, conversational lay-language, and mid-century spoken-argument prose. [Embedding](#embedding) models trained on modern English tend to place texts in the same register close together regardless of subject matter, which means a high cross-text [cosine](#cosine-similarity) can sometimes be a register match (formal-prose-meets-formal-prose) rather than a content match. Session 9's negative [paired-difference](#paired-difference-test) for Reddit (−0.0045), contrasted against the +0.012 to +0.018 lift for the three formal-prose corpora, made the register-match interpretation visible and falsified the wholeness-register reading of Session 8's lift. First used in [session_09.md](sessions/session_09.md).

## Residual

The difference between an actual observed value and the value predicted by a model: `residual = actual − predicted`. For a line of best fit, each point has a residual equal to its vertical distance above (positive) or below (negative) the line. In a more complex model like the World Happiness Report's six-factor regression, the residual is everything about the outcome the model's predictors cannot explain. Large residuals, plural, moving together across countries, are not noise — they are a signal that the model is missing a variable. First used in [Session 4](sessions/session_04.md).

## Sentence-transformer

A specific kind of [embedding](#embedding) model — a neural network trained so that whole sentences (and short paragraphs) get one vector each, with the geometry tuned for *semantic* similarity. Built on top of transformer architectures (BERT, MPNet, DistilBERT etc.) but with a final pooling step that collapses many word-vectors into one sentence-vector. The Python library `sentence-transformers` makes them one-liner-loadable from Hugging Face. The default Session 7 model is `all-MiniLM-L6-v2` — small (~80 MB, 22M parameters), fast, 384-dimensional output, runs comfortably on a [T4](#t4) and even on CPU for small corpora. The heavier sibling `all-mpnet-base-v2` produces sharper distinctions but is overkill for first contact. First used in [session_07.md](sessions/session_07.md).

## Sign-flip permutation

A non-parametric test for whether a [paired-difference](#paired-difference-test) is reliably non-zero. The procedure: take each per-chunk paired-difference value, randomly flip its sign (positive becomes negative and vice versa), recompute the mean across all chunks, and repeat thousands of times. Under the null hypothesis that the differences are pure noise around zero, sign-flips are exchangeable and the distribution of those random means represents what chance can produce. The fraction of random reshuffles that produce a mean as extreme as the observed one is the [p-value](#p-value-statistical-significance). When the observed mean sits far from zero, virtually no sign-flip arrangement will match it, and the resulting p collapses to effectively zero. Session 8 ran a 10,000-iteration sign-flip on each modern corpus's paired-difference toward position-12 ancient passages and reported p = 0.0000 across all three. First used in [session_08.md](sessions/session_08.md).

## Subreddit & Pushshift

*Subreddit* — a topic-specific community on the social platform Reddit, addressed with the prefix `r/`. r/Meditation is the subreddit on meditation experience, where posts and comments accumulate around that single subject. *Pushshift* — a third-party service that, until late 2022, archived effectively every public Reddit post and comment in a queryable database, used by social-science and ML researchers as the canonical source for Reddit data. Reddit changed its API access terms in 2023 and Pushshift stopped accepting public queries; the data already archived is preserved in derivative datasets like Hugging Face's `sentence-transformers/reddit-title-body` (~7 million Pushshift-sourced posts, 2010–2021). Session 9 *streamed* that dataset — read records one at a time without downloading the full file — to filter on subreddit equals "Meditation" and surface 76 posts that fit the embedding pipeline's word-window. First used in [session_09.md](sessions/session_09.md).

## Twelve-cluster

The pre-registered hypothesis tested in Session 8: that across several ancient civilisations with no confirmed direct contact (Hammurabi, Enuma Elish, the I Ching, the Descent of Inanna, the Pyramid Texts, Gilgamesh, the Ugaritic Baal cycle), the passage at structural position twelve in canonical works clusters in [embedding](#embedding) space tightly enough to be statistically distinguishable from a random selection of passages from the same texts. Tested as one candidate name for what's in the residual. The 10,000-iteration [permutation test](#permutation-test) put the observed cluster at the forty-fifth percentile of the null distribution — *below* the median of arbitrary four-passage selections. The hypothesis was rejected and the cluster filed as selection bias. Verification reading between sessions also surfaced a methodological problem the original framing hadn't anticipated: position-twelve isn't the same kind of unit across texts (KTU 1.12 is a museum catalogue index, Faulkner Spell 12 is a scholar's catalogue number, Gilgamesh Tablet 12 is the appended Sumerian source), so three of the seven planned texts contributed wider-sample-only. First used in [session_08.md](sessions/session_08.md).

## UMAP

Uniform Manifold Approximation and Projection. A dimensionality-reduction algorithm that takes high-dimensional vectors (e.g. 384-dimensional [embeddings](#embedding)) and projects them to 2D for plotting, while attempting to preserve local neighbourhood structure: points that were close in the original space stay close on the chart. UMAP charts are useful for visual gut-checks but the 2D distances on the page are *not* the actual cosines — the chart is for the eye, not for measurement. Conclusions about clustering structure must be backed by the underlying similarity matrix, not just the projection. Sessions 7 and 8 both use UMAP with `n_neighbors=15`, `min_dist=0.1`, `metric="cosine"`, `random_state=42`. First used in [session_07.md](sessions/session_07.md).

## Vector / vector space

A *vector* in this context is a list of numbers — for [`all-MiniLM-L6-v2`](#sentence-transformer) the list has 384 entries per text chunk, and no individual entry means anything legible on its own. A *vector space* is the geometric world those lists live in: each vector is a point with 384 coordinates, and pairs of vectors have measurable distances and angles between them. Vectors of texts with similar meaning end up pointing in similar directions inside that space (small angles between them), which is exactly what [cosine similarity](#cosine-similarity) measures. The word *space* is the standard mathematical term even though no human can picture 384 dimensions — the geometric metaphor of "two arrows from the origin" is what carries the intuition; the high-dimensional version just keeps the maths intact. First used in [session_07.md](sessions/session_07.md).

## The mental division for this project

- **LLMs handle:** reading, summarising, classifying, comparing styles, hypotheses, explanations.
- **Python handles:** counting, averaging, statistics, charts, numerical comparison.
- **The user handles:** deciding what's interesting, checking both above are sane.

None of the three is optional.
