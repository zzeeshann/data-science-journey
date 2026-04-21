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

## Cantril ladder

A survey instrument the Gallup World Poll and World Happiness Report use to measure subjective wellbeing. Respondents are asked to imagine a ladder with steps numbered 0 to 10, where the top step represents the best possible life for them and the bottom step the worst possible life, and to say which step they currently stand on. The country score reported each year is a three-year average of responses. First used in [Session 4](sessions/session_04.md).

## Dystopia + residual

A single column in the World Happiness Report. It combines two things: the *Dystopia constant*, a time-invariant reference benchmark representing a hypothetical worst country (so every real country's contribution is positive), and the *residual*, which is the part of each country's happiness score that the six measured factors — GDP, social support, health, freedom, generosity, corruption — cannot explain. Because the Dystopia constant does not change over time, the *change* in this column between years is the *change in residual*: any year-over-year movement is the model's unexplained-component movement. Session 4 found this column fell in 98% of countries between 2019 and 2025 while measured factors rose in 99%, pointing to a systematic global variable the WHR model does not capture. First used in [Session 4](sessions/session_04.md).

## Line of best fit

A straight line drawn through a scatter of points that minimises the squared distance between the line and the points (ordinary least squares). The simplest way to summarise a two-variable relationship with one line. In Python: `slope, intercept = np.polyfit(x, y, 1)` — the `1` means "degree-1 polynomial," i.e. a line. First used in [Session 4](sessions/session_04.md).

## Panel data

A dataset with both a cross-section dimension (e.g. country) and a time dimension (e.g. year), so each row is an observation of one unit at one time. The World Happiness Report file is a country × year panel: 2,116 rows ≈ 150 countries × 14 years. Opposite of a pure cross-section (one moment, many units) or a pure time series (one unit, many moments). Panels let you ask questions neither a cross-section nor a time series alone can answer — like "did social support rise in the UK while happiness fell?" First used in [Session 4](sessions/session_04.md).

## Pearson correlation

A single number between −1 and +1 that summarises how tightly two variables move together in a straight-line relationship. +1 = perfect positive line, 0 = no linear relationship, −1 = perfect negative line. Invariant under positive linear transforms, so scaling or shifting either variable doesn't change *r*. Does **not** capture non-linear relationships and is vulnerable to outliers — see the Venezuela moment in [Session 4](sessions/session_04.md), where dropping one broken row shifted *r* from +0.745 to +0.799. In pandas: `df['a'].corr(df['b'])`.

## Residual

The difference between an actual observed value and the value predicted by a model: `residual = actual − predicted`. For a line of best fit, each point has a residual equal to its vertical distance above (positive) or below (negative) the line. In a more complex model like the World Happiness Report's six-factor regression, the residual is everything about the outcome the model's predictors cannot explain. Large residuals, plural, moving together across countries, are not noise — they are a signal that the model is missing a variable. First used in [Session 4](sessions/session_04.md).

## The mental division for this project

- **LLMs handle:** reading, summarising, classifying, comparing styles, hypotheses, explanations.
- **Python handles:** counting, averaging, statistics, charts, numerical comparison.
- **The user handles:** deciding what's interesting, checking both above are sane.

None of the three is optional.
