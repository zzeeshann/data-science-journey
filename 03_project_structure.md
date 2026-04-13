# 📁 Project Structure

*Folder layout and setup steps. Related: [02_project_brief.md](02_project_brief.md).*

---

## The layout

```
data-science-journey/
│
├── 00_index.md                    ← the map
├── 01_working_agreement.md        ← rules
├── 02_project_brief.md            ← what the project is
├── 03_project_structure.md        ← this file
├── 04_roadmap.md                  ← 6-month plan
├── 05_glossary.md                 ← concept definitions
│
├── sessions/                      ← what we did, session by session
│   └── session_01.md
│
├── book/                          ← personal book, written as we go
│   ├── chapter_01.md
│   └── chapter_02.md
│
├── notebooks/                     ← Colab notebooks (.ipynb)
├── data/
│   ├── raw/                       ← never edit
│   └── processed/                 ← cleaned versions
├── outputs/                       ← charts, tables, findings
│
├── README.md                      ← points to 00_index.md for visitors
├── .gitignore
└── requirements.txt
```

## Why

Each folder has one job:
- **Root `.md` files** — project meta (rules, plan, definitions).
- **`sessions/`** — chronological record of real work.
- **`book/`** — personal narrative.
- **`notebooks/`** — actual analysis code.
- **`data/`** — datasets; `raw/` is sacred and never edited.
- **`outputs/`** — results worth keeping.

## Mac setup

1. Make `data-science-journey/` somewhere memorable.
2. Create the sub-folders above (empty is fine).
3. Drop the `.md` files into their right places.

## GitHub setup

Easiest path: use an AI coding CLI tool like **Claude Code** (or similar tools such as Cursor, Aider, or GitHub Copilot CLI). In terminal, `cd` into the folder and start the tool. Tell it *"read 01_working_agreement.md, then initialise git and push this to a new GitHub repo called data-science-journey."*

Manual path: create a free account at github.com → New repository → clone locally with GitHub Desktop → copy files into the cloned folder → commit → push.

## The `.gitignore`

```
__pycache__/
*.pyc
.ipynb_checkpoints/
data/raw/*
data/processed/*.csv
.DS_Store
*.env
```

## The one rule

**Never edit files in `data/raw/`.** Ever. Read them, transform them in a notebook, save the result to `data/processed/`. This single habit saves you from the most common beginner mistake.
