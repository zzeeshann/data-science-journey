# 🤝 Working Agreement

*How we work. Read this second, after [00_index.md](00_index.md).*
*"The assistant" in this file means whichever AI model I'm working with — Claude, ChatGPT, Gemini, or any other.*

---

## The core rule

**The book is a record of what actually happened, in the order it happened.** Not a lesson plan. Not a tutorial. If a concept wasn't covered in conversation, it does not appear in the book. Future chapters are built from what *just happened*, not from what "should" come next.

## What the user wants

- The **modern 2026 way** — LLMs, agents, tool use, cloud-first. Not the 2018 pandas-for-three-months path.
- To be treated like a **beginner who knows some coding** — real foundations, plain English, no jargon without translation.
- **Confidence from doing**, not from reading. Small real wins, repeated.
- To feel, by the end, that they can walk into a technical room and not fake it.

## What the user does NOT want

- Tutorial-voice, textbook pacing, or surface-level padded answers.
- The assistant deciding what they learned when they didn't.
- Files that contradict each other.
- Over-questioning — make reasonable assumptions and proceed.
- Giant files. Small, single-purpose, linked is the rule.

## How the assistant should behave

- **Think before writing.** Match the output to what actually happened.
- **Be honest and direct.** Push back when the user is wrong. Don't just nod.
- **Present all `.md` files together** after any update, so the user sees the full library.
- **Cut fluff.** Say the real thing.
- **Admit mistakes cleanly** when called out — no excuses, just fix it.
- **Keep files small and linked.** Cross-reference, don't duplicate. Definitions live in [05_glossary.md](05_glossary.md) only.

## The user's setup

- **Laptop:** 2016 MacBook Pro (Intel). Too old for useful local LLM work.
- **Cloud compute:** Google Colab free tier (T4 GPU).
- **Models/data:** Hugging Face.
- **Thinking partner:** whichever LLM the user is using (Claude, ChatGPT, Gemini, etc.).
- **No local Ollama install.** User chose against it with good reason. Don't re-suggest.

## Project status

See [02_project_brief.md](02_project_brief.md) for the project. See `/sessions/` for the latest state of what's been done.

---

## End-of-session ritual

Every session ends with:
1. A new `session_XX.md` file written in `/sessions/`.
2. Book chapter updated or added in `/book/` if relevant.
3. [00_index.md](00_index.md) updated with any new files.
4. This file updated if the working agreement itself evolved.
5. (Optionally) a `git commit` + push.

---

*This file is the source of truth for how the project runs.*
