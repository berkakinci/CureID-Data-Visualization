# CureID Data

Local queryable database of CureID case reports (FDA/NCATS).

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

## Visualization

Open `drug_outcomes_viz.html` in a browser — self-contained stacked bar chart of drug→outcome data. Sort by % positive, % significant, % resolved, or % worsened. Hover for details. Adjust minimum report threshold with the slider.

## Data source

API: `https://cure-api.ncats.io/v2` (no auth required).  
Raw JSON cached in `raw_api_data/` — re-run `build_db.py` to rebuild after adding new data.

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
