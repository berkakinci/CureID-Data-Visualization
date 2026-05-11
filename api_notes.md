# CureID API Notes

## Overview

CureID is a collaboration between the FDA and NCATS/NIH. It captures real-world clinical outcome data (case reports) for drug repurposing across infectious diseases, rare cancers, and other conditions.

- **Website**: https://cure.ncats.io/explore
- **Live API base**: `https://cure-api.ncats.io/v2`
- **Auth required**: No (API is open; the SPA gates the UI but not the data endpoints)
- **Backend**: Django (based on response structure and prior art)
- **WebSocket**: `cure-api.ncats.io/ws` (purpose TBD — likely real-time notifications)

## Relevant Disease IDs

| ID   | Name       | Report Count |
|------|------------|--------------|
| 1589 | COVID-19   | 117,173      |
| 1988 | Long COVID | 616          |
| 1873 | SARS       | 2            |

## Known Endpoints (v2)

### Diseases
```
GET /v2/diseases
GET /v2/diseases?limit=500
GET /v2/diseases/{id}
```
- Paginated (default limit=16)
- Returns: id, name, url, discussion_count, report_count, trial_count, event_count, article_count, image_url, category, disease_group, url_name
- Response includes `api_version: "v2.0"`

### Drugs (per disease)
```
GET /v2/drugs?disease={disease_id}
GET /v2/drugs?disease={disease_id}&no_page    (v1 pattern — may still work)
```
- Not yet tested on v2 — needs probing

### Reports (case data)
```
GET /v2/reports?disease={disease_id}&drugs_id={drug_id}
```
- Not yet tested on v2 — needs probing
- v1 returned: patient demographics, drug regimens, outcomes, adverse events, country, case notes

## Dead Endpoints

- `cure-api2.ncats.io/v1/*` — connection timeout as of 2026-05-10. Was the original API used by CharlieDigital's project in 2021.

## Pagination

The v2 API uses offset-based pagination:
```json
{
  "count": 461,
  "next": "https://cure-api.ncats.io/v2/diseases?limit=16&offset=16",
  "previous": null,
  "results": [...]
}
```

## Prior Art

### CharlieDigital/covidcureid (MIT, 2021)
- GitHub: https://github.com/CharlieDigital/covidcureid
- Extracted COVID cases via v1 REST API
- Data flow: fetch drugs list → iterate each drug → fetch reports per drug → store as JSON
- Key v1 endpoints used:
  - `GET /v1/drugs?disease=630&no_page` (630 was COVID's v1 ID)
  - `GET /v1/reports?disease=630&drugs_id={id}&outcome_computed=&no_page=`
- Stored in Azure CosmosDB; front-end in Vue.js/Quasar
- Data model: DrugEntry (outcome per drug) + RegimenEntry (outcome per drug combination)
- Note: disease ID changed from 630 (v1) to 1589 (v2)

### OHDSI/CureIdRegistry (TSQL, institutional)
- GitHub: https://github.com/OHDSI/CureIdRegistry
- SQL scripts for extracting CureID cohorts from OMOP CDM (EHR-sourced data)
- Requires institutional OMOP database access — not useful for public API extraction
- But documents the target schema: Person, Measurement, Drug Exposure, Death, Observation, Procedure, Condition, Visit Occurrence, Device Exposure
- Cohort definition: hospitalized COVID patients with positive lab + inpatient stay within 7 days before to 21 days after positive test + COVID symptoms within 2 weeks of inpatient period

## Official Documentation

- **Data Dictionary**: https://cure.ncats.io/assets/resources/data-dictionary.pdf
- **Researcher's Guide**: https://cure.ncats.io/assets/resources/researchers-guide.pdf
- **Outcome Measures Report**: https://cure.ncats.io/assets/resources/outcome-measures-of-importance-to-patients.pdf
- **Patient Case Report Form**: https://cure.ncats.io/create/case/therapy-selection

## Data Characteristics (from ASPE/HHS project page)

- 115,000+ acute COVID-19 cases from 7 healthcare systems (100+ US hospitals)
- 585+ Long COVID cases (submitted by patients, caregivers, clinicians)
- Platform expanded beyond COVID: MPOX, RASopathies, Sarcoma, rare genetic disorders
- EHR-extracted data uses OMOP CDM concepts
- Manual case reports submitted by clinicians globally

## Data Model (from Data Dictionary)

The CureID case report form captures ~40 variables in the "small dataset" (publicly visible) and ~180 variables in the "large dataset" (requires SCCM or IDDO access).

### Core Fields (Small Dataset — available via API)

| # | Variable | Type | Notes |
|---|----------|------|-------|
| 1 | Disease | controlled term | e.g., COVID-19 |
| 2 | How Diagnosis | controlled term | Clinical assessment, PCR, etc. |
| 3 | Why New Way | controlled term | Reason for repurposing |
| 4 | Drug(s) | controlled term | Treatment drug names |
| 5 | Age | numeric | Patient age at treatment |
| 6 | Gender | controlled term | Male/Female |
| 7 | Outcome | controlled term | Cured/Improved/Deteriorated/Died |
| 8 | Country | controlled term | Country of treatment |
| 9 | Severity/Setting | controlled term | Inpatient/Outpatient/ICU |
| 10 | Year | numeric | Year treatment began |
| 11 | Adverse Events | controlled term + free text | |
| 12a-p | Comorbidities | Yes/No flags | HIV, Asthma, COPD, Diabetes, Hypertension, Cardiovascular, Chronic Renal, Chronic Liver, Immunodeficiency, Immunosuppressants, Malignancy, Obesity, Pregnancy, Smoking |
| 13 | Clinical presentation | free text (clinician only) | Site of disease, clinical syndrome |
| 14 | Unusual details | free text (clinician only) | |
| 15 | Organism | controlled term | e.g., SARS-CoV-2 |
| 18a-d | Dosing | numeric + free text | Dose, Frequency, Route, Duration (future EHR) |
| 20a | Severity proxy | controlled term | Treatment setting |
| 28 | Relapse | Yes/No | Disease relapse after treatment |
| 29 | Other info | free text | Clinician notes |

### EHR-Only Fields (Large Dataset — not in public API)

| # | Variable | Notes |
|---|----------|-------|
| 30 | BMI | At admission, grouped |
| 31a | Charlson Index | Comorbidity score |
| 31b | Serum Creatinine | First during hospitalization |
| 31c | GFR | First during hospitalization |
| 31d | WBC | First during hospitalization |
| 32 | Pulse Oximetry | Lowest SpO2 during stay |
| 33 | SpO2/FiO2 | Ratio at highest O2 demand (first 48h) |
| 34 | Oxygen Support Device | Highest level required |
| 35 | Admission date (relative) | De-identified, shifted |
| NA | CURE ID assigned ID | Internal tracking |
| NA | Subject ID | De-identified |

### Key Distinctions
- **Clinician-submitted cases**: Have free-text fields (unusual details, clinical syndrome, other info, dosing)
- **EHR-extracted cases**: Have structured lab values, BMI, Charlson index, oxygen data — but NOT free text
- **Both**: Have demographics, comorbidities, drugs, outcomes, country

## Data Architecture (from Researcher's Guide)

### Data Sources
1. **SCCM VIRUS Registry** — manual extraction from ICU/hospital sites
2. **EDGE Tool** — automated EHR extraction → OMOP CDM → CURE ID format
3. **CURE ID CRF** — clinician-submitted and literature-extracted cases
4. **ISARIC** — international dataset (only available via IDDO, not on CURE ID itself)

### Data Flow
```
EHR → EDGE Tool → OMOP CDM → De-identification (SANT) → Mayo/SCCM → IDDO (OMOP→SDTM) → NCATS → CURE ID
```

### Cohort Definition (COVID-19)
- All inpatients at participating facilities since March 2020
- Confirmed positive COVID-19 test within 14 days of admission
- Excluded: primary admission for trauma/surgery (COVID was incidental)
- Outpatient encounters NOT systematically captured

### De-identification Method: SANT (Shift and Truncate)
- Random person IDs replace medical record numbers
- All dates shifted by random per-patient offset (temporal relationships preserved)
- Site IDs removed by Mayo Clinic
- Displayed dates may appear as early as 6 months before March 2020

### Data Access Tiers
1. **Small dataset (40 vars)** — openly available via CURE ID website/app (and API!)
2. **Large dataset (180 vars)** — requires ancillary study proposal to SCCM Discovery
3. **Combined dataset (SCCM + IDDO/ISARIC)** — requires IDDO Data Access Application

### Important Limitation
> "The CURE ID CRF form data is only available for exploration in the CURE ID Website and Mobile App, and it is not available for download."

This is the official position — but the REST API serves the same data without auth, so the practical situation differs from the stated policy.

## Patient Outcome Measures (from Outcome Measures Report)

Key finding: Patients prioritize **Long COVID outcomes** over acute COVID-19 outcomes.

### Outcomes important to patients (NOT well captured in EHRs):
- Brain fog / cognitive function
- Fatigue / energy levels
- Ability to care for self/others
- Ability to function at work/school
- Mental health impact
- Quality of life measures

### Outcomes captured in EHRs (but less meaningful to patients):
- Death
- Length of hospital stay
- Lab values (objective measures)

### Implication for our work:
The Long COVID cases (616 reports) are likely patient/caregiver-submitted via the CRF and may contain richer subjective outcome data in free-text fields than the EHR-extracted acute COVID cases.

## Next Steps

- [x] Probe v2 drugs endpoint for Long COVID (disease=1988) — 961 drugs
- [x] Probe v2 reports endpoint — rich per-symptom outcome data confirmed
- [x] Check for rate limiting / pagination limits — limit=50 works reliably; limit=700 times out
- [ ] ~~Determine if `no_page` param works on v2~~ — not needed; pagination works fine
- [x] Map full endpoint surface — reports, drugs confirmed; filter params ignored on acute COVID
- [x] Download and review data dictionary PDF
- [ ] Design local database schema for querying
- [x] Investigate whether Long COVID cases have richer free-text data — YES, via extra_fields
- [x] Check if dosing info (18a-d) is populated — mostly null for Long COVID patient-submitted cases

## Downloaded Data Inventory

All cached in `raw_api_data/` to avoid re-fetching.

### Core
| File | Disease ID | Records | Size |
|------|-----------|---------|------|
| long_covid_reports.json | 1988 | 616 | 13 MB |
| long_covid_drugs.json | 1988 | 961 | 129K |
| covid19_acute_drugs.json | 1589 | 1000 | 162K |

### Post-infectious / Overlap
| File | Disease ID | Records |
|------|-----------|---------|
| dysautonomia_pots_reports.json | 2120 | 7 |
| mcas_reports.json | 2146 | 5 |
| mecfs_reports.json | 2121 | 1 |
| fibromyalgia_reports.json | 2122 | 2 |
| ehlers_danlos_reports.json | 2064 | 3 |
| small_fiber_neuropathy_reports.json | 2086 | 1 |

### Viral Persistence / Reactivation
| File | Disease ID | Records |
|------|-----------|---------|
| epstein_barr_reports.json | 1664 | 3 |
| cytomegalovirus_reports.json | 1632 | 23 |
| herpes_simplex_reports.json | 1705 | 6 |
| herpes_zoster_reports.json | 1706 | 3 |
| herpes_labialis_reports.json | 1704 | 3 |
| genital_herpes_reports.json | 1681 | 3 |
| infectious_mononucleosis_reports.json | 1712 | 2 |

### Autoimmune / Neuroinflammatory
| File | Disease ID | Records |
|------|-----------|---------|
| encephalitis_reports.json | 1649 | 4 |
| myelitis_reports.json | 1766 | 2 |
| colitis_reports.json | 1619 | 4 |
| crohns_disease_reports.json | 2099 | 1 |
| myasthenia_gravis_reports.json | 2193 | 1 |
| cipn_reports.json | 2174 | 1 |

### Infection-Triggered
| File | Disease ID | Records |
|------|-----------|---------|
| chronic_lyme_reports.json | 2125 | 6 |
| lyme_acute_reports.json | 1736 | 5 |

## API Behavior Notes

- Pagination: offset-based, limit=50 is reliable, limit=700+ causes timeout on large datasets
- Filter params (`drugs_id`, `outcome_computed`, `form_type`, `report_type`, `drug`) are **ignored** on the acute COVID endpoint — always returns full count regardless
- Filter params DO work on Long COVID (user's Feb download used `long_covid_outcome` and `symptom_long_covid` successfully)
- Rate limiting: none observed at our request rate (~2 req/sec with 0.3-0.5s delays)
- The `sort=latest` param works
- WebSocket at `cure-api.ncats.io/ws` — purpose unknown, not explored
