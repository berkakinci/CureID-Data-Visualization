# Drug Heatmap Visualization

Self-contained HTML (`drug_heatmap_viz.html`) with all data embedded inline. Open directly from the filesystem — no server needed.

## Rebuilding

After DB changes, regenerate the HTML (re-embeds data from DB):
```bash
python drug_heatmap_build.py
```

## Files

| File | Role |
|------|------|
| `drug_heatmap_viz_template.html` | HTML/CSS/JS template with `/*__DATA_PLACEHOLDER__*/` and `/*__META_PLACEHOLDER__*/` |
| `drug_heatmap_build.py` | Queries DB via `symptom_drug_efficacy.py`, embeds into template → produces `drug_heatmap_viz.html` |
| `drug_heatmap_viz.html` | Generated output (do not edit directly — edit the template) |

## Features

- **Heatmap**: symptoms (rows, sorted by report count) × drugs (columns, sorted by selected metric). Color = lift or rate value.
- **Color by**: Co-occurrence Significant Improvement Lift (default), Any Improvement Lift, Significant Improvement Rate, Attributed Significant Improvement Lift.
- **Min N slider**: filter drugs by minimum co-occurring reports (higher = fewer drugs, more reliable).
- **Sort drugs**: N-weighted avg, Bayesian (shrinkage toward zero), Avg lift (unweighted), Max lift, A-Z. Hover buttons show formulas.
- **Hover tooltip**: full stats for each cell — co-occurrence N, significant improvement rate + lift, any improvement rate + lift, attributed stats (if available), and symptom baseline rates. "Click for details" hint.
- **Side panel (click)**:
  - Click a **drug name** (column header) → drug summary across all symptoms, ranked by current metric, with total N and average.
  - Click a **symptom name** (row label) → all drugs ranked for that symptom, plus symptom baseline rates.
  - Click a **cell** → full detail: rankings, outcome distribution bar, all co-occurrence and attributed stats, symptom baseline, and a mini leaderboard of top drugs for that symptom.
- **Drill-down to cases**: click any **N= value** (dotted underline) or the outcome distribution bar → detail pane opens as a second column showing individual case reports. Two-pane layout keeps stats visible on the left while browsing cases on the right. Case cards show demographics, full drug regimen (target highlighted), symptom outcomes (target symptom at top with background highlight, then others), and CureID link. Sortable: best/worst outcome, fewest symptoms, fewest drugs.
- **Info panel**: collapsible explanation of all metrics, controls, and interactions.
- **Data freshness**: subtitle shows most recent report date and count, derived from DB at build time.

## Color scales

- **Lift metrics** (all three): diverging red → yellow → green. Scale range is fixed across all lift metrics and N thresholds — the same color always means the same magnitude of lift, making views directly comparable.
- **Rate metric**: sequential yellow → green (0% to global maximum rate). Also fixed regardless of N threshold.
- **Dark cells**: no data for that drug-symptom pair at the current N threshold.

## Data thresholds

Configured in `drug_heatmap_build.py`:
- Symptoms must have ≥50 total reports
- Drugs must have ≥5 co-occurring reports per symptom
- Drugs must appear across ≥3 symptoms to be included

## Drug name normalization

All drug names are normalized via `normalize_name()` from `normalize_drugs.py` — programmatic cleanup (strip parenthetical brand names, dosage info, salt forms) followed by `drug_name_map` table lookup. Same normalization path used by the bar chart and efficacy scripts.

## Architecture

Single HTML file. D3 v7 loaded from CDN (requires internet connection). Data is embedded inline by the build script — includes aggregate cell metrics, outcome distributions, per-report case data (demographics, drugs, symptom outcomes), and cell-to-report mappings. Template uses placeholder comments that get replaced with JSON data and metadata during build. Typical output ~560 KB.

## Dependencies

- [D3 v7](https://d3js.org/) loaded from CDN at runtime
- `cureid.db` + `symptom_drug_efficacy.py` at build time
