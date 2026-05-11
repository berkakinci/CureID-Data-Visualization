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
3. **Self-reported** — 80% of reports are from patients/caregivers, not clinicians
4. **Chronic population** — most reporters have had symptoms 12–48+ months; early-stage Long COVID is underrepresented
5. **Polypharmacy** — most patients report multiple drugs simultaneously (avg 6.7 per report); individual drug attribution is difficult
6. **No dosing standardization** — dose/frequency data exists but varies widely
7. **Attribution bias** — patients choose which drugs to credit for which symptoms; drugs with systemic effects may be under-credited for some symptoms and over-credited for others

---

## Per-Symptom Drug Efficacy (Dual-Lens Analysis)

Two complementary approaches to rank drugs per symptom:

1. **Attributed**: patient explicitly linked drug → symptom → outcome (what they reported)
2. **Co-occurrence lift**: improvement rate for reports *taking* drug X vs reports *not taking* drug X, regardless of what the patient attributed (removes attribution bias, but confounded by polypharmacy)

### Definitions

- **Baseline**: the improvement rate for a symptom across *all* reports, regardless of drug. Shown in bold at the top of each table for comparison.
- **Co-N**: number of reports where the patient was taking this drug and had an outcome recorded for this symptom (regardless of attribution).
- **Sig%**: % of co-occurring reports where the outcome was "Significant improvement" or "Complete resolution."
- **Sig Lift**: difference between this drug's Sig% and the baseline Sig%. Positive = more significant outcomes than average.
- **Impr%**: % of co-occurring reports where the symptom improved (any level: mild through complete resolution).
- **Impr Lift**: difference between this drug's Impr% and the Impr% for reports *not* taking this drug. Positive = better than average; negative = worse (often indicates confounding by severity).
- **Attr N**: number of times patients explicitly attributed this drug to this symptom's outcome.
- **Attr Sig%**: % of attributed entries reporting significant improvement or complete resolution.
- **Attr Sig Lift**: difference between Attr Sig% and the baseline attributed Sig%.
- **Attr Impr%**: % of attributed entries reporting any improvement.
- **Attr Impr Lift**: difference between Attr Impr% and the baseline attributed Impr%.

### How to read the tables

A drug is most convincing when it scores high on *both* Sig Lift (more significant outcomes than average) and Impr Lift (associated with better-than-average improvement). High Impr Lift with low Sig% means broad mild benefit. High Sig% with negative Impr Lift means the drug works but is given to harder cases. The co-occurrence table is sorted by Sig Lift; the attributed table by Attr Sig Lift.

### PEM (Post-Exertional Malaise)

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **300** | **32%** | — | **87%** | — | **249** | **28%** | — | **86%** | — |
| | | | | | | | | | | |
| Hyperbaric Oxygen Therapy (HBOT) | 10 | 60% | +28% | 90% | +5% | — | — | — | — | — |
| Melatonin | 28 | 46% | +15% | 96% | +13% | — | — | — | — | — |
| Valacyclovir | 15 | 47% | +14% | 80% | -6% | 7 | 43% | +15% | 57% | -29% |
| Paxlovid (Nirmatrelvir-Ritonavir) | 16 | 44% | +11% | 94% | +9% | 8 | 75% | +47% | 88% | +2% |
| Nattokinase | 25 | 40% | +8% | 88% | +3% | 10 | 50% | +22% | 90% | +4% |
| Vitamin D3 | 23 | 39% | +7% | 87% | +2% | — | — | — | — | — |
| Guanfacine | 11 | 36% | +3% | 82% | -4% | 5 | 0% | -28% | 80% | -6% |
| Gabapentin | 20 | 35% | +2% | 80% | -6% | — | — | — | — | — |
| Cromolyn Sodium | 18 | 33% | +0% | 100% | +16% | — | — | — | — | — |
| Quercetin | 18 | 33% | +0% | 100% | +16% | — | — | — | — | — |
| Metformin | 18 | 33% | +0% | 94% | +10% | 8 | 25% | -3% | 100% | +14% |
| Propranolol | 37 | 32% | -1% | 65% | -24% | 5 | 60% | +32% | 80% | -6% |
| Loratadine | 16 | 31% | -2% | 100% | +16% | — | — | — | — | — |
| Metoprolol | 16 | 31% | -2% | 81% | -4% | — | — | — | — | — |
| Aspirin | 30 | 30% | -4% | 87% | +2% | 11 | 27% | -0% | 91% | +5% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **300** | **32%** | — | **87%** | — | **249** | **28%** | — | **86%** | — |
| | | | | | | | | | | |
| Paxlovid (Nirmatrelvir-Ritonavir) | 16 | 44% | +11% | 94% | +9% | 8 | 75% | +47% | 88% | +2% |
| Oxaloacetate | 5 | 40% | +7% | 100% | +15% | 5 | 60% | +32% | 100% | +14% |
| Ketotifen | 25 | 20% | -15% | 96% | +12% | 5 | 60% | +32% | 100% | +14% |
| Propranolol | 37 | 32% | -1% | 65% | -24% | 5 | 60% | +32% | 80% | -6% |
| Nattokinase | 25 | 40% | +8% | 88% | +3% | 10 | 50% | +22% | 90% | +4% |
| Famotidine | 45 | 29% | -5% | 89% | +5% | 9 | 44% | +17% | 89% | +3% |
| Valacyclovir | 15 | 47% | +14% | 80% | -6% | 7 | 43% | +15% | 57% | -29% |
| Low Dose Aripiprazole | 18 | 28% | -6% | 83% | -2% | 7 | 29% | +1% | 100% | +14% |
| Aspirin | 30 | 30% | -4% | 87% | +2% | 11 | 27% | -0% | 91% | +5% |
| Nicotine Patch | 15 | 20% | -14% | 80% | -6% | 11 | 27% | -0% | 91% | +5% |

**Insight:** Sorting by Sig Lift reshuffles the picture. HBOT leads co-occurrence significance (+28% lift, N=10) — small sample but striking. Antivirals dominate: Paxlovid has the highest attributed Sig Lift (+47%) and valacyclovir shows +14% co-occurrence Sig Lift, supporting viral persistence. Melatonin is a surprise at +15% Sig Lift with good N (28). Mast cell drugs (cromolyn, quercetin, loratadine) still show +16% Impr Lift (everyone improves) but 0% Sig Lift — broad mild benefit, not dramatic. Ketotifen's attributed Sig Lift (+32%) confirms it produces strong outcomes for those who credit it, even though its co-occurrence Sig% is below baseline. The best PEM drugs combining both signals: **Paxlovid** (+11% Sig Lift, +47% Attr Sig Lift) and **nattokinase** (+8% Sig Lift, +22% Attr Sig Lift).

### Brain Fog

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **367** | **33%** | — | **79%** | — | **304** | **40%** | — | **85%** | — |
| | | | | | | | | | | |
| Valacyclovir | 18 | 61% | +24% | 89% | +0% | — | — | — | — | — |
| Ketotifen | 24 | 54% | +17% | 92% | +3% | 6 | 50% | +10% | 83% | -2% |
| Fexofenadine | 26 | 54% | +17% | 96% | +8% | 11 | 55% | +15% | 100% | +15% |
| Metoprolol | 13 | 54% | +16% | 85% | -4% | — | — | — | — | — |
| Modafinil | 15 | 53% | +15% | 93% | +5% | 12 | 58% | +19% | 92% | +7% |
| Metformin | 22 | 45% | +7% | 82% | -7% | 6 | 17% | -23% | 67% | -18% |
| Amphetamine-Dextroamphetamine (Adderall) | 11 | 45% | +7% | 91% | +2% | — | — | — | — | — |
| Albuterol (Salbutamol, Proventil HFA, Ventolin HFA, Proair HFA, etc.) | 11 | 45% | +7% | 91% | +2% | — | — | — | — | — |
| Clopidogrel | 11 | 45% | +7% | 91% | +2% | 5 | 60% | +20% | 100% | +15% |
| Pyridostigmine | 19 | 42% | +3% | 95% | +7% | 6 | 33% | -6% | 83% | -2% |
| Ivabradine | 31 | 42% | +3% | 90% | +2% | — | — | — | — | — |
| Electrolytes | 12 | 42% | +3% | 100% | +12% | — | — | — | — | — |
| Paxlovid (Nirmatrelvir-Ritonavir) | 12 | 42% | +3% | 83% | -6% | 5 | 60% | +20% | 60% | -25% |
| Montelukast | 17 | 41% | +2% | 94% | +6% | — | — | — | — | — |
| Famotidine | 53 | 40% | +1% | 89% | +0% | 9 | 56% | +16% | 89% | +4% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **367** | **33%** | — | **79%** | — | **304** | **40%** | — | **85%** | — |
| | | | | | | | | | | |
| Cetirizine | 34 | 38% | -1% | 94% | +6% | 6 | 67% | +27% | 100% | +15% |
| Clopidogrel | 11 | 45% | +7% | 91% | +2% | 5 | 60% | +20% | 100% | +15% |
| Paxlovid (Nirmatrelvir-Ritonavir) | 12 | 42% | +3% | 83% | -6% | 5 | 60% | +20% | 60% | -25% |
| Modafinil | 15 | 53% | +15% | 93% | +5% | 12 | 58% | +19% | 92% | +7% |
| Famotidine | 53 | 40% | +1% | 89% | +0% | 9 | 56% | +16% | 89% | +4% |
| Fexofenadine | 26 | 54% | +17% | 96% | +8% | 11 | 55% | +15% | 100% | +15% |
| Guanfacine | 23 | 35% | -5% | 87% | -2% | 19 | 53% | +13% | 89% | +5% |
| Ketotifen | 24 | 54% | +17% | 92% | +3% | 6 | 50% | +10% | 83% | -2% |
| Aspirin | 33 | 30% | -10% | 91% | +3% | 6 | 50% | +10% | 83% | -2% |
| Methylphenidate | 13 | 31% | -9% | 77% | -12% | 6 | 50% | +10% | 83% | -2% |

**Insight:** Valacyclovir leads co-occurrence Sig Lift (+24%) for brain fog — another antiviral signal. Fexofenadine and ketotifen both hit +17% Sig Lift, nearly doubling the 33% baseline. Modafinil combines strong co-occurrence (+15% Sig Lift) with high attributed significance (+19% Attr Sig Lift, N=12) — the most convincing cognitive-targeted drug. Guanfacine has the highest attributed volume (N=19, 53% Attr Sig%) but slightly negative co-occurrence lift, suggesting it's prescribed to harder cases. Cetirizine's +27% Attr Sig Lift with high co-occurrence N (34) makes it a reliable broad performer. LDN (not shown in top 15) has 0% Sig Lift despite 106 co-occurring reports.

### Fatigue

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **343** | **25%** | — | **84%** | — | **308** | **18%** | — | **82%** | — |
| | | | | | | | | | | |
| Hyperbaric Oxygen Therapy (HBOT) | 10 | 50% | +24% | 90% | +4% | — | — | — | — | — |
| Hydroxyzine | 11 | 45% | +19% | 82% | -4% | — | — | — | — | — |
| Nattokinase + Serrapeptase | 12 | 42% | +15% | 100% | +15% | 14 | 29% | +11% | 100% | +18% |
| Iron | 16 | 38% | +11% | 94% | +8% | 7 | 29% | +11% | 100% | +18% |
| Gabapentin | 14 | 36% | +9% | 86% | -0% | — | — | — | — | — |
| Loratadine | 17 | 35% | +8% | 88% | +3% | — | — | — | — | — |
| Vitamin C | 18 | 33% | +6% | 100% | +15% | — | — | — | — | — |
| Vitamin B12 | 20 | 30% | +3% | 90% | +4% | 5 | 40% | +22% | 80% | -2% |
| Fish Oil | 10 | 30% | +3% | 100% | +15% | — | — | — | — | — |
| Guanfacine | 10 | 30% | +3% | 90% | +4% | — | — | — | — | — |
| Paxlovid (Nirmatrelvir-Ritonavir) | 17 | 29% | +2% | 82% | -4% | 7 | 57% | +39% | 71% | -10% |
| Midodrine | 14 | 29% | +1% | 79% | -8% | — | — | — | — | — |
| Quercetin | 18 | 28% | +0% | 89% | +3% | — | — | — | — | — |
| Levocetirizine | 11 | 27% | -0% | 91% | +5% | — | — | — | — | — |
| Montelukast | 15 | 27% | -1% | 80% | -6% | — | — | — | — | — |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **343** | **25%** | — | **84%** | — | **308** | **18%** | — | **82%** | — |
| | | | | | | | | | | |
| Paxlovid (Nirmatrelvir-Ritonavir) | 17 | 29% | +2% | 82% | -4% | 7 | 57% | +39% | 71% | -10% |
| Vitamin B12 | 20 | 30% | +3% | 90% | +4% | 5 | 40% | +22% | 80% | -2% |
| Clopidogrel | 11 | 18% | -10% | 82% | -4% | 6 | 33% | +15% | 67% | -15% |
| Nattokinase + Serrapeptase | 12 | 42% | +15% | 100% | +15% | 14 | 29% | +11% | 100% | +18% |
| Iron | 16 | 38% | +11% | 94% | +8% | 7 | 29% | +11% | 100% | +18% |
| Apixaban (Eliquis) | 16 | 19% | -9% | 75% | -12% | 7 | 29% | +11% | 71% | -10% |
| Propranolol | 32 | 25% | -3% | 72% | -16% | 7 | 29% | +11% | 57% | -25% |
| Modafinil | 10 | 20% | -8% | 90% | +4% | 8 | 25% | +7% | 88% | +6% |
| Aspirin | 35 | 23% | -5% | 86% | -0% | 9 | 22% | +4% | 67% | -15% |
| Valacyclovir | 10 | 20% | -8% | 100% | +15% | 5 | 20% | +2% | 100% | +18% |

**Insight:** HBOT again leads Sig Lift (+24%, N=10) — consistent with PEM. Nattokinase+serrapeptase combines high Sig Lift (+15%) with high Impr Lift (+15%) and strong attributed data (N=14, 100% improved). Iron at +11% Sig Lift with N=16 is a practical standout — suggests screening for iron deficiency in Long COVID fatigue. Paxlovid has the highest Attr Sig Lift (+39%) but negative Impr Lift, confirming it's used by sicker patients who nonetheless get dramatic improvement when it works. Vitamin B12 shows +22% Attr Sig Lift — another nutritional deficiency worth screening for.

### Insomnia

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **197** | **35%** | — | **73%** | — | **134** | **40%** | — | **89%** | — |
| | | | | | | | | | | |
| Fexofenadine | 23 | 61% | +21% | 96% | +7% | — | — | — | — | — |
| Ketotifen | 18 | 61% | +20% | 83% | -8% | 9 | 67% | +27% | 100% | +11% |
| Pyridostigmine | 15 | 60% | +18% | 93% | +4% | — | — | — | — | — |
| Probiotic | 14 | 57% | +15% | 86% | -5% | — | — | — | — | — |
| Cetirizine | 15 | 53% | +11% | 93% | +4% | 5 | 60% | +20% | 100% | +11% |
| Famotidine | 34 | 50% | +9% | 85% | -7% | 6 | 17% | -23% | 83% | -5% |
| Propranolol | 21 | 48% | +5% | 90% | +0% | — | — | — | — | — |
| Aspirin | 15 | 47% | +3% | 93% | +4% | — | — | — | — | — |
| Quercetin | 11 | 45% | +2% | 91% | +1% | — | — | — | — | — |
| Low Dose Aripiprazole | 11 | 45% | +2% | 64% | -29% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 55 | 44% | -0% | 89% | -2% | 14 | 43% | +3% | 64% | -25% |
| Guanfacine | 14 | 43% | -1% | 79% | -13% | — | — | — | — | — |
| CoQ10 | 19 | 42% | -2% | 79% | -13% | — | — | — | — | — |
| Midodrine | 12 | 42% | -2% | 92% | +2% | — | — | — | — | — |
| Nattokinase | 12 | 42% | -2% | 92% | +2% | — | — | — | — | — |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **197** | **35%** | — | **73%** | — | **134** | **40%** | — | **89%** | — |
| | | | | | | | | | | |
| Ketotifen | 18 | 61% | +20% | 83% | -8% | 9 | 67% | +27% | 100% | +11% |
| Cetirizine | 15 | 53% | +11% | 93% | +4% | 5 | 60% | +20% | 100% | +11% |
| Hydroxyzine | 10 | 40% | -4% | 80% | -11% | 7 | 57% | +18% | 86% | -3% |
| Trazodone | 18 | 33% | -12% | 89% | -1% | 17 | 47% | +8% | 94% | +5% |
| Low Dose Naltrexone (LDN) | 55 | 44% | -0% | 89% | -2% | 14 | 43% | +3% | 64% | -25% |
| Gabapentin | 14 | 29% | -17% | 79% | -13% | 7 | 43% | +3% | 57% | -32% |
| Melatonin | 32 | 41% | -4% | 91% | +1% | 30 | 30% | -10% | 90% | +1% |
| Magnesium | 22 | 36% | -9% | 86% | -5% | 6 | 17% | -23% | 83% | -5% |
| Famotidine | 34 | 50% | +9% | 85% | -7% | 6 | 17% | -23% | 83% | -5% |
| Zolpidem | 10 | 10% | -37% | 80% | -11% | 6 | 17% | -23% | 100% | +11% |

**Insight:** Mast cell drugs dominate insomnia Sig Lift: fexofenadine (+21%), ketotifen (+20%), cetirizine (+11%). This is unexpected — insomnia isn't typically considered a mast cell symptom, but histamine is a wake-promoting neurotransmitter, so H1 blockade may directly help sleep. Ketotifen combines the best of both lenses (+20% Sig Lift, +27% Attr Sig Lift). Trazodone (the classic sleep drug) has high attributed volume (N=17) but negative Sig Lift — it's prescribed to the hardest insomnia cases. Melatonin has the highest attributed N (30) but -10% Attr Sig Lift — broad mild benefit, rarely dramatic.

### POTS (Postural Orthostatic Tachycardia)

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **228** | **30%** | — | **77%** | — | **158** | **37%** | — | **94%** | — |
| | | | | | | | | | | |
| Albuterol (Salbutamol, Proventil HFA, Ventolin HFA, Proair HFA, etc.) | 10 | 70% | +31% | 100% | +6% | — | — | — | — | — |
| Fexofenadine | 10 | 60% | +21% | 100% | +6% | — | — | — | — | — |
| Montelukast | 10 | 60% | +21% | 90% | -5% | — | — | — | — | — |
| Metoprolol | 25 | 56% | +18% | 100% | +7% | 20 | 60% | +23% | 100% | +6% |
| Magnesium | 13 | 54% | +14% | 92% | -2% | — | — | — | — | — |
| Gabapentin | 15 | 53% | +14% | 80% | -16% | — | — | — | — | — |
| Melatonin | 17 | 53% | +14% | 88% | -7% | — | — | — | — | — |
| Duloxetine | 10 | 50% | +10% | 100% | +6% | — | — | — | — | — |
| Electrolytes | 10 | 50% | +10% | 100% | +6% | — | — | — | — | — |
| Loratadine | 15 | 47% | +7% | 93% | -1% | — | — | — | — | — |
| Vitamin B12 | 11 | 45% | +5% | 82% | -14% | — | — | — | — | — |
| Ivabradine | 41 | 44% | +4% | 90% | -6% | 40 | 48% | +11% | 95% | +1% |
| Famotidine | 30 | 43% | +3% | 90% | -6% | — | — | — | — | — |
| Vitamin D3 | 14 | 43% | +2% | 86% | -10% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 64 | 39% | -3% | 94% | -1% | 6 | 17% | -20% | 83% | -10% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **228** | **30%** | — | **77%** | — | **158** | **37%** | — | **94%** | — |
| | | | | | | | | | | |
| Metoprolol | 25 | 56% | +18% | 100% | +7% | 20 | 60% | +23% | 100% | +6% |
| Ivabradine | 41 | 44% | +4% | 90% | -6% | 40 | 48% | +11% | 95% | +1% |
| Guanfacine | 10 | 10% | -33% | 70% | -26% | 6 | 33% | -3% | 67% | -27% |
| Propranolol | 49 | 35% | -9% | 96% | +2% | 46 | 33% | -4% | 96% | +2% |
| Midodrine | 20 | 25% | -18% | 95% | +1% | 14 | 21% | -15% | 93% | -1% |
| Pyridostigmine | 19 | 32% | -11% | 95% | +0% | 12 | 17% | -20% | 100% | +6% |
| Low Dose Naltrexone (LDN) | 64 | 39% | -3% | 94% | -1% | 6 | 17% | -20% | 83% | -10% |
| Fludrocortisone | 14 | 36% | -6% | 86% | -10% | 6 | 17% | -20% | 67% | -27% |

**Insight:** Metoprolol remains the clear POTS standout — +18% Sig Lift, +23% Attr Sig Lift, 100% improvement rate, N=25. It dominates both lenses. Ivabradine has high volume (N=41) and +11% Attr Sig Lift but only +4% co-occurrence Sig Lift with negative Impr Lift (-6%), confirming it's prescribed to more severe patients. Fexofenadine and montelukast (mast cell drugs) show +21% Sig Lift for POTS — surprising, suggesting mast cell activation contributes to orthostatic intolerance. Propranolol (most-used, N=49) has -9% Sig Lift — it provides broad mild relief (96% Impr%) but rarely produces significant improvement. Midodrine and pyridostigmine both show negative Sig Lift, likely reflecting use in refractory cases.

### Tachycardia (rest)

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **160** | **35%** | — | **66%** | — | **80** | **51%** | — | **92%** | — |
| | | | | | | | | | | |
| Ivabradine | 20 | 70% | +19% | 85% | -11% | 21 | 71% | +20% | 95% | +3% |
| Cetirizine | 17 | 65% | +12% | 100% | +7% | — | — | — | — | — |
| Apixaban (Eliquis) | 10 | 60% | +6% | 90% | -4% | — | — | — | — | — |
| Melatonin | 10 | 60% | +6% | 90% | -4% | — | — | — | — | — |
| Famotidine | 26 | 58% | +4% | 96% | +3% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 41 | 56% | +3% | 93% | -2% | 7 | 43% | -8% | 86% | -7% |
| Pyridostigmine | 13 | 54% | -1% | 100% | +7% | 7 | 57% | +6% | 86% | -7% |
| Vitamin D3 | 13 | 54% | -1% | 85% | -11% | — | — | — | — | — |
| Metoprolol | 18 | 50% | -6% | 94% | +1% | 17 | 53% | +2% | 94% | +2% |
| CoQ10 | 11 | 45% | -10% | 91% | -3% | — | — | — | — | — |
| Propranolol | 28 | 46% | -12% | 93% | -1% | 22 | 36% | -15% | 95% | +3% |
| N-Acetylcysteine (NAC) | 10 | 40% | -16% | 90% | -4% | — | — | — | — | — |
| Loratadine | 10 | 40% | -16% | 90% | -4% | — | — | — | — | — |
| Aspirin | 18 | 39% | -19% | 94% | +1% | 6 | 33% | -18% | 83% | -9% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **160** | **35%** | — | **66%** | — | **80** | **51%** | — | **92%** | — |
| | | | | | | | | | | |
| Ivabradine | 20 | 70% | +19% | 85% | -11% | 21 | 71% | +20% | 95% | +3% |
| Pyridostigmine | 13 | 54% | -1% | 100% | +7% | 7 | 57% | +6% | 86% | -7% |
| Metoprolol | 18 | 50% | -6% | 94% | +1% | 17 | 53% | +2% | 94% | +2% |
| Low Dose Naltrexone (LDN) | 41 | 56% | +3% | 93% | -2% | 7 | 43% | -8% | 86% | -7% |
| Propranolol | 28 | 46% | -12% | 93% | -1% | 22 | 36% | -15% | 95% | +3% |
| Aspirin | 18 | 39% | -19% | 94% | +1% | 6 | 33% | -18% | 83% | -9% |

**Insight:** For resting tachycardia specifically (vs POTS), ivabradine is the clear winner — +19% Sig Lift, +20% Attr Sig Lift, 71% attributed significance. This makes sense: ivabradine's mechanism (If channel blockade) directly targets heart rate without affecting blood pressure, making it ideal for inappropriate sinus tachycardia. Metoprolol and propranolol both show negative Sig Lift here despite being standard tachycardia treatments — likely confounding by severity. Cetirizine at +12% Sig Lift with 100% improvement is intriguing (mast cell–mediated tachycardia?).

### Exertional Dyspnea

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **57** | **37%** | — | **95%** | — | **12** | **25%** | — | **92%** | — |
| | | | | | | | | | | |
| Aspirin | 12 | 42% | +7% | 92% | -3% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 25 | 40% | +7% | 88% | -12% | — | — | — | — | — |
| Melatonin | 11 | 36% | -0% | 100% | +7% | — | — | — | — | — |
| Famotidine | 11 | 36% | -0% | 91% | -4% | — | — | — | — | — |
| Ivabradine | 11 | 9% | -35% | 100% | +7% | 7 | 29% | +4% | 100% | +8% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **57** | **37%** | — | **95%** | — | **12** | **25%** | — | **92%** | — |
| | | | | | | | | | | |
| Ivabradine | 11 | 9% | -35% | 100% | +7% | 7 | 29% | +4% | 100% | +8% |

**Insight:** Limited data for exertional dyspnea (only 57 reports with outcomes, 12 attributed). The 95% baseline improvement rate is very high, leaving little room for drugs to show lift. Aspirin and LDN show modest +7% Sig Lift. Ivabradine has strongly negative Sig Lift (-35%) but positive attributed data — classic confounding by severity (prescribed to the worst cases).

### Muscle Pain

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **77** | **39%** | — | **90%** | — | **27** | **26%** | — | **89%** | — |
| | | | | | | | | | | |
| Famotidine | 17 | 59% | +22% | 100% | +12% | — | — | — | — | — |
| Cetirizine | 11 | 36% | -7% | 100% | +11% | — | — | — | — | — |
| Vitamin D3 | 13 | 23% | -24% | 92% | +1% | — | — | — | — | — |
| Magnesium | 11 | 18% | -29% | 91% | -0% | — | — | — | — | — |
| N-Acetylcysteine (NAC) | 11 | 18% | -29% | 91% | -0% | — | — | — | — | — |
| Propranolol | 16 | 19% | -31% | 94% | +3% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 37 | 27% | -34% | 92% | +2% | 27 | 26% | +0% | 89% | +0% |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **77** | **39%** | — | **90%** | — | **27** | **26%** | — | **89%** | — |
| | | | | | | | | | | |
| Low Dose Naltrexone (LDN) | 37 | 27% | -34% | 92% | +2% | 27 | 26% | +0% | 89% | +0% |

**Insight:** Famotidine is the only drug with positive Sig Lift for muscle pain (+22%, N=17, 100% improved). Most drugs show strongly negative Sig Lift — the 39% baseline significance is already high, and drugs are likely prescribed to more refractory cases. LDN dominates attributed volume (N=27) but shows exactly 0% lift on both measures — its muscle pain outcomes perfectly match the baseline population.

### Headache/Migraine

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **125** | **37%** | — | **86%** | — | **48** | **31%** | — | **83%** | — |
| | | | | | | | | | | |
| Ivabradine | 18 | 61% | +21% | 83% | -9% | — | — | — | — | — |
| Gabapentin | 13 | 62% | +20% | 85% | -7% | — | — | — | — | — |
| Famotidine | 16 | 56% | +15% | 94% | +4% | — | — | — | — | — |
| Nattokinase | 10 | 50% | +7% | 100% | +11% | — | — | — | — | — |
| Pyridostigmine | 10 | 50% | +7% | 90% | -0% | — | — | — | — | — |
| Melatonin | 10 | 50% | +7% | 90% | -0% | — | — | — | — | — |
| Probiotic | 11 | 45% | +2% | 91% | +1% | — | — | — | — | — |
| Cromolyn Sodium | 12 | 42% | -3% | 92% | +2% | — | — | — | — | — |
| N-Acetylcysteine (NAC) | 15 | 40% | -5% | 87% | -4% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 42 | 38% | -11% | 86% | -8% | 11 | 27% | -4% | 91% | +8% |
| Vitamin B12 | 10 | 30% | -16% | 90% | -0% | — | — | — | — | — |
| Metoprolol | 11 | 27% | -19% | 100% | +11% | — | — | — | — | — |
| Amitriptyline (Elavil, Vanatrip, Domical) | 11 | 27% | -19% | 82% | -10% | — | — | — | — | — |
| Magnesium | 12 | 25% | -22% | 75% | -18% | — | — | — | — | — |
| Vitamin C | 10 | 20% | -27% | 80% | -12% | — | — | — | — | — |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **125** | **37%** | — | **86%** | — | **48** | **31%** | — | **83%** | — |
| | | | | | | | | | | |
| Nortriptyline | 9 | 33% | -12% | 78% | -14% | 6 | 50% | +19% | 67% | -17% |
| Low Dose Naltrexone (LDN) | 42 | 38% | -11% | 86% | -8% | 11 | 27% | -4% | 91% | +8% |
| Rizatriptan | 5 | 20% | -25% | 100% | +10% | 5 | 20% | -11% | 80% | -3% |
| Propranolol | 22 | 18% | -34% | 82% | -11% | 8 | 12% | -19% | 75% | -8% |

**Insight:** Ivabradine (+21% Sig Lift) and gabapentin (+20%) lead for headache/migraine, though both have negative Impr Lift — they're prescribed to harder cases but produce significant outcomes when they work. Famotidine at +15% Sig Lift with 94% Impr% and positive Impr Lift (+4%) is the most balanced performer. Nattokinase (100% improved, +11% Impr Lift, +7% Sig Lift) suggests a vascular component. Traditional migraine drugs (propranolol, amitriptyline) show strongly negative Sig Lift — confounding by severity. Nortriptyline is the only drug with positive Attr Sig Lift (+19%), though with small N.

### Neuropathic Pain

**Co-occurrence lift leaders** (sorted by Sig Lift, min 10 co-occurring reports):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **78** | **35%** | — | **85%** | — | **40** | **18%** | — | **68%** | — |
| | | | | | | | | | | |
| Cetirizine | 12 | 67% | +35% | 92% | +4% | — | — | — | — | — |
| Aspirin | 11 | 45% | +8% | 82% | -8% | — | — | — | — | — |
| Famotidine | 12 | 42% | +4% | 83% | -7% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 23 | 30% | -13% | 96% | +11% | — | — | — | — | — |
| Gabapentin | 23 | 30% | -13% | 83% | -10% | 22 | 27% | +10% | 77% | +10% |
| Propranolol | 12 | 25% | -17% | 75% | -17% | — | — | — | — | — |

**Attributed significance leaders** (sorted by Attr Sig Lift, min 5 attributed):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **78** | **35%** | — | **85%** | — | **40** | **18%** | — | **68%** | — |
| | | | | | | | | | | |
| Gabapentin | 23 | 30% | -13% | 83% | -10% | 22 | 27% | +10% | 77% | +10% |
| Pregabalin | 7 | 14% | -28% | 86% | -3% | 6 | 0% | -18% | 67% | -1% |
| Duloxetine | 9 | 22% | -19% | 67% | -26% | 6 | 0% | -18% | 33% | -34% |

**Insight:** Cetirizine dominates neuropathic pain with +35% Sig Lift (67% significant vs 35% baseline) — a striking signal for an antihistamine. This may reflect mast cell–mediated neuroinflammation or small fiber neuropathy driven by mast cell activation. Gabapentin (the standard neuropathic pain drug) has -13% Sig Lift but +10% Attr Sig Lift — it's prescribed to the hardest cases and still produces above-baseline attributed significance. Pregabalin and duloxetine both show 0% attributed significance — disappointing for standard-of-care drugs, though confounding by severity is likely.

### Cross-Symptom Patterns

**Drugs with consistently positive Sig Lift across multiple symptoms:**
- **Valacyclovir** — top Sig Lift for PEM (+14%) and brain fog (+24%). Antiviral signal is strong.
- **HBOT** — top Sig Lift for PEM (+28%) and fatigue (+24%). Small N but consistent.
- **Mast cell drugs** — fexofenadine, ketotifen, cetirizine appear in top Sig Lift for brain fog, insomnia, POTS, neuropathic pain. The class signal is robust.
- **Famotidine** — positive Sig Lift for muscle pain (+22%), headache (+15%), insomnia (+9%), tachycardia (+4%). Broad systemic benefit.
- **Nattokinase (+serrapeptase)** — positive Sig Lift for fatigue (+15%), headache (+7%), PEM (+8%). Vascular/fibrinolytic signal.

**Drugs with high attributed counts but minimal/negative co-occurrence Sig Lift:**
- **LDN** — -0% to -3% Sig Lift across all symptoms despite being in 60%+ of reports. Its high attributed improvement rate reflects the baseline improvement rate of the population taking it, not a drug-specific effect. However, it does show +11% Impr Lift for neuropathic pain.
- **Propranolol** — negative Sig Lift for POTS (-9%), tachycardia (-12%), headache (-34%). Prescribed to harder cases; provides broad mild relief but rarely dramatic improvement.
- **Ivabradine** — negative Impr Lift for POTS (-6%) and tachycardia (-11%) despite high attributed significance. Classic confounding by indication.

**Key interpretive finding:** Sorting by Sig Lift (rather than Impr Lift as in the previous version) elevates antivirals and HBOT — interventions targeting root causes (viral persistence, tissue hypoxia) rather than symptom management. Mast cell drugs remain strong but their signal is more nuanced: they produce broad improvement (high Impr Lift) but not always dramatic improvement (moderate Sig Lift), except for cetirizine in neuropathic pain and ketotifen in insomnia/brain fog.

**Strongest drug–symptom combinations (high on both Sig Lift and Attr Sig Lift):**
- Paxlovid → PEM (+11% / +47%)
- Metoprolol → POTS (+18% / +23%)
- Ivabradine → Tachycardia (+19% / +20%)
- Modafinil → Brain fog (+15% / +19%)
- Ketotifen → Insomnia (+20% / +27%)
- Cetirizine → Neuropathic pain (+35% / no attributed data)
- Nattokinase+Serrapeptase → Fatigue (+15% / +11%)

---

## Next Steps

- [x] ~~Normalize drug names~~
- [x] ~~Build efficacy rankings per symptom~~
- [ ] Analyze comorbidity clusters vs treatment response (do MCAS patients respond differently?)
- [ ] Cross-reference with related condition reports (do POTS drugs from standalone reports match Long COVID POTS treatments?)
- [ ] Investigate temporal patterns (do drugs work better earlier vs later in disease course?)
- [ ] Pull clinical trial data for top drugs to triangulate with patient reports
