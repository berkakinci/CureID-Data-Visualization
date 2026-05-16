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
| `drug_outcomes_viz_data.json` | Per-drug outcome counts (resolved/significant/moderate/mild/unchanged/worsened) |
| `drug_outcomes_viz_details.json` | Per-drug list of case reports with metadata + attributed symptom outcomes |

## Files

| File | Role |
|------|------|
| `drug_outcomes_viz_template.html` | HTML/CSS/JS template with `/*__DATA_PLACEHOLDER__*/` and `/*__META_PLACEHOLDER__*/` |
| `drug_outcomes_viz_build.py` | Queries DB, generates JSON, embeds into template → produces `drug_outcomes_viz.html` |
| `drug_outcomes_viz.html` | Generated output (do not edit directly — edit the template) |

## Features

- **Bar chart**: stacked horizontal bars, one per drug. Color = outcome grade.
- **Controls**: sort (avg score per report, sum of scores, total outcomes, total reports, % any improvement, % significant improvement, % complete resolution, % worsened, alpha), min-report slider, absolute/% toggle.
- **Hover tooltip**: outcome breakdown with counts, percentages, and average score.
- **Legend tooltips**: hover color swatches for outcome category definitions.
- **Info panel**: collapsible explanation of controls and metrics.
- **Click drill-down**: slide-in panel listing all cases for that drug. Each case shows demographics, illness duration, author type, attributed symptom→outcome pairs, and a link to the CureID web page.
- **Panel sort**: best/worst outcome, most symptoms, longest duration.
- **Data freshness**: subtitle shows most recent report date and count, derived from DB at build time.

## Architecture

Single HTML file, no runtime dependencies. Data is embedded inline by the build script. Template uses placeholder comments that get replaced with JSON data and metadata during build.

## CureID Case Links

```
https://cure.ncats.io/explore/long-covid/case-reports/case-details/{report_uuid}
```

## Dependencies

- D3 is **not** used here (pure vanilla JS)
- Requires `cureid.db` at build time
