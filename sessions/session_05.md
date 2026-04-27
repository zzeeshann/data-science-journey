# Session 5 — Record

*Second session of the Wholeness Investigation. Concepts link to [05_glossary.md](../05_glossary.md).*

---

## Goal

Test **H1** — does economic growth actually translate into human development? Load thirty years of UNDP Human Development Index data, merge it with the WHR change panel from Session 4, and see whether GDP and development have started pulling apart post-2019. If they have, does HDI stagnation predict bigger falls in the happiness residual?

## What actually happened

The global story was more nuanced than the hypothesis predicted: GDP and HDI didn't fully decouple everywhere. They still correlate at r=0.32 — moderate, statistically significant. But inside that global relationship, a clear subgroup of 38 countries emerged where GDP rose while HDI barely moved, and in that group the happiness decline landed almost entirely in the unexplained residual. H1 isn't a universal law; it's a real pattern that holds for roughly a third of the dataset.

The other result that surprised: HDI stagnation alone doesn't strongly predict residual drops (r=0.11, not significant). Only when you control for GDP does HDI start to matter (p=0.062, borderline). What that means is the residual isn't explained by development metrics either — it lives somewhere else that neither HDI nor the WHR six factors can see.

## The data

- **UNDP Human Development Index complete time series 1990–2023**, 206 countries, downloaded from `hdr.undp.org`. File: `HDR25_Composite_indices_complete_time_series.csv`.
- **WHR change panel from Session 4**: `whr_changes_2019_2025.csv` — 141 countries, 2019→2025 changes.
- **Merged file**: `session_05_merged.csv` — 129 countries after inner join on country name. This is the working dataset for all Session 5 analysis.

Analysis run in Julius AI (julius.ai). No Colab this session — the merged CSV was built here and Julius handled all the analysis and charts.

## Finding 1 — Global HDI stalled after 2019

Mean HDI across 129 countries rose steadily from 0.617 in 1990 to 0.753 in 2019 — thirty years of consistent upward movement. Then it dipped during the pandemic years before recovering to 0.762 by 2023. The post-2019 period is visibly flatter than any comparable stretch in the preceding three decades.

Thirty years of improvement in health, education, and living standards, then a pause. The pause itself is not the main story — it's what happened to happiness inside the pause.

## Finding 2 — H1 result: partial, not global

The correlation between WHR GDP-factor change (2019→2025) and HDI change (2019→2023) is **r = 0.32**, p ≈ 0.015. Economic improvement still tends to come with development improvement. The clean version of H1 — "growth has stopped translating into development everywhere" — is not supported.

But correlation hides the distribution. The scatter plot shows wide spread: plenty of countries with substantial GDP-factor gains but near-zero HDI movement, sitting below the regression line. H1 is not a law; it is a subgroup pattern.

## Finding 3 — 38 countries: GDP up, HDI flat

The sharpest result came from a direct filter: countries where the WHR GDP factor rose (d_gdp > 0) but HDI moved less than 0.005 between 2019 and 2023. **38 countries — nearly a third of the dataset** — fit this profile.

| Country | d_gdp | d_hdi (2019–2023) | d_unexplained | d_happiness |
|---|---|---|---|---|
| Afghanistan | 0.620 | −0.011 | −1.368 | −1.121 |
| Austria | 0.637 | 0.002 | −1.341 | −0.449 |
| Canada | 0.615 | 0.002 | −1.272 | −0.491 |
| Lebanon | 0.539 | −0.019 | −1.271 | −1.049 |
| Norway | 0.633 | 0.003 | −1.255 | −0.246 |
| Finland | 0.630 | 0.001 | −1.181 | −0.045 |
| Germany | 0.634 | 0.002 | −1.167 | −0.194 |
| New Zealand | 0.634 | 0.000 | −1.125 | −0.305 |
| United Kingdom | 0.623 | 0.005 | −0.961 | −0.471 |
| United States | 0.628 | 0.002 | −0.810 | −0.124 |

Afghanistan sits next to Austria. Lebanon next to Norway. Crisis-affected nations and wealthy stable democracies in the same bucket. The pattern isn't about poverty or political collapse — it cuts across country type.

In every one of these 38 countries, the GDP factor rose, human development barely moved, and the happiness decline showed up almost entirely in the unexplained residual. The measured world improved. The felt world didn't.

## Finding 4 — Inside the 38: health shock is the strongest thread

Within the 38-country group, checking which WHR factors correlate with the residual decline:

| Factor | Correlation with d_unexplained |
|---|---|
| d_health | −0.306 |
| d_social | +0.193 |
| d_gdp | −0.161 |
| d_generosity | +0.128 |
| d_freedom | +0.118 |
| d_corruption | +0.034 |

Health is the strongest signal: where health worsened, the residual dropped further. This is consistent with pandemic-era disruption leaving a mark that outlasted the acute phase — not just in mortality statistics but in how people experience their lives.

But no single factor explains it. The post-2019 wellbeing decline is multi-causal and sits mostly outside what any standard metric measures.

## Finding 5 — The UK in miniature

UK HDI: 0.941 in 2019, dipped to 0.930 during COVID, then recovered to 0.946 by 2023. By development statistics, the UK is essentially where it was. Happiness fell from 7.165 to 6.694 — nearly half a point gone. The entire gap between those two numbers lives in the unexplained residual.

The UK's development statistics did not predict its happiness trajectory at all.

## What this means for the investigation

H1 is filed. Not a global law, but a real pattern in a meaningful subgroup. The deeper finding is that neither HDI nor the WHR six factors can explain what happened to happiness in the 2020s. The residual isn't development stagnation. It isn't health decline alone. It isn't any single measured thing.

The investigation has now ruled out two large candidate explanations — GDP stagnation (Session 4 showed GDP rose almost everywhere) and development stagnation (Session 5 shows HDI moved too). Whatever is in the residual is something that standard metrics of both economic and human progress don't capture.

**The residual is the investigation now. Sessions 6 onwards try to name it.**

## Caveats

1. The HDI data ends at 2023. The WHR change panel runs to 2025. The HDI gap means we're comparing a slightly shorter window for the development side.
2. 38 countries is a real cluster but not a majority. 91 countries in this dataset did see GDP and HDI move together.
3. The health correlation (−0.306) is the strongest signal but still weak in absolute terms. Multi-causality is the honest description, not a clean single driver.
4. Julius AI generated all charts and statistics. Code was generated automatically and not manually verified line by line — findings should be treated as strong leads, not final results, until replicated.

## Status at end of session

Five charts ([`chapter_06_hdi_global_trend.png`](../book/images/chapter_06_hdi_global_trend.png), [`chapter_06_gdp_hdi_scatter.png`](../book/images/chapter_06_gdp_hdi_scatter.png), [`chapter_06_residual_hdi_scatter.png`](../book/images/chapter_06_residual_hdi_scatter.png), [`chapter_06_h1_health_scatter.png`](../book/images/chapter_06_h1_health_scatter.png), [`chapter_06_uk_hdi_happiness.png`](../book/images/chapter_06_uk_hdi_happiness.png)). One processed CSV ([`session_05_merged.csv`](../data/processed/session_05_merged.csv)). One new book chapter ([`chapter_06.md`](../book/chapter_06.md)).

H1 is done. The residual is still unexplained. Session 6 moves into embeddings and language — the Ackoff text, *Thinking in Wholes*, Reddit corpora — to ask whether the language of wholeness and fragmentation is actually shifting in the years the data says something changed.

---

## Raw outputs (receipts)

### Global HDI summary
```
Mean HDI 1990: 0.617
Mean HDI 2019: 0.753
Mean HDI 2023: 0.762
Post-2019 change: +0.009 (vs +0.136 over 1990–2019)
```

### H1 correlation
```
Correlation (d_gdp, d_hdi_2019_2023): 0.318
OLS slope: 0.037
OLS p-value: 0.015
```

### HDI stagnation vs residual
```
Bivariate r (d_hdi_2019_2023, d_unexplained): 0.11
p-value: 0.25 (not significant)
With GDP controlled: HDI slope ≈ 8.42, p ≈ 0.062 (borderline)
```

### H1 filter: GDP up, HDI flat (< 0.005)
```
Countries matching: 38 (of 129)
Share of dataset: 29.5%
```

### UK HDI by year
```
2019: 0.941
2020: 0.930
2021: 0.941
2022: 0.946
2023: 0.946
Happiness 2019: 7.165
Happiness 2025: 6.694
Change: −0.471 (almost entirely in d_unexplained)
```
