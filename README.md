# CureID Data

Local queryable database of CureID case reports (FDA/NCATS).

## Configuration

`config.json` sets the target disease for all build scripts:

```json
{
  "disease_id": 1988,
  "disease_name": "Long COVID"
}
```

Change these values and rebuild to generate visualizations for a different CureID disease.

## Usage

```bash
python build_db.py          # builds cureid.db from raw_api_data/*.json
sqlite3 cureid.db           # query directly
```

## Schema (key tables)

- `reports` — one row per case (disease, outcome, author type)
- `patients` — demographics (sex, age_group, country, ethnicity)
- `symptoms` — per-report symptom list with severity
- `symptom_outcomes` — per-symptom treatment outcome (graded)
- `symptom_outcome_drugs` — which drug(s) produced each outcome
- `drugs` / `report_drugs` — drug catalog and per-report regimens with dosing
- `comorbidities` — pre-existing conditions
- `comorbidities_after` — conditions developed post-disease (e.g., ME/CFS after Long COVID)
- `extra_fields` — vaccine status, symptom duration, EHR labs, free-text notes

## Drug Name Normalization

Mapping table `drug_name_map` consolidates duplicate drug names without modifying raw data. View `v_drug_outcomes` applies it. See `python normalize_drugs.py --help`.

## Per-Symptom Efficacy Analysis

```bash
python symptom_drug_efficacy.py            # print tables to terminal
python symptom_drug_efficacy.py --markdown  # output markdown tables for findings.md
```

Dual-lens approach: co-occurrence lift (leave-one-out) + patient-attributed outcomes. Results in `symptom_drug_efficacy.csv`.

## Findings

See `findings.md` for the full write-up: demographics, top symptoms, drug efficacy rankings, per-symptom tables, mechanism groupings, and cross-symptom patterns.

## Visualization

Two interactive HTML visualizations (open directly in browser, no server needed):

- **`drug_outcomes_viz.html`** — Stacked bar chart of drug→outcome distributions with drill-down. See `drug_outcomes_viz_readme.md`.
- **`drug_heatmap_viz.html`** — Symptom × drug efficacy heatmap (D3). See `drug_heatmap_viz_readme.md`.

## Data source

API: `https://cure-api.ncats.io/v2` (no auth required).  
Raw JSON cached in `raw_api_data/` — re-run `build_db.py` to rebuild after adding new data.

## Updating data

Check for new reports and fetch if available:

```bash
python fetch_cureid.py          # check remote vs local count
python fetch_cureid.py --fetch  # download all reports into raw_api_data/
```

After fetching, rebuild everything:

```bash
python build_db.py                # rebuild cureid.db from raw JSON
python drug_outcomes_viz_build.py  # rebuild drug_outcomes_viz.html (embeds data from DB)
python drug_heatmap_build.py       # rebuild drug_heatmap_viz.html (embeds data from DB)
```

The HTML files embed all data inline (no server needed). The "Most recent report updated" date in each viz is derived from the DB automatically.

## Example queries

```sql
-- Top drugs for brain fog by outcome
SELECT sod.drug_name, so.outcome, COUNT(*) as n
FROM symptom_outcome_drugs sod
JOIN symptom_outcomes so ON sod.symptom_outcome_id = so.id
WHERE so.symptom LIKE '%Brain fog%' OR so.symptom LIKE '%Cognitive%'
GROUP BY sod.drug_name, so.outcome
ORDER BY sod.drug_name, n DESC;

-- Comorbidities developed after Long COVID
SELECT value, COUNT(*) as n
FROM comorbidities_after
GROUP BY value ORDER BY n DESC;
```
