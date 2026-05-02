# `ancient_voices/passages/` — format spec

Each file is one passage, ready to be loaded as an embedding input. The header carries the citation; the body is the passage text. Plain `.txt`. No markdown.

## Filename convention

```
{text_short_name}_{position_kind}_{position_number}.txt
```

Examples:
- `gilgamesh_tablet_12.txt`
- `gilgamesh_tablet_11.txt`
- `enuma_elish_1_line_12.txt`
- `hammurabi_law_12.txt`
- `inanna_descent_line_12.txt`
- `iching_hexagram_12.txt`
- `pyramid_texts_spell_12.txt`
- `ugaritic_ktu_1_12.txt`

Lowercase, underscore-separated, no spaces, no diacritics. Position kind is one of: `tablet`, `line`, `law`, `hexagram`, `spell`, `ktu` (or another short token if a new text is added).

## File body — header + passage

The first lines are a citation header, in the format below. Then a blank line. Then the passage text. Nothing else.

```
TEXT: Epic of Gilgamesh
POSITION: Tablet 12
TRANSLATION: Andrew George (Penguin Classics, 1999)
SOURCE_URL: https://www.sacred-texts.com/ane/eog/eog31.htm
LANGUAGE: Akkadian (translated)
DATE: ~1200 BCE (Standard Babylonian version)
NOTES: Tablet 12 is structurally distinct from Tablets 1-11 — appended Sumerian source. Discussed in chapter introduction of George (1999).

[passage text begins here]
```

Required header keys: `TEXT`, `POSITION`, `TRANSLATION`, `SOURCE_URL`, `LANGUAGE`, `DATE`. Optional: `NOTES`. Header values do not span multiple lines — keep them one-line. If a value would be long, put it in `NOTES`.

## What counts as "the passage"

For position-defined units (a tablet, a hexagram, a law, a spell): the full unit. Not an extract from it. The whole tablet, the whole hexagram, the whole law as written.

For line-defined positions: the full line and immediate surrounding context, typically 5–10 lines. The header `POSITION` field names the central line; the passage includes enough context for a human reader (and the embedding model) to understand it. Mark the central line in `NOTES` if needed (e.g. `NOTES: Line 12 begins at the third line of this extract.`).

For fragmentary texts: the legible portion plus a brief note in `NOTES` about reconstruction. Do not invent text to fill gaps. Use `[…]` for damaged sections in the passage body.

## What does not go in `passages/`

- LLM-generated paraphrases. Only verified human translations.
- Multiple translations of the same passage in one file. Pick one authoritative translation; if comparative work is needed, add additional files with `_alt1`, `_alt2` suffixes.
- Headers in any format other than the one above.
- Files without a `SOURCE_URL`. Even an academic-translation file should cite the digital edition or repository it was sourced from.

## What if the verified translation contradicts what Claude said in earlier conversations

Claude's earlier descriptions are working hypotheses, not data. The verified translation is the data. If the actual passage at position 12 is different from what was described in the bundle, Session 8's procedure handles that automatically — it embeds whatever is in the file. The bundle's description of the passage is replaced by the file. Note the correction in the relevant session record.
