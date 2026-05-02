# Start Session 13 — Book Audit (the 14-year-old readability pass)

*Drafted by Claude Code at user's request, May 2 2026, after Sessions 7–9 surfaced a real readability gap (numbers landing in chapters without scale-anchoring; terms used without glossary entries). Read this at the start of Session 13 and follow it. If anything here conflicts with `01_working_agreement.md` or `CLAUDE.md`, those win.*

---

## When to run this

After Session 12 (the Phase 3 synthesis) closes. By that point all twelve chapters will exist in draft, the full investigation arc will be visible, and a single comprehensive readability pass catches more than three smaller passes would.

If you decide to run an interim pass earlier (Chapters 1–9 only, before Session 10 starts), the procedure below still applies — just scope it to the existing chapters and skip the parts about Sessions 10–12.

## Goal

**Make the book readable by a 14-year-old.** Not a rewrite. A pass-through that catches every number, every term, every implicit assumption a beginner wouldn't follow, and patches them in place. Plus four new files that capture lessons-learned, an executive summary, and improvement questions.

The threshold: if a 14-year-old (smart, curious, no statistics or NLP background) reads a chapter cold and gets stuck on a sentence, the chapter has a gap the audit needs to close.

## What this session is NOT

- Not a content rewrite. Findings stay. Numbers stay. The voice stays.
- Not a re-investigation. No new data, no new tests, no new corpus.
- Not "dumbing down." A 14-year-old isn't dumb — just has less context.
- Not padding. One short scale-anchor sentence is enough; don't lecture.
- Not adding code comments inside code blocks. New terms go in the glossary; new explanations go in prose.

## The reading bar — concrete examples

These are the kinds of gaps the audit looks for. Each is from chapters already written.

**Numbers without scale anchoring.** Chapter 7 says *"Top Ackoff↔TinW pair hits cosine 0.80… The next four pairs all sit between 0.69 and 0.78."* A 14-year-old reading that has no idea whether 0.80 is high, low, or normal. The fix is one sentence: *"For context, two paragraphs paraphrasing each other typically land between 0.7 and 0.8; two unrelated paragraphs land near 0.05–0.10."* That sentence belongs the first time a cosine is quoted in any chapter.

**Terms used before defined.** "Embedding," "cosine similarity," and "sentence-transformer" are in the glossary, but "paired-difference," "bootstrap CI," "sign-flip permutation," "register," "subreddit," "Pushshift" all appear in chapters without a glossary anchor. Either define them inline (one short clause) or add a glossary entry and link to it.

**Implicit assumptions.** Chapter 5 mentions "the residual" and links to the glossary — good. But it assumes the reader understands what *kind* of variable a residual is. A 14-year-old who clicks through to the glossary entry should find an explanation that doesn't itself require regression knowledge.

**Voice drift.** Chapters 1–6 were drafted at different times by different model versions. Chapter 6 had to be audited (Session 6 found the fabricated quote). Chapters 7–9 are recent Opus drafts with sustained prose. The audit should flag any chapter that sounds noticeably different from the others, and patch the worst dissonance.

## The procedure

### Step 1 — read every chapter cold

For each chapter from Chapter 1 onward, read it as if you'd never seen the project. As you read, keep a running list of:

- **Numbers without scale anchoring.** Every cosine, correlation, p-value, percentile, percentage, n_pairs count that appears without context for what the value means.
- **Terms not in the glossary.** Every technical word you'd have to look up.
- **Implicit assumptions.** Every "obviously" or "of course" or unstated step.
- **Sentences that confused you on first read.** Trust the reading-from-cold reaction; that's what a 14-year-old will hit.

Save the list as `notes/book_audit_findings.md` (create the `notes/` folder if it doesn't exist). One section per chapter. Concrete line numbers and sentences.

### Step 2 — apply the patches

Work chapter by chapter, in order. For each chapter:

1. **Add scale-anchor sentences** where a number first appears that needs context. One short sentence. Don't pad — just enough that a beginner can locate the number on a mental scale.
2. **Add or update glossary entries** for every new term flagged. Cross-link from the chapter to the glossary entry on first use of the term. Keep entries short — 3–6 sentences each, plus the *"First used in [session_NN.md]"* line.
3. **Patch implicit assumptions** with one-clause explanations inline. If the explanation is longer than one sentence, it probably belongs in the glossary.
4. **Smooth voice drift** if any chapter sounds jarringly different. This is a light touch — don't rewrite, just adjust opening or closing sentences.

After each chapter is patched, re-read it cold one more time. If you're still confused, the patch isn't done.

### Step 3 — produce the four new files

These are the audit's outputs beyond the inline patches.

**`mistakes_made.md`** at repo root. The project's mistakes-and-corrections record. One section per mistake. For each: what happened, where the mistake was, how it was caught, what verification habit fixed it, what habit was added to standing process to prevent recurrence. Sources to mine:
- Session 5 — chart-fix episode (commits `68230bf` → `70d49f2`).
- Session 6 — fabricated *Thinking in Wholes* quote in Chapter 6, caught by Opus 4.7 audit.
- Session 8 — catalogue-vs-position discovery (KTU is a museum index, not a content position) caught between sessions during verification reading.
- Session 9 — wholeness-register interpretation falsified by Reddit's negative paired-difference. (This isn't a mistake exactly — it's a pre-registered prediction that the data rejected. But it's the same discipline: write the prediction down, accept the data, file the rejected interpretation.)

This file is one of the most useful things in the repo. It demonstrates the project's verify-don't-trust discipline working in practice.

**`summary_for_a_reader.md`** at repo root. ~500 words. Self-contained executive summary for someone who has not read the book. Structure:
- The starting question (one paragraph).
- The hook the investigation now orbits — the residual fall across 141 countries (one paragraph).
- What the investigation has tried (one paragraph: country-scale data; embeddings; ancient texts; Reddit; WVS; topic modelling).
- What it has found and what it has ruled out (one paragraph).
- What it has not yet found (one paragraph: the residual is still unnamed).
- One sentence pointing readers at the chapters or sessions for detail.

Voice: same as the chapters. No lecture, no marketing. The summary you'd hand someone asking "what is this project about?"

**`improvements.md`** at repo root. ~10 numbered points. What you'd do differently if starting over. Each point: 2–4 sentences. Things to consider:
- Pre-registration discipline — was every test pre-registered? Were any post-hoc rationalisations slipped in?
- Corpus choice — would different corpora answer the question better?
- Model choice — `all-MiniLM-L6-v2` was the default; would a heavier model change conclusions?
- Sample sizes — places where small-n weakened a conclusion.
- Methodological assumptions that didn't survive (the catalogue-vs-position discovery is the cleanest example).
- Anything you noticed reading the chapters that you wished you'd thought of earlier.

This isn't a self-criticism document. It's a "what I'd put in the next investigation's planning brief" document.

**`reader_glossary_audit.md`** at repo root. A list of every new glossary entry the audit added, with a note on which chapter triggered it and why. Stays as a working doc. Useful for future audits.

### Step 4 — verify

Standard "verify, don't trust" pass:

```bash
# Every glossary anchor referenced from any chapter resolves to a real heading
grep -nE "05_glossary\.md#" book/chapter_*.md | awk -F'#' '{print $2}' | sort -u
grep -nE "^## " 05_glossary.md | sed 's/^## //' | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sort -u

# Every chapter image referenced exists
grep -nE "!\[.*\]\(images/" book/chapter_*.md | awk -F'(' '{print $2}' | awk -F')' '{print $1}'
ls book/images/

# No fabricated book quotes (citation grep — the Session 6 precedent)
grep -inE "the book (says|argues|calls|claims|describes|writes)" book/chapter_*.md

# Number consistency: any number that appears in a chapter should also appear (matching) in a session record
# (manual spot-check; pick five numbers per chapter and verify)
```

### Step 5 — commit + push

Multi-paragraph commit per `CLAUDE.md` HEREDOC pattern. Title line: *"Book audit: 14-year-old readability pass"*. Two paragraphs of context. Bulleted what-changed list (chapters patched, glossary entries added, four new files created). Co-Authored-By line.

## Things to avoid

- **Padding.** A scale-anchor sentence is one sentence. A glossary entry is 3–6 sentences. Don't write paragraphs of explanation when a clause will do.
- **Rewriting voice.** The chapters have a voice that built up over 9+ sessions. Don't smooth it into something more "professional"; the directness is the point.
- **Defining trivial things.** "GDP" doesn't need a glossary entry. "Bootstrap" probably does. Use judgement.
- **Adding marketing or apologies.** No "as we'll see in the next chapter" or "I'm not an expert but." The book stands as a record.
- **Fixing things that aren't broken.** If a sentence is fine for a 14-year-old, leave it.
- **Comparative-style summaries** ("this means that…"). Most readers can carry the implication if the prose is clean.

## Status going in

When this session runs, the following will be true:
- All chapters in `book/` exist in draft form.
- Glossary in `05_glossary.md` has all terms used through whichever sessions have run.
- Index in `00_index.md` reflects the full session count.
- `mistakes_made.md`, `summary_for_a_reader.md`, `improvements.md`, `reader_glossary_audit.md` do not yet exist.
- The investigation is paused after the synthesis; this audit pass is the last thing before any Phase 4 work.

## Verification habits this session adds to standing process

If anything is found that the project should have caught earlier, fold it into the standing verification list in `CLAUDE.md`. The Session 6 audit added three habits ("verify chart visually", "citation grep before commit", "model identity in receipts"). This audit might add habits like "scale-anchor every number on first use," "glossary anchor every technical term on first use," "voice consistency check across recently-edited chapters."
