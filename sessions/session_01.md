# Session 1 — Record

*What actually happened. Not a plan, a diary entry. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Setup decision

Skipped local Ollama install — 2016 Intel MacBook Pro is too old, and Claude is already available as a much bigger model. Went cloud-first instead. See [01_working_agreement.md](../01_working_agreement.md) for the setup rationale.

## What I did

1. Opened [Google Colab](../05_glossary.md#google-colab) in my browser, created a notebook, enabled T4 GPU.
2. Installed `transformers accelerate` — ~8 seconds.
3. Loaded SmolLM2-1.7B-Instruct from [Hugging Face](../05_glossary.md#hugging-face) — ~1 minute, 3.42 GB.
4. Asked it *"What did Camus mean by the absurd?"* — got near-empty output because I sent raw text.
5. Learned [prompt engineering](../05_glossary.md#prompt-engineering-small-form) — wrapped the question in chat format, got a full paragraph.
6. Compared SmolLM2's answer to Claude's. Saw [parameter size](../05_glossary.md#parameters) in the output.

## The observation

SmolLM2 got the core of Camus right but opened with *"Jean-Paul Sartre's concept of the absurd is closely related to Albert Camus'."* Wrong — the absurd is specifically Camus's. Sartre had his own ideas (nausea, bad faith). Claude was sharper, more specific, didn't blur the two thinkers.

First real instance of the "sense of drift" skill — noticing where a model is quietly off.

## What got added to the book

- [Chapter 01](book/chapter_01.md) — why I'm doing this.
- [Chapter 02](book/chapter_02.md) — first contact.

## Decisions deferred

- Which of the three sub-questions in [02_project_brief.md](../02_project_brief.md) to pursue.
- GitHub setup.

## Status at end of session

Cloud setup working. First LLM run done. Library of `.md` files drafted and re-architected into modular, linked form.

## What's next

Session 2 starts with two inputs from me:
1. Chosen sub-question.
2. GitHub set up via Claude Code.

Then: load first real text, first actual analysis, write Chapter 3 from what happens — not ahead of it.
