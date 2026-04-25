# 🌍 Research Plan — The Wholeness Investigation

*Sub-question 2, sharpened. A multi-session investigation inspired by Thinking in Wholes (2026).*

**Status:** Plan drafted at end of Session 3. Sessions 4 onwards execute it.
**Will take:** 6-10 sessions, honestly. Possibly more.

---

## The sharpened question

Original sub-question 2: *How has the language of consciousness shifted from religious to neuroscientific over the last 200 years?*

Sharpened version, inspired by *Thinking in Wholes*: **Is the worldview shift the book describes — from machine-thinking (parts, growth, optimisation, separation) to systems-thinking (wholes, development, connection, meaning) — visible in real data on how humans and societies are doing?**

We are no longer just measuring how scientists write. We are measuring how humans live, what they value, what's working and what isn't, across countries and decades — and asking whether the systems-vs-machine framing actually explains what we see.

## The four hypotheses we will test

The book makes specific, testable claims. We will test them.

**H1 — Growth and development have decoupled.** Countries that grew fastest economically did not become happiest, healthiest, or most connected. Some countries developed (became more capable, more connected, higher quality of life) without growing. Others grew without developing.

**H2 — Connection predicts wellbeing better than wealth.** Across countries and individuals, the strength of social bonds (trust, family, community, friendship) predicts life satisfaction more strongly than income, GDP, or material standard of living.

**H3 — The language of wholeness is rising in modern writing.** In the last 20 years, the language of connection, system, ecosystem, interdependence, meaning, purpose has become more common in public discourse. The language of pure mechanism, optimisation, individual achievement is plateauing or declining.

**H4 — Cultures vary systematically.** Some cultures (regions, language groups) describe consciousness, meaning, and the self in more "wholeness" terms; others in more "machine" terms. This varies measurably and connects to wellbeing outcomes.

These four hypotheses give the project a spine. Every session contributes to one or more of them.

## The data we will use

All free, all public.

**Country-scale wellbeing and development data:**
- World Happiness Report (Kaggle / Our World in Data) — ~150 countries × 10+ years × happiness, social support, freedom, generosity, trust, GDP per capita.
- UN Human Development Index — ~190 countries × 30 years × HDI components.
- Our World in Data — life expectancy, mental health, loneliness, social trust, inequality.
- World Bank Open Data — GDP, income inequality (Gini), education.
- World Values Survey — ~100 countries × 40 years × hundreds of values questions.

**Text data at scale (Hugging Face):**
- Reddit corpora — r/Meditation, r/NDE, r/decidingtobebetter, r/loneliness, r/Psychonaut. Millions of posts, modern, lay-language.
- News datasets — multi-decade headline and article corpora across countries.
- Wikipedia article corpora — for definitional and cultural reference.
- Project Gutenberg — for historical depth (William James already in repo).

**The book itself:**
- *Thinking in Wholes* (2026) — saved to `/data/raw/`. Functions as the **theoretical lens** that supplies the categories we measure (wholeness, connection, development, system) — not as a data point in the comparison.

## The Hugging Face models we will use

Each session introduces one new tool from the modern AI toolkit. By the end you will have used:

- **Sentence-transformers** (e.g. `all-MiniLM-L6-v2`) — turn text into vectors so we can measure semantic similarity. Foundation of all modern AI text work.
- **Emotion classifier** (e.g. `j-hartmann/emotion-english-distilroberta-base`) — measure emotional content of text.
- **Zero-shot classifier** (e.g. `facebook/bart-large-mnli`) — categorise text against a list of categories you define, without training.
- **A small LLM** (e.g. Llama 3.2 1B, Qwen 2.5 1.5B) — for theme extraction, summarisation, structured output. Used with proper prompt engineering.
- **Topic modelling** (BERTopic) — find the actual topics inside a corpus without telling it what to look for.

## The session plan

Each session has one clear job. The book chapter and session record after each one becomes part of the long story.

### Session 4 — Country-scale wellbeing baseline
**Job:** Load the World Happiness Report data. Build a country-by-country, year-by-year picture of happiness, social support, GDP, freedom, trust. Make the first cross-country comparison chart. Begin testing **H1** (growth ≠ development) and **H2** (connection > wealth).
**New skill:** loading structured tabular data; basic correlation; world-level visualisation.
**Output:** chart of GDP-per-capita vs happiness, with outliers identified by name. First "wholeness" finding: which countries have decoupled growth from wellbeing, in which direction?

### Session 5 — The development-vs-growth decoupling
**Job:** Combine HDI with GDP across 30 years. Identify countries that developed without growing, and those that grew without developing. The book's central claim, made empirical.
**New skill:** time-series data; rate-of-change calculations; merging datasets on country codes.
**Output:** table and chart of the four quadrants — high growth/high development, high growth/low development, etc. Which countries are where, and what changed over 30 years.

### Session 6 — Embeddings: first encounter
**Job:** Use sentence-transformers to turn text into numbers that represent meaning. Apply to chapters of *Thinking in Wholes*, paragraphs of James, a sample of Reddit r/Meditation posts. See which texts are semantically close to each other and why.
**New skill:** what an embedding is; loading a HF model; cosine similarity; the first "the model found something I didn't tell it to look for" moment.
**Output:** similarity matrix; surprising matches and surprising mismatches written up honestly.

### Session 7 — Mapping the language of wholeness across Reddit
**Job:** Pull a large corpus from r/decidingtobebetter or r/Meditation (or both). Use zero-shot classification to label each post on dimensions: connection, isolation, growth-language, systems-language, meaning, purpose, mechanism. Quantify the language of wholeness in modern lay writing. First test of **H3**.
**New skill:** zero-shot classification; large-corpus processing on Colab; dealing with messy social text.
**Output:** distribution chart — what % of posts in each subreddit lean wholeness vs machine. Sample passages for each.

### Session 8 — Cross-cultural values via World Values Survey
**Job:** Load WVS data. Identify which countries cluster on "wholeness" values (trust in others, sense of community, meaning, traditional bonds) vs "machine" values (individual achievement, material success, optimisation). Cross-reference with happiness data. Test **H4**.
**New skill:** cluster analysis; categorical data; large multi-country surveys.
**Output:** map or chart of "wholeness clusters" of countries. Honest discussion of what this does and doesn't show.

### Session 9 — Topic modelling: what the world is actually saying
**Job:** Use BERTopic on a multi-year news or text corpus. Let the model find topics without us telling it what to look for. See whether the language of connection, system, wholeness has actually risen over time in public discourse.
**New skill:** unsupervised topic modelling; reading model output sceptically.
**Output:** topic trends over time; honest discussion of whether the H3 prediction holds.

### Session 10 — Synthesis: the wholeness investigation
**Job:** Pull every finding into one piece of writing. State which hypotheses survived, which didn't, and what the data actually showed. The book's biggest chapter so far.
**New skill:** putting research together. Writing a real argument backed by your own work.
**Output:** chapter, possibly multi-part, that's the strongest thing in the book so far. Possibly the whole project's first publishable artefact.

## What we are NOT doing

To stay honest:

- We are not proving or disproving the book. We are testing whether its specific claims show up in real data.
- We are not building a model that predicts happiness. We are looking at the data thoughtfully.
- We are not doing original sociology — we are using existing data competently and asking sharp questions.
- We are not skipping the basics. Every session still introduces concepts step by step.

## How this changes the working agreement (it doesn't, but worth noting)

- Same rules: book records what actually happened, sessions are diaries with receipts, files small and linked, definitions only in glossary.
- Each session still ends with the full ritual.
- Each session still goes one cell at a time, beginner-paced.
- Plans are not promises. If Session 4 reveals that the data is different from what I expected, we adjust. The plan is a compass, not a contract.

## What gets parked alongside this

- *Thinking in Wholes* (2026) → `/data/raw/thinking_in_wholes_2026.md` — the lens.
- Ackoff lecture → `/data/raw/ackoff_lecture_systems_age.txt` — Session 6 reference material when we hit embeddings.
- Hamming lecture → already in `/data/raw/` — kept for a possible later session on the scientist's voice.

---

*Plan written end of Session 3. Session 4 begins by loading country-scale wellbeing data and asking the first big question: did growth and development actually decouple?*
