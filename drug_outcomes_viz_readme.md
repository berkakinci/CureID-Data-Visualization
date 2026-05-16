# Drug Outcomes Visualization

Self-contained HTML (`drug_outcomes_viz.html`) with all data embedded inline. Open directly from the filesystem — no server needed.

## Rebuilding

After DB changes, regenerate the HTML (re-embeds data from DB):
```bash
python drug_outcomes_viz_build.py
```

This also regenerates the intermediate JSON files:

| File | Contents |
|------|----------|
| `drug_outcomes_viz_data.json` | Per-drug per-report quantized outcome counts + scoring metrics |
| `drug_outcomes_viz_details.json` | Per-drug list of case reports with metadata + attributed symptom outcomes |

## Files

| File | Role |
|------|------|
| `drug_outcomes_viz_template.html` | HTML/CSS/JS template with `/*__DATA_PLACEHOLDER__*/` and `/*__META_PLACEHOLDER__*/` |
| `drug_outcomes_viz_build.py` | Queries DB, generates JSON, embeds into template → produces `drug_outcomes_viz.html` |
| `drug_outcomes_viz.html` | Generated output (do not edit directly — edit the template) |

## How it works

Each bar represents one drug. Each patient report gets **one vote** based on the average of its attributed symptom scores, quantized back to the nearest outcome bucket:

| Avg Score | Bucket |
|-----------|--------|
| ≥ 2.5 | Resolved |
| 1.5 – 2.5 | Significant |
| 0.75 – 1.5 | Moderate |
| 0.25 – 0.75 | Mild |
| -0.25 – 0.25 | Unchanged |
| < -0.25 | Worsened |

**Scoring:** resolution=+3, significant=+2, moderate=+1, mild=+0.5, unchanged=0, worsening=-0.5 to -2. A report's score is the mean across all symptoms the patient attributed to that drug.

## Features

- **Bar chart**: stacked horizontal bars, one per drug. Each segment = one report quantized to an outcome bucket. Color = outcome grade.
- **Controls**: sort (sum of scores, avg score, total outcomes, total reports, % any improvement, % moderate+, % significant, % resolved, % worsened, alpha), min-report slider, normalize bars toggle.
- **Hover tooltip**: per-report quantized outcome breakdown with counts and percentages.
- **Legend tooltips**: hover color swatches for outcome category definitions.
- **Info panel**: collapsible explanation of scoring, quantization, and controls.
- **Click drill-down**: slide-in panel listing all cases for that drug. Each case shows demographics, illness duration, author type, attributed symptom→outcome pairs, and a link to the CureID web page. Sorted by per-report average score.
- **Panel sort**: best/worst outcome (by avg score), most symptoms, longest duration.
- **Data freshness**: subtitle shows most recent report date and count, derived from DB at build time.
- **Auto-normalize**: percentage and avg-score sorts auto-enable normalized bars; volume sorts auto-disable.

## Drug name normalization

All drug names are normalized via `normalize_name()` from `normalize_drugs.py` — programmatic cleanup (strip parenthetical brand names, dosage info, salt forms) followed by `drug_name_map` table lookup. Same normalization path used by the heatmap and efficacy scripts.

## Architecture

Single HTML file, no runtime dependencies. Data is embedded inline by the build script. Template uses placeholder comments that get replaced with JSON data and metadata during build.

## CureID Case Links

```
https://cure.ncats.io/explore/long-covid/case-reports/case-details/{report_uuid}
```

## Dependencies

- D3 is **not** used here (pure vanilla JS)
- Requires `cureid.db` at build time
