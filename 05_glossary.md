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

## Google Colab

A computer I rent from Google, for free, running in my browser. Google keeps the computer in a data centre; I control it through a web page. A **Colab notebook** is a page with two kinds of boxes — code cells (Python, Shift+Enter runs it) and text cells (notes).

Free tier includes a **T4 GPU**, which is what's needed for AI work and what my 2016 Mac doesn't have. Enable it: Runtime → Change runtime type → T4 GPU → Save.

## Hugging Face

The GitHub of AI models. A website where the open-source AI world publishes:
- **Models Hub** — thousands of LLMs, loadable with one line of Python.
- **Datasets Hub** — ready-to-use datasets, loadable with one line.
- **Spaces** — mini-apps where you can try models in your browser.

The Python library `transformers` is how you use them in code.

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

## The mental division for this project

- **LLMs handle:** reading, summarising, classifying, comparing styles, hypotheses, explanations.
- **Python handles:** counting, averaging, statistics, charts, numerical comparison.
- **The user handles:** deciding what's interesting, checking both above are sane.

None of the three is optional.
