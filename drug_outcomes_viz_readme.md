# Drug Outcomes Visualization

Self-contained HTML (`drug_outcomes_viz.html`) that loads two JSON data files.

## Data Files

| File | Contents |
|------|----------|
| `drug_outcomes_viz_data.json` | Per-drug outcome counts (resolved/significant/moderate/mild/unchanged/worsened) |
| `drug_outcomes_viz_details.json` | Per-drug list of case reports with metadata + attributed symptom outcomes |

Regenerate both after DB changes:
```bash
python drug_outcomes_viz_build.py
```

## Features

- **Bar chart**: stacked horizontal bars, one per drug. Color = outcome grade.
- **Controls**: sort (total, % positive, % sig+resolved, % resolved, % worsened, alpha), min-report slider, absolute/% toggle.
- **Hover tooltip**: outcome breakdown with counts and percentages.
- **Click drill-down**: slide-in panel listing all cases for that drug. Each case shows demographics, illness duration, author type, attributed symptom→outcome pairs, and a link to the CureID web page.
- **Panel sort**: best/worst outcome, most symptoms, longest duration.

## Architecture

Single HTML file, no build step, no dependencies. Fetches JSON via relative `fetch()` — must be served or opened from the same directory. CSS and JS are inline.

## CureID Case Links

```
https://cure.ncats.io/explore/long-covid/cases/{report_uuid}
```
