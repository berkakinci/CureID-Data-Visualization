# CureID Long COVID Data — Initial Findings

**Date:** May 10, 2026  
**Source:** FDA CureID Platform (v2 API, no auth required)  
**Database:** `cureid.db` — 702 reports, 22 diseases, 10K symptoms, 3.5K symptom→outcome mappings

---

## Dataset Overview

| Metric | Value |
|--------|-------|
| Long COVID reports | 616 |
| Related condition reports | 86 (across 21 conditions) |
| Total drugs tracked | 961 |
| Symptom entries | ~10,000 |
| Per-symptom treatment outcomes | ~3,500 |

**Report authors:** 495 patients, 108 doctors, 11 care partners  
**Symptom duration before treatment:** Majority 12–48+ months (chronic population)

### Demographics (Long COVID)

| Category | Breakdown |
|----------|-----------|
| Sex | Female 69%, Male 27%, Unknown 4% |
| Peak age | 31–50 (317 of 616, 51%) |
| Top countries | US (407), UK (55), Canada (34), Germany (19), Australia (14) |
| Vaccinated | Yes 55%, No 40%, Unknown 5% |

---

## Top Symptoms Reported

| # | Symptom | Count |
|---|---------|-------|
| 1 | Post-Exertional Malaise (PEM) | 502 |
| 2 | Brain fog / Cognitive dysfunction | 483 |
| 3 | General fatigue | 440 |
| 4 | Insomnia | 300 |
| 5 | POTS (orthostatic tachycardia) | 264 |
| 6 | Exertional dyspnea | 238 |
| 7 | Myalgia (muscle pain) | 238 |
| 8 | Orthostatic presyncope | 227 |
| 9 | Migraine / chronic headache | 222 |
| 10 | Muscle weakness | 214 |
| 11 | Tinnitus | 213 |
| 12 | Arthralgia (joint pain) | 203 |
| 13 | Temperature dysregulation | 198 |
| 14 | Short-term memory loss | 189 |
| 15 | Neuropathic pain | 187 |
| 16 | Tachycardia at rest | 181 |
| 17 | Nausea | 160 |
| 18 | Tremors | 154 |
| 19 | Anxiety | 153 |
| 20 | Dizziness | 143 |

---

## Outcome Distribution

| Outcome | Count | % |
|---------|-------|---|
| Significant improvement | 1,013 | 29% |
| Moderate improvement | 844 | 24% |
| Mild improvement | 658 | 19% |
| Complete resolution | 240 | 7% |
| **Total positive** | **2,755** | **79%** |
| Unchanged | 458 | 13% |
| Significant worsening | 49 | 1.4% |
| Moderate worsening | 44 | 1.3% |
| Mild worsening | 43 | 1.2% |
| Unknown/Other | 65 | 2% |

**Note:** Strong positive bias — patients who found something helpful are more likely to report. The 79% improvement rate should not be interpreted as drug efficacy; it reflects reporting behavior.

---

## Most-Used Drugs (by distinct reports)

| # | Drug | Reports |
|---|------|---------|
| 1 | Low Dose Naltrexone (LDN) | 222 |
| 2 | Famotidine (Pepcid) | 102 |
| 3 | Propranolol | 80 |
| 4 | CoQ10 | 73 |
| 5 | Cetirizine (Zyrtec) | 70 |
| 6 | Magnesium | 64 |
| 7 | Aspirin | 64 |
| 8 | NAC | 63 |
| 9 | Ivabradine | 59 |
| 10 | Fexofenadine (Allegra) | 49 |
| 11 | Gabapentin | 47 |
| 12 | Nattokinase | 46 |
| 13 | Vitamin D3 | 45 |
| 14 | Metoprolol | 45 |
| 15 | Melatonin | 44 |
| 16 | Probiotic | 41 |
| 17 | Vitamin B12 | 40 |
| 18 | Quercetin | 36 |
| 19 | Pyridostigmine (Mestinon) | 35 |
| 20 | Nicotine patch | 35 |
| 21 | Cromolyn sodium | 33 |
| 22 | Loratadine (Claritin) | 32 |
| 23 | Montelukast (Singulair) | 31 |
| 24 | Turmeric / Curcumin | 30 |
| 25 | Midodrine | 29 |

---

## Drug Efficacy (Symptom Outcome Breakdown)

Top drugs ranked by total outcome entries, showing improvement vs unchanged vs worsening:

| Drug | Improved | Unchanged | Worsened | Total | Improvement % |
|------|----------|-----------|----------|-------|---------------|
| LDN (combined) | 302 | 22 | 22 | 358 | 84% |
| Propranolol | 76 | 9 | 14 | 100 | 76% |
| Famotidine | 71 | 12 | 0 | 83 | 86% |
| Aspirin | 59 | 12 | 0 | 73 | 81% |
| Nattokinase | 56 | 8 | 0 | 69 | 81% |
| Ketotifen | 62 | 2 | 0 | 65 | 95% |
| Prednisolone | 43 | 2 | 1 | 48 | 90% |
| Melatonin | 33 | 9 | 1 | 43 | 77% |
| Gabapentin | 22 | 14 | 4 | 42 | 52% |
| Maraviroc | 32 | 5 | 3 | 41 | 78% |
| Metoprolol | 36 | 1 | 3 | 40 | 90% |
| Ivabradine (combined) | 80 | 8 | 0 | 90 | 89% |
| Cetirizine | 33 | 1 | 0 | 34 | 97% |
| Magnesium Glycinate | 28 | 0 | 0 | 30 | 100% |
| Bisoprolol | 30 | 2 | 1 | 33 | 91% |
| Midodrine | 26 | 1 | 0 | 27 | 96% |
| Hydroxyzine | 24 | 0 | 0 | 25 | 96% |

**Standouts:**
- **Ketotifen** (mast cell stabilizer): 95% improvement, zero worsening
- **Ivabradine** (heart rate control): 89% improvement, zero worsening
- **Famotidine, Aspirin, Nattokinase**: All show 0 worsening reports
- **Gabapentin**: Notably lower efficacy (52%) with highest unchanged rate — may reflect use for refractory symptoms

---

## Multi-Symptom Drugs

Drugs that improved the most distinct symptoms (minimum 10 total outcome entries):

| Drug | Distinct Symptoms Improved | Total Positive Outcomes |
|------|---------------------------|------------------------|
| LDN | 38 | 216 |
| Famotidine | 38 | 71 |
| Ketotifen | 36 | 62 |
| Cetirizine | 28 | 33 |
| Prednisolone | 25 | 43 |
| Propranolol | 24 | 76 |
| Aspirin | 24 | 59 |
| Nattokinase | 22 | 56 |
| Maraviroc | 22 | 32 |
| Hydroxyzine | 21 | 24 |
| Fexofenadine | 21 | 23 |
| Magnesium Glycinate | 20 | 28 |
| CBD | 19 | 25 |
| Bisoprolol | 18 | 30 |

**Interpretation:** Drugs helping 20+ distinct symptoms likely act on systemic mechanisms rather than targeting individual symptoms. LDN, famotidine, and ketotifen stand out as broad-spectrum — consistent with immune modulation / mast cell stabilization hypotheses.

---

## PEM-Specific Drug Outcomes

Post-Exertional Malaise is the hallmark Long COVID symptom. Top drugs with reported PEM outcomes:

| Drug | Significant | Moderate | Mild | Unchanged | Worsened |
|------|-------------|----------|------|-----------|----------|
| LDN (combined) | 12 | 20 | 20 | 5 | — |
| Nattokinase | 5 | — | — | — | — |
| Aspirin | 3 | 4 | 2 | — | — |
| Nicotine | — | 4 | — | — | — |
| Prednisolone | 4 | — | — | — | — |
| Paxlovid | 3 | — | — | — | — |
| Oxaloacetate | 3 | — | — | — | — |
| HBOT | 2 | — | — | — | — |
| IVIG | — | 2 | — | — | — |
| HELP Apheresis | 2 | — | — | — | — |

**Notable:** The anticoagulant cluster (nattokinase, aspirin, apheresis) and antivirals (Paxlovid) appearing for PEM aligns with microclot and viral persistence hypotheses.

---

## Comorbidities Developed After Long COVID

| Condition | Reports |
|-----------|---------|
| Dysautonomia | 313 (51%) |
| ME/CFS | 262 (43%) |
| POTS | 260 (42%) |
| MCAS | 156 (25%) |
| Migraine | 90 (15%) |
| Hypertension | 62 (10%) |
| Immunocompromised | 61 (10%) |
| IBS | 52 (8%) |
| Sleep apnea | 51 (8%) |
| Fibromyalgia | 48 (8%) |
| Autoimmune disorder | 38+30 (11%) |
| Herpesvirus reactivation | 37 (6%) |
| Asthma | 36 (6%) |
| Gastroparesis | 32 (5%) |
| Cardiovascular disease | 30 (5%) |
| Ehlers-Danlos Syndrome | 26 (4%) |

**Key pattern:** The dysautonomia/ME-CFS/POTS/MCAS cluster dominates post-COVID comorbidities, appearing in 25–51% of reports. This strongly supports the hypothesis that Long COVID triggers autonomic and immune dysregulation.

---

## Mechanism-Based Drug Groupings

Based on the top drugs, clear mechanistic clusters emerge:

### Mast Cell / Antihistamine
Famotidine, cetirizine, fexofenadine, ketotifen, hydroxyzine, cromolyn, loratadine, montelukast, quercetin

### Autonomic / Heart Rate
Propranolol, ivabradine, metoprolol, bisoprolol, midodrine, pyridostigmine, fludrocortisone

### Anticoagulant / Vascular
Aspirin, nattokinase, lumbrokinase, apixaban (Eliquis), clopidogrel, HELP apheresis

### Immune Modulation
LDN, prednisolone, IVIG, maraviroc

### Antiviral
Paxlovid (nirmatrelvir-ritonavir), valacyclovir

### Mitochondrial / Metabolic
CoQ10, NAC, magnesium, oxaloacetate, metformin, alpha-ketoglutarate

### Neurological / Pain
Gabapentin, amitriptyline, guanfacine, nicotine patch

### Other
Melatonin, CBD/THC, probiotics, vitamin D3, vitamin B12, turmeric

---

## Data Limitations

1. **Survivorship/reporting bias** — patients who improve are more likely to report; 79% improvement rate is not a true efficacy measure
2. **No control group** — cannot distinguish drug effect from natural recovery or placebo
3. **Drug name duplication** — same drug appears under multiple names (e.g., LDN has 2 variants, ivabradine has 3); counts above are partially consolidated but full normalization is pending
4. **Self-reported** — 80% of reports are from patients/caregivers, not clinicians
5. **Chronic population** — most reporters have had symptoms 12–48+ months; early-stage Long COVID is underrepresented
6. **Polypharmacy** — most patients report multiple drugs simultaneously; individual drug attribution is difficult
7. **No dosing standardization** — dose/frequency data exists but varies widely

---

## Next Steps

- [ ] Normalize drug names (consolidate duplicates for accurate counts)
- [ ] Build efficacy rankings per symptom (which drug works best for brain fog vs PEM vs POTS?)
- [ ] Analyze comorbidity clusters vs treatment response (do MCAS patients respond differently?)
- [ ] Cross-reference with related condition reports (do POTS drugs from standalone reports match Long COVID POTS treatments?)
- [ ] Investigate temporal patterns (do drugs work better earlier vs later in disease course?)
- [ ] Pull clinical trial data for top drugs to triangulate with patient reports
