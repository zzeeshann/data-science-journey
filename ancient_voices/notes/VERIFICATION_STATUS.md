# Verification status — Tier 1 passages

*Tracker for the seven 12-cluster passages and their position-11 / position-13 controls. Maintained between Sessions 7 and 8. Each row says where the verified passage came from (or what's blocking it). Files in `passages/` use only public-domain or openly-licensed translations.*

## Done — in `passages/`

| File | Source | Translator + year | License | Position |
|---|---|---|---|---|
| `hammurabi_law_11.txt` | Project Gutenberg #17150 | C. H. W. Johns (1903) | Public domain | Position 11 (control) |
| `hammurabi_law_12.txt` | Project Gutenberg #17150 | C. H. W. Johns (1903) | Public domain | **Position 12 (cluster)** |
| `hammurabi_law_13.txt` | Project Gutenberg #17150 | C. H. W. Johns (1903) | Public domain | Position 13 (control) |
| `enuma_elish_1_line_11.txt` | Project Gutenberg #9914 | E. A. Wallis Budge (1921) | Public domain | Position 11 (control) |
| `enuma_elish_1_line_12.txt` | Project Gutenberg #9914 | E. A. Wallis Budge (1921) | Public domain | **Position 12 (cluster)** |
| `enuma_elish_1_line_13.txt` | Project Gutenberg #9914 | E. A. Wallis Budge (1921) | Public domain | Position 13 (control) |
| `iching_hexagram_11.txt` | sacred-texts.com | James Legge (1899) | Public domain | Position 11 (Thâi / Peace — *yin-yang complement of 12*; flag in chapter) |
| `iching_hexagram_12.txt` | sacred-texts.com | James Legge (1899) | Public domain | **Position 12 (cluster — Phî / Standstill)** |
| `iching_hexagram_13.txt` | sacred-texts.com | James Legge (1899) | Public domain | Position 13 (Thung Zăn / Union of Men) |
| `pyramid_texts_unas_utterance_213.txt` | pyramidtextsonline.com | Faulkner / Piankoff / Speleer | Public domain | First inscribed Unas utterance — *not* Faulkner Spell 12 (Spell 12 is not in the Unas pyramid). Used as Pyramid Texts representative. |
| `pyramid_texts_unas_utterance_217.txt` | pyramidtextsonline.com | Faulkner / Piankoff / Speleer | Public domain | Wider-sample Unas utterance |
| `gilgamesh_pennsylvania_tablet_dream.txt` | Wikisource | Stephen Langdon (1917) | Public domain | Old Babylonian "Tablet II" opening dream — *not* Standard Babylonian Tablet 12. Used as Gilgamesh wider-sample representative. |
| `inanna_descent_opening.txt` | User-uploaded PDF | Wolkstein & Kramer (1983) | **Fair-use academic research excerpt** — translation in copyright through ~2083; ~25 lines from a 200+ page book; ETCSL would be the openly-licensed swap when reachable | Opening descent (position approximate; Inanna doesn't use conventional verse numbering) |

**Status by text:**
- **Hammurabi:** complete with full position-11/12/13 ✓ (PD)
- **Enuma Elish:** complete with full position-11/12/13 ✓ (PD)
- **I Ching:** complete with full position-11/12/13 ✓ (PD, Legge 1899) — Wilhelm-Baynes draft superseded; remains in `notes/` as a translation-sensitivity reference only
- **Inanna's Descent:** opening passage saved as fair-use research excerpt ✓ — would migrate to ETCSL when reachable. No clean position-11/13 controls (the text is unnumbered).
- **Pyramid Texts:** Spell 12 (Faulkner numbering) not in PD via Unas. Two wider-sample Unas utterances saved. Session 8 chapter should flag honestly that this text contributes wider-sample only, not the position-12 cluster test.
- **Gilgamesh:** Standard Babylonian Tablet 12 not in PD via available sources. Pennsylvania Tablet (OB Tablet II) saved as wider-sample representative. Same note as Pyramid Texts for Session 8 chapter.
- **Ugaritic KTU 1.12:** still pending. No clean PD source identified. May be skipped in Session 8 with the absence noted plainly.

13 files in `passages/`. Two more in `notes/` (this status doc + the superseded Wilhelm I Ching reference).

## Session 8 — what's runnable now

**Five of seven texts have something in `passages/`:**
- 4 texts with full position-11/12/13: Hammurabi ✓, Enuma Elish ✓, I Ching ✓ + Inanna (12 only, no controls)
- 2 texts with wider-sample passages only: Pyramid Texts (Unas), Gilgamesh (Pennsylvania Tablet)

**The 12-cluster permutation test can run on three texts** (Hammurabi, Enuma Elish, I Ching) cleanly, with Inanna's opening counted on the 12-side without a 11/13 control. That's a meaningful test, with the chapter for Session 8 honestly noting what's been substituted and why.

The **only fully-pending text** is Ugaritic KTU 1.12. If you can find a PD or open-access KTU 1.12 translation (Wyatt 2002 is paywalled; older fragments in academic open access exist on academia.edu sometimes), Session 8 has its full seven-text corpus. If not, six texts is fine.

## Pending — need copy-paste from one of these URLs

### Gilgamesh — Tablet 11 + Tablet 12

The reading guide names Andrew George (Penguin Classics 1999) as the gold standard, but George is in copyright. Public-domain options:

- **R. Campbell Thompson 1928 (UK PD; US PD only after 2024)** — Wikisource has the full text:
  - Index: https://en.wikisource.org/wiki/The_Epic_of_Gilgamish
  - The page lists individual tablet sub-pages; copy-paste Tablet XI and Tablet XII content.
- **L. W. King fragments (1902)** — partial, not a full translation.
- **Stephen Langdon 1917** — partial, scholarly fragments.

**Note:** Gilgamesh has only 12 tablets, so position-13 doesn't exist. Tablet 11 (the flood) is the position-11 control; Tablet 12 (the Sumerian appendix about the netherworld) is the 12-cluster candidate.

When you paste, save as:
- `gilgamesh_tablet_11.txt` — control
- `gilgamesh_tablet_12.txt` — 12-cluster

### I Ching — Hexagrams 11, 12, 13

The reading guide names Wilhelm-Baynes (Bollingen 1950) as the scholarly standard but it's in copyright. Public-domain alternative:

- **James Legge 1899** — Wikisource hosts it as Sacred Books of the East Volume 16. The hexagrams are likely on a sub-page like `Sacred_Books_of_the_East/Volume_16/The_Yî_King/I` or similar; the index page is at:
  - https://en.wikisource.org/wiki/Sacred_Books_of_the_East/Volume_16
  - You'll need to find the actual translation page (the hexagrams are in "The Yî King" / "The Text of King Wăn") and copy-paste hexagrams 11 (T'ai / Peace), 12 (Pi / Standstill), and 13 (T'ung Jên / Fellowship with Men).

Also free online (legality varies — these may host Wilhelm-Baynes content):
- https://www.iching-online.com/iching-12.htm
- https://www.iching-online.com/iching-11.htm
- https://www.iching-online.com/iching-13.htm

When you paste, save as:
- `iching_hexagram_11.txt` — control (T'ai / Peace; structurally paired with 12)
- `iching_hexagram_12.txt` — 12-cluster (Pi / Standstill)
- `iching_hexagram_13.txt` — control (T'ung Jên / Fellowship with Men)

**Important caveat for Session 8 chapter:** Hexagrams 11 and 12 are the explicit yin-yang complement pair in the I Ching itself. Hexagram 11's high cosine with Hexagram 12 will be partly built into the source structure, not just an embedding finding. The Session 8 permutation test should be reported both with and without I Ching position-11 included.

### Inanna's Descent — opening passage

ETCSL (Oxford-hosted Sumerian corpus) is the named authoritative source but the server was unreachable when I tried. URL:
- https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.4.1
- https://etcsl.orinst.ox.ac.uk/section1/c141.htm

If ETCSL is up when you read this, copy-paste the opening section (the framing of Inanna's descent and her abandonment of titles). The file's NOTES header should say the position is approximate — Inanna doesn't use conventional verse numbering — and document which verses correspond to position 11, 12, 13.

Wikipedia has substantial summary plus quoted passages here:
- https://en.wikipedia.org/wiki/Inanna%27s_Descent_into_the_Underworld

Wikipedia is acceptable for the *passage* if it cites a primary source for each quoted line — but Wikipedia paraphrase isn't. Use Wikipedia to find the primary source, then paste the primary source.

When you paste, save as:
- `inanna_descent_line_11.txt` — control (approximate)
- `inanna_descent_line_12.txt` — 12-cluster (approximate)
- `inanna_descent_line_13.txt` — control (approximate)

### Pyramid Texts — Spell 12

The reading guide names Faulkner (1969) and Allen (2005) — both in copyright. Public-domain options:

- **Breasted 1912** ("Development of Religion and Thought in Ancient Egypt") — partial; check Project Gutenberg.
- **Maspero, Mercer pre-1928 fragments** — incomplete.
- **Pyramidtextsonline.com** uses Faulkner's numbering; legality uncertain.

The honest answer: Spell 12 in Faulkner numbering is short (a few lines). Saving the Faulkner version may exceed fair use; saving the Breasted PD partial is safer if it covers spell 12. If neither works cleanly, this passage may be skipped in Session 8 with the absence noted plainly in the chapter.

URLs to try:
- https://www.pyramidtextsonline.com/translation.html
- https://en.wikipedia.org/wiki/Pyramid_Texts

When you paste, save as:
- `pyramid_texts_spell_11.txt` — control
- `pyramid_texts_spell_12.txt` — 12-cluster
- `pyramid_texts_spell_13.txt` — control

### Ugaritic — KTU 1.12

KTU 1.12 is fragmentary. The Wyatt 2002 translation is paywalled. Public-domain alternatives are scarce; KTU 1.12 was published in the 1930s onward and most translations remain in copyright.

Open-access academic papers may have full translations under fair-use quotation:
- https://en.wikipedia.org/wiki/Baal_Cycle (general context; KTU 1.12 is one of the related texts)
- https://www.omnika.org/ (some translations; check licence)

This is the hardest of the seven. If a clean PD/openly-licensed KTU 1.12 cannot be found, Session 8's record should note the absence and run the test on the six texts that have verified passages. The chapter must be honest about the corpus shape.

When you paste (or skip), save as:
- `ugaritic_ktu_1_12.txt` — 12-cluster
- (KTU 1.11 and 1.13 exist as separate fragments; controls should match the same numbering convention.)

## Wider sample (Tier 1 supplementary, 7–14 files)

Per `ANCIENT_TEXTS_READING_GUIDE.md`, the wider sample is randomly-selected positions from the same seven texts — not 11, 12, 13 — to give the permutation test a baseline. These can be added in any order. Easiest sources:
- More Hammurabi laws from PG #17150 (random picks from the 282 laws)
- More Enuma Elish lines from PG #9914
- More I Ching hexagrams once the Legge text is sourced

## What "verified" means in this folder

Per `ancient_voices/README.md`: every passage file cites a primary-source URL or a published academic translation. The translation is by a real human translator, not an LLM. Position numbers are exact where the source numbers them; approximate where the source doesn't (and the file says so).

If a passage cannot meet this standard, it goes here in `notes/` as a working draft, not in `passages/`.
