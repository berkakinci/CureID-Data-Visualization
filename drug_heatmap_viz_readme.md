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
- **Sort drugs**: N-weighted avg, Bayesian (shrinkage toward zero), Avg lift (unweighted), Max lift, A-Z. Hover buttons for formula descriptions.
- **Hover tooltip**: full stats for each cell — co-occurrence N, significant improvement rate + lift, any improvement rate + lift, and (if available) attributed N + sig rate + lift.
- **Info panel**: collapsible explanation of all metrics and controls.
- **Data freshness**: subtitle shows most recent report date and count, derived from DB at build time.

## Color scales

- **Lift metrics**: diverging red → yellow → green (negative lift = red, zero = yellow, positive = green).
- **Rate metrics**: sequential yellow → green (0% to max).
- **Dark cells**: no data for that drug-symptom pair at the current N threshold.

## Data thresholds

Configured in `drug_heatmap_build.py`:
- Symptoms must have ≥50 total reports
- Drugs must have ≥5 co-occurring reports per symptom
- Drugs must appear across ≥3 symptoms to be included

## Architecture

Single HTML file. D3 v7 loaded from CDN (requires internet connection). Data is embedded inline by the build script. Template uses placeholder comments that get replaced with JSON data and metadata during build.

## Dependencies

- [D3 v7](https://d3js.org/) loaded from CDN at runtime
- `cureid.db` + `symptom_drug_efficacy.py` at build time
