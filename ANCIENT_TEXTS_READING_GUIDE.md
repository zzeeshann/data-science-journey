# Ancient Texts — Reading Guide

*Working document for the user's parallel reading between Sessions 7 and 8 (and beyond). Lives in the project root for now; can move to `ancient_voices/` once it stabilises. Read alongside `ancient_voices/passages/README.md` for the file-format spec.*

---

## What this is for

Session 8 needs verified passage files in `ancient_voices/passages/`. This guide is the order to read in, the editions to trust, and the format to extract into. The reading is yours; this document is a map.

The minimum viable Session 8 corpus is **21 files** — the seven "12-cluster" passages plus the position-11/13 controls (where they exist), plus 7–14 wider-sample passages. That's the work.

If reading goes deeper, that's better. The project has space for it. But Session 8 doesn't wait on Tier 2 or Tier 3.

---

## Tier 1 — Verification (must-have before Session 8)

### What you're verifying

For each of the seven texts: is the passage at position 12 actually about what we think it is? What are the *exact* words of the most authoritative translation? What does the line/spell/law/tablet number resolve to in the standard edition? And what does the passage at position 11 and position 13 from the same text say?

The whole investigation pivots on this work being honest. If the passage at Gilgamesh Tablet 12 is something other than what the bundle described, the cluster shrinks. If position 13 in the I Ching contains something thematically identical to position 12, the cluster's distinctiveness weakens. Either is a real finding. The point of verification is to find out.

### The seven texts, with editions to trust

**Epic of Gilgamesh — Tablet 12.** Penguin Classics edition, Andrew George (1999) is the gold-standard scholarly translation. Free online: sacred-texts.com (older Sandars / Heidel). For verification: cross-check the George translation if possible (library, Internet Archive). Note: Tablet 12 is structurally distinct from Tablets 1–11 — it's a Sumerian source appended later. George's introduction discusses why. This is relevant for the chapter.

**Enuma Elish — Tablet 1, line 12.** Stephanie Dalley, *Myths from Mesopotamia* (Oxford World's Classics, 2000). Free online: sacred-texts.com (Heidel) and worldhistory.org. The line numbering varies slightly across editions — note which one you're using.

**Code of Hammurabi — Law 12.** ehammurabi.org has the standard 282-law numbering. Cross-check with Martha Roth, *Law Collections from Mesopotamia and Asia Minor* (1995, 2nd ed. 1997) if you can find it. Laws 11 and 13 also need to be extracted as controls.

**Descent of Inanna — opening passage.** ETCSL (etcsl.orinst.ox.ac.uk) is the Oxford-hosted authoritative translation. **Important:** Inanna doesn't use line numbers like a numbered scripture. The "~line 12" reference is approximate. Read the opening section (the framing of Inanna's descent and her abandonment of titles), pick the verse that corresponds best, and document the approximation in the file's `NOTES` header. This honest acknowledgment makes the verification cleaner, not weaker.

**I Ching — Hexagram 12 (Pi/否).** Wilhelm-Baynes translation (Bollingen / Princeton) is the scholarly standard in English. Free online: iching-online.com. Hexagrams 11 (T'ai/泰, "Peace") and 13 (T'ung Jên/同人, "Fellowship with Men") are the controls — note that the I Ching is the only one of the seven where the position-11 entry is also thematically loaded (Peace ↔ Standstill is a known yin-yang pairing). This complicates the falsification test in an interesting way; flag it for Chapter 8.

**Pyramid Texts — Spell 12.** Pyramidtextsonline.com uses Faulkner's standard numbering. Cross-check with Allen, *The Ancient Egyptian Pyramid Texts* (2nd ed. 2015). Spells 11 and 13 are short — extract both.

**Ugaritic — KTU 1.12.** Omnika.org has translations. Cross-check with N. Wyatt, *Religious Texts from Ugarit* (2002) if available. KTU 1.12 is fragmentary — the file's `NOTES` header must say so. Where text is reconstructed by a scholar, the reconstruction is what we embed (not Claude's guess at what was missing).

### What you produce

For each of the seven 12-passages and each of the position-11 / position-13 controls (where they exist), one `.txt` file in `ancient_voices/passages/` matching the format in `ancient_voices/passages/README.md`. Header with citation. Body with passage. Nothing else.

Approximate file count: 7 (positions 12) + ~12 controls (positions 11 and 13 where they exist; Gilgamesh has no Tablet 13) = **~19 files** to start. Add 7–14 wider-sample passages (random positions from the same texts, not 11/12/13) and you're at the minimum Session 8 corpus.

### How to handle gaps

- **A passage you can't find a good translation of:** put a placeholder file in `ancient_voices/notes/` describing the difficulty, and skip that text in Session 8. Document the absence in Session 8's record.
- **A passage that contradicts the bundle's description:** the verified text wins. Update the file. Note the correction in Session 8's record. The bundle was a starting hypothesis, not data.
- **A passage where the position number is approximate:** say so in `NOTES`. Don't pretend a precise number exists when it doesn't.

---

## Tier 2 — Wider context (optional but recommended; feeds Sessions 9–12)

If you have time and energy, the project gets stronger if the corpus has more depth than the 12-cluster + controls. These are passages worth reading and extracting at the same standard:

**Full primary texts to consider for partial extraction:**
- *Descent of Inanna* — full text (ETCSL). Useful for the descent-as-universal-structure question that the 12-cluster touches but doesn't exhaust.
- *Gilgamesh Tablet 11* — the flood narrative. The clearest direct parallel to Genesis. Useful for the cross-cultural memory question, even if the project doesn't formally test it.
- *Pyramid Texts spells 1–30* — broader sample of Egyptian funerary thinking. Provides a baseline for "what Egyptian afterlife writing looks like" that makes Spell 12 more interpretable.
- *Hammurabi laws 1–30* — broader baseline. Lets you see whether Law 12 actually stands out among its neighbours or whether the surrounding laws have similar themes.
- *Enuma Elish Tablet 1, full* — the creation account in full. Gives Line 12 its proper context.
- *I Ching hexagrams 1–30* — half the book, roughly. Useful if you want to ask whether Hexagram 12's "standstill" theme has structural neighbours or sits alone.

**Time investment:** Tier 2 is many hours of reading. Treat it as background rather than blocking. Session 8 doesn't need it. Session 11 (topic modelling on a multi-text corpus) is where Tier 2 reading would actually flow into analytics — by then, having extracted ~50 passages across the seven texts gives BERTopic enough material to find clusters within ancient writing itself.

---

## Tier 3 — Interpretive lenses (optional, with caution)

The project already has two interpretive lenses: *Thinking in Wholes* (2026) and the Ackoff lecture. That's a coherent modern-systems-thinking frame. Adding more interpretive theorists is tempting, but the project's working agreement is sharp on this: *"We are not doing original sociology — we are using existing data competently and asking sharp questions."*

If you want a lens for the ancient material:

- **Mircea Eliade — *The Sacred and the Profane*.** Threshold and liminality concepts. Most directly relevant to the 12-cluster's threshold theme. If any Tier 3 reading is worth doing, this is probably it.
- **Karl Jaspers — *The Origin and Goal of History* (Axial Age).** The 8th–3rd century BCE as a period of simultaneous philosophical/religious breakthrough across multiple unconnected civilisations. Relevant if you want to ask why so many of the texts emerged from this window.
- **Joseph Campbell — *The Hero with a Thousand Faces*.** Comparative monomyth. **Use with caution** — Campbell's approach to "universal patterns" is exactly the kind of charitable-reading-across-cultures the project's standards rule out as primary evidence. Useful for orientation, dangerous as analytical input.
- **Carl Jung — archetypes literature.** Same caution as Campbell. Universal-archetype claims are interpretive, not empirical, and the project's standard is empirical.
- **Julian Jaynes — *The Origin of Consciousness in the Breakdown of the Bicameral Mind*.** Specific to changes in self-reference language in ancient texts (especially the Iliad-vs-Odyssey shift). Speculative, contested, fascinating. If you read it, save the reading notes; the embedding pipeline can directly test some of his claims about pronoun/agency language across texts.

**Standing rule:** if a Tier 3 reading produces a sharp testable hypothesis, treat it like *Thinking in Wholes*. Save the source to `data/raw/`, add a glossary entry, and let it function as a lens — not as evidence in itself. The book *records what happened in the data*, not what theorists predicted would happen.

---

## How reading flows into the project

Between Sessions 7 and 8: Tier 1 verification. Produces ~21 passage files. Hard requirement for Session 8.

Between Sessions 8 and 9: react to whatever Session 8 found. If the 12-cluster survived, expand Tier 2 reading to deepen the corpus for Sessions 9–12. If it didn't, the corpus is still useful — sessions 9–12 might still find something worth pulling on.

Between Sessions 9 and 12: Tier 2 reading at your own pace. Each session can pull from whatever has been verified.

After Session 12 synthesis: Tier 3 reading is most useful here, when the data has spoken and you're trying to interpret what it said. Reading Eliade with Session 8's results in front of you is more useful than reading Eliade before knowing what the data shows.

---

## A note on translations

Different translations of the same ancient passage produce different embeddings. This is real. A dense, archaic translation (King James-style for Hebrew, Sandars for Gilgamesh) sits in a different vector neighbourhood than a modern colloquial one (NRSV, Mitchell). The project's choice is to use **scholarly editions, consistently** — Penguin / Oxford World's Classics / academic standards — rather than mixing styles.

If two scholarly translations of the same passage diverge sharply, Session 8 can embed both (`gilgamesh_tablet_12_alt1.txt` etc.) and report whether they end up in the same neighbourhood. A divergence in cosine similarity between two translations of "the same" passage is itself an interesting finding: it tells us how much of the cross-cultural pattern is in the language and how much is in the translator's voice.

This is a Tier 2 concern, not a Tier 1 blocker. Pick one good translation each, get to Session 8.

---

*Keep this file open during reading. Mark passages as verified by adding the corresponding `.txt` file to `ancient_voices/passages/`. Session 8 reads whatever is there.*
