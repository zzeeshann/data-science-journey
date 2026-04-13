# Chapter 2 — First Contact

*(Draft — edit freely. Concept definitions live in [05_glossary.md](../05_glossary.md).)*

---

Before you write serious code, you have to feel the thing you're learning about. This chapter is about the moment I went from "LLMs are something I hear about" to "LLMs are something I ran on a free cloud computer from my old laptop." It took about an hour. It cost zero dollars.

---

## Getting the vocabulary straight

Two words had to click before anything useful could happen: [**parameters**](../05_glossary.md#parameters) and [**tokens**](../05_glossary.md#tokens). People use them constantly without explaining them. Definitions are in the glossary so I'm not repeating them here — the short version: parameters are the size of the model's brain, tokens are the size of the notepad it reads from. Independent.

Also had to understand what [**Google Colab**](../05_glossary.md#google-colab) actually is (a computer I rent from Google, free, in my browser) and what [**Hugging Face**](../05_glossary.md#hugging-face) is (the GitHub of AI models).

---

## Running my first LLM

Three cells, each with a specific job:

1. Install `transformers` from Hugging Face — 8 seconds.
2. Load SmolLM2-1.7B-Instruct — ~1 minute, 3.42 GB downloaded.
3. Ask it a question.

First attempt at *"What did Camus mean by the absurd?"* got almost nothing back — the model just echoed my question. First real lesson: [**the wrapping around your question matters as much as the question itself**](../05_glossary.md#prompt-engineering-small-form). Instruct models expect chat format. Once I wrapped it properly, the model answered in full paragraphs.

---

## Feeling parameter size in the output

SmolLM2 gave a decent textbook answer about Camus — humans crave meaning, the universe is indifferent, Myth of Sisyphus, acceptance. But it opened with *"Jean-Paul Sartre's concept of the absurd is closely related to Albert Camus'."* That's wrong. The absurd is specifically Camus's territory. Sartre had his own ideas (nausea, bad faith). The model blurred two thinkers.

Claude's answer on the same question was sharper — phrases like *"meaning-hungry creatures in a meaning-silent world,"* the refusal of two escapes (suicide and invented grand systems), Sisyphus pushing the rock *happy*.

**Parameter size isn't abstract. You can feel it in the output.** And the ability to feel it — to sense when a model is slightly off — is the most valuable skill I can develop. That skill is the difference between copilot and crutch.

---

## Why LLMs are bad at numbers

Second thing I learned: [**LLMs aren't calculators**](../05_glossary.md#why-llms-are-bad-at-numbers), and for data science this matters enormously. They predict plausible-looking tokens, not exact numbers. A hallucinated average can look completely reasonable and still be wrong.

The real fix — and the modern answer — is [**tool use**](../05_glossary.md#tool-use-function-calling--agents). The LLM doesn't do math; it writes Python, hands it to a real interpreter, and reads the result back. That's what "AI agents" really are. Nothing hallucinated — the number came from real execution on real data.

---

## The mental model I'm carrying forward

For my project: **LLMs handle text (reading, summarising, classifying). Python handles numbers. I handle deciding what's interesting and checking both are sane.** None optional. Full version in [the glossary](../05_glossary.md#the-mental-division-for-this-project).

---

## What I have now, after Session 1

- A working cloud setup. Zero cost.
- A real LLM I can call in three lines.
- Hugging Face's library of models and datasets.
- One honest observation about model quality from my own eyes.
- A clear mental model of what LLMs can and can't do.

That's more than most people who "study data science" have after a week. And I did it in an hour.

---

*(End of Chapter 2. Next: narrowing the question, loading first real data.)*
