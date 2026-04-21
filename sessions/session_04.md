# Session 4 — Record

*First session of the Wholeness Investigation. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

Load country-scale wellbeing data. First cross-country look at how happiness relates to its putative drivers. Open testing of **H2** (connection predicts wellbeing better than wealth). Park time-series data for **H1** (growth ≠ development), coming in Session 5.

## What actually happened

The surface question — does social support correlate more with happiness than GDP — came back tied at four decimal places (0.812 vs 0.799, n=144, 2025 cross-section). That was a non-finding; the difference is within noise. But the investigation did not stop there. When I extended the analysis into the time dimension (2019 → 2025, the years where the WHR's factor decomposition is fully populated) a much bigger, stranger pattern emerged: **the WHR's own model systematically fails globally between 2019 and 2025, and the failure has the shape the book predicts.**

## The big finding

Across 141 countries with full 2019 and 2025 data:

| | |
|---|---|
| Countries where measured factors collectively **rose** | **99.3%** |
| Countries where the unexplained component (Dystopia + residual) **fell** | **97.9%** |
| Both, AND happiness still fell | 37.6% |
| Global mean change in measured factors | **+0.944** |
| Global mean change in unexplained | **−0.842** |
| Global mean change in happiness | +0.102 |

The measured factors improved almost everywhere; the unexplained component fell almost everywhere; they nearly cancel. **The WHR model predicts a substantially happier world between 2019 and 2025 than actually exists.** The gap is global and systematic, not noise.

This is not the finding I set out to produce. The initial session plan was "begin testing H1 and H2." H2's single-year test was inconclusive. But the time-series extension opened a bigger question the plan didn't anticipate and which all four hypotheses now orbit: *what is in the residual, and why is it falling?*

## Decisions made

- **Data source.** Official World Happiness Report 2026 file, "Data for Figure 2.1 (2011–2025)." 2,116 rows, 13 columns, country × year panel.
- **Download path.** S3 direct download returned HTTP 403 to Python's urllib. Fell back to browser download + Colab upload. Lesson: public data ≠ script-accessible data.
- **Cross-section for correlations:** 2025 only, 147 countries before cleaning.
- **NaN + Venezuela dropped.** Venezuela's GDP column is a literal 0.000 (USD/PPP uncomputable under hyperinflation). 145 → 144.
- **Factor columns' semantics.** The six "Explained by" columns are each factor's contribution to predicted happiness in the WHR's regression, not raw values. Pearson correlation is invariant under their positive linear transforms, so correlations are valid.
- **Time-series window: 2019–2025.** Factor decomposition only populated from 2019 onwards. Six-year window, pandemic-spanning.

## The cross-section (first pass, H2 test)

Pearson *r* between happiness and each factor contribution, 144 countries, 2025:

| Factor | r |
|---|---|
| Social support | +0.812 |
| Log GDP per capita | +0.799 |
| Healthy life expectancy | +0.679 |
| Freedom to make life choices | +0.638 |
| Perceptions of corruption (inverted) | +0.396 |
| Generosity | +0.038 |

Gap between top two: 0.013. Noise. H2 not confirmed, not rejected, too blunt a test.

Dropping Venezuela moved GDP from +0.745 to +0.799. Social support did not move. One broken row was doing almost all the work of separating them — the "sense of drift" moment. Any finding that fragile is not a finding.

**Top residuals** (happier than GDP alone predicts): Mozambique +1.58, Costa Rica +1.39, Kosovo +1.29, Belize +1.27, Nicaragua +1.26.

**Bottom residuals:** Afghanistan −2.53, Botswana −2.28, Egypt −1.82, Lebanon −1.61, Sri Lanka −1.50.

## The time series (the real finding)

### Anglosphere 2019 → 2025

| Country | Δ happy | Δ GDP | Δ social | Δ health | Δ freedom | Δ generosity | Δ corruption | **Δ unexplained** |
|---|---|---|---|---|---|---|---|---|
| UK | −0.47 | +0.62 | +0.00 | −0.09 | +0.44 | −0.18 | −0.03 | **−1.23** |
| Canada | −0.49 | +0.62 | +0.09 | −0.07 | +0.30 | −0.13 | −0.03 | **−1.27** |
| US | −0.12 | +0.63 | +0.11 | −0.15 | +0.24 | −0.14 | +0.00 | **−0.81** |
| Australia | −0.31 | +0.63 | +0.02 | −0.07 | +0.37 | −0.17 | −0.04 | **−1.04** |
| New Zealand | −0.30 | +0.63 | +0.09 | −0.08 | +0.39 | −0.17 | −0.04 | **−1.13** |
| Ireland | −0.17 | +0.70 | +0.09 | −0.04 | +0.44 | −0.12 | −0.01 | **−1.22** |
| Switzerland | −0.54 | +0.64 | +0.06 | −0.02 | +0.41 | −0.12 | +0.04 | **−1.55** |

Every measured factor neutral or positive. Every country's unexplained component falling by ~1 point. The entire happiness decline lives in the residual.

### Global pattern (n=141)

- **99.3%** saw measured factors rise.
- **97.9%** saw unexplained fall.
- Mean measured rise: +0.944. Mean unexplained fall: −0.842. Net: +0.102.

A unidirectional global signal. Residuals being random error would give numbers symmetric around zero. These are not.

### The exceptions

Countries where happiness rose 2019 → 2025 (top): Viet Nam +1.07, India +0.96, China +0.95, Serbia +0.91, Armenia +0.91, Georgia +0.84, Albania +0.78, Mozambique +0.71, Bosnia +0.71. These are the ones where the unexplained component held steady or rose.

### What is in the residual

By construction: anything moving between countries and years affecting life evaluations not captured by the six factors. The six are income, social support (one question: *"If in trouble, do you have relatives or friends you can count on?"*), healthy life expectancy, freedom to make life choices (one question), generosity (one question: *"Have you donated money to charity in the past month?"*), perceived corruption (two-question avg).

Not measured: meaning, purpose, hope, religious practice, fertility, family structure, loneliness as a continuous variable, trust in institutions beyond government, housing, attention fragmentation, digital life, belonging to groups thicker than "someone to count on."

This is H2's real answer, pushed. The WHR's "social support" measure is a one-item proxy for what the book means by connection. It is too thin. Something richer is in the residual and is falling.

## What got added to the book

- [Chapter 5](../book/chapter_05.md) — *What the model can't see.*

## Caveats on the record

1. Window is short (2019–2025, six years, pandemic inside).
2. "Dystopia + residual" adds a time-invariant Dystopia constant to country-specific residual. The *change* is still the change in residual. Absolute levels in the column are confounded for cross-sectional reads.
3. 141 countries = intersection of 2019 and 2025 samples. Gallup fieldwork shifts mean some countries appear in one year but not the other.
4. Happiness here means the Cantril ladder. Other wellbeing measures (affect, eudaimonic) may look different.
5. Correlation ≠ decomposition. Two different arguments. First says factors are informative cross-sectionally; second says they are uninformative about change over time — a stronger claim.

## Decisions deferred

- Extend backward using pre-2019 raw Gallup data (Session 7+).
- Merge residual change against external data: loneliness surveys, fertility, religious practice, trust, screen time (Sessions 7–10).
- Botswana mystery — deep below the line in both cross-section and change. Flag for later.
- Generosity null correlation (r = +0.038). Almost certainly a measurement issue. Park.

## Status at end of session

Three charts ([`chapter_05_gdp_happiness.png`](../book/images/chapter_05_gdp_happiness.png), [`chapter_05_uk_decomposition.png`](../book/images/chapter_05_uk_decomposition.png), [`chapter_05_measured_vs_unexplained.png`](../book/images/chapter_05_measured_vs_unexplained.png)). Two processed CSVs ([`whr2025_clean.csv`](../data/processed/whr2025_clean.csv), [`whr_changes_2019_2025.csv`](../data/processed/whr_changes_2019_2025.csv)). Source xlsx at [`/data/raw/WHR26_Data_Figure_2.1.xlsx`](../data/raw/WHR26_Data_Figure_2.1.xlsx).

The investigation has a real hook: **name what is in the residual.** All four hypotheses reorient around that. Session 5 starts from the processed CSV with HDI + World Bank data to test H1 over 30 years.

---

## Raw outputs (receipts)

### UK year by year

```
 year  happiness   gdp  social  health  freedom  generosity  corruption  unexplained
 2019      7.165 1.273   1.458   0.976    0.525       0.373       0.323        2.237
 2020      7.064 1.423   1.062   0.757    0.580       0.340       0.306        2.596
 2021      6.943 1.867   1.143   0.750    0.597       0.289       0.329        1.967
 2022      6.796 1.857   1.366   0.511    0.626       0.272       0.340        1.822
 2023      6.749 1.822   1.326   0.672    0.713       0.267       0.351        1.598
 2024      6.728 1.725   1.562   0.779    0.872       0.211       0.318        1.260
 2025      6.694 1.896   1.458   0.888    0.962       0.191       0.291        1.008
```

UK's unexplained column: 2.24 → 1.01. Collapse of 1.23 points in six years, while GDP rose from 1.27 to 1.90.

### Global summary (n=141, 2019→2025)

```
Fraction of countries where:
  measured factors collectively went UP: 99.3%
  unexplained went DOWN:                97.9%
  both AND happiness fell:              37.6%

Means of changes:
  d_measured_sum   +0.944
  d_unexplained    -0.842
  d_happiness      +0.102
```

### Key code blocks

Build the 2019→2025 change panel:

```python
fac = raw[raw['year'] >= 2019].dropna(
    subset=['gdp','social','health','freedom','generosity','corruption','unexplained'])
d1 = fac[fac['year']==2019].set_index('country')
d2 = fac[fac['year']==2025].set_index('country')
common = d1.index.intersection(d2.index)
ch = pd.DataFrame(index=common)
for c in ['happiness','gdp','social','health','freedom','generosity','corruption','unexplained']:
    ch[f'd_{c}'] = d2.loc[common,c] - d1.loc[common,c]
ch['d_measured_sum'] = ch[['d_gdp','d_social','d_health',
                            'd_freedom','d_generosity','d_corruption']].sum(axis=1)
```

### Exports

- `data/processed/whr2025_clean.csv` — 144 countries, 2025 cross-section, cleaned.
- `data/processed/whr_changes_2019_2025.csv` — 141 countries × 2019 level + 2025 level + delta for all columns + measured-sum.
