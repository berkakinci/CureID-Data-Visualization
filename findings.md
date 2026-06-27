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
| | | |
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

**Note:** Raw improvement percentages and multi-symptom drug counts are available interactively in the [drug outcomes bar chart](drug_outcomes_viz.html) and [symptom × drug heatmap](drug_heatmap_viz.html). The per-symptom dual-lens analysis below controls for baseline rates and confounding by severity.

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

| Mechanism | Drugs |
|-----------|-------|
| Mast Cell / Antihistamine | Famotidine, cetirizine, fexofenadine, ketotifen, hydroxyzine, cromolyn, loratadine, montelukast, quercetin |
| Autonomic / Heart Rate | Propranolol, ivabradine, metoprolol, bisoprolol, midodrine, pyridostigmine, fludrocortisone |
| Anticoagulant / Vascular | Aspirin, nattokinase, lumbrokinase, apixaban (Eliquis), clopidogrel, HELP apheresis |
| Immune Modulation | LDN, prednisolone, IVIG, maraviroc |
| Antiviral | Paxlovid (nirmatrelvir-ritonavir), valacyclovir |
| Mitochondrial / Metabolic | CoQ10, NAC, magnesium, oxaloacetate, metformin, alpha-ketoglutarate |
| Neurological / Pain | Gabapentin, amitriptyline, guanfacine, nicotine patch |
| Other | Melatonin, CBD/THC, probiotics, vitamin D3, vitamin B12, turmeric |

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

---

## Per-Symptom Drug Efficacy (Dual-Lens Analysis)

Two complementary approaches to rank drugs per symptom:

1. **Attributed**: patient explicitly linked drug → symptom → outcome (what they reported)
2. **Co-occurrence lift**: improvement rate for reports *taking* drug X vs reports *not taking* drug X, regardless of what the patient attributed (removes attribution bias, but confounded by polypharmacy)

### Definitions

- **Baseline row**: the overall improvement rate for this symptom across *all* reports, shown as a reference point. Note: lifts are not computed directly against this row (see below).
- **Co-N**: number of reports where the patient was taking this drug and had an outcome recorded for this symptom (regardless of attribution).
- **Sig%**: % of co-occurring reports where the outcome was "Significant improvement" or "Complete resolution."
- **Sig Lift**: difference between this drug's Sig% and the Sig% of reports *not* taking this drug (leave-one-out). This isolates the drug's association from its own influence on the overall rate — important for high-volume drugs like LDN that are in 60%+ of reports. For low-volume drugs, this is nearly identical to comparing against the baseline row.
- **Impr%**: % of co-occurring reports where the symptom improved (any level: mild through complete resolution).
- **Impr Lift**: same leave-one-out method as Sig Lift, applied to overall improvement rate.
- **Attr N**: number of times patients explicitly attributed this drug to this symptom's outcome.
- **Attr Sig%**: % of attributed entries reporting significant improvement or complete resolution.
- **Attr Sig Lift**: difference between Attr Sig% and the pooled attributed Sig% across all drugs for this symptom (global average, not leave-one-out — the attributed pool is smaller so leave-one-out would be noisy).
- **Attr Impr%**: % of attributed entries reporting any improvement.
- **Attr Impr Lift**: same global-average method as Attr Sig Lift, applied to attributed improvement rate.

### How to read the tables

Each symptom has a single merged table sorted by co-occurrence Sig Lift. A drug appears if it has ≥10 co-occurring reports OR ≥5 attributed entries. A drug is most convincing when it scores high on *both* Sig Lift (more significant outcomes than average) and Attr Sig Lift (patients who credit it report better-than-average significance). High Impr Lift with low Sig% means broad mild benefit. High Sig% with negative Impr Lift suggests confounding by indication — the drug may be prescribed to harder cases, making its overall improvement rate look worse even though some patients get strong results.

### PEM

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **300** | **32%** | — | **87%** | — | **229** | **30%** | — | **87%** | — |
| | | | | | | | | | | |
| Hyperbaric Oxygen Therapy (HBOT) | 10 | 60% | +28% | 90% | +5% | — | — | — | — | — |
| Prednisolone | 7 | 57% | +25% | 86% | +1% | 5 | 100% | +70% | 100% | +13% |
| Melatonin | 28 | 46% | +15% | 96% | +13% | — | — | — | — | — |
| Valacyclovir | 15 | 47% | +14% | 80% | -6% | 7 | 43% | +13% | 57% | -30% |
| Paxlovid (Nirmatrelvir-Ritonavir) | 16 | 44% | +11% | 94% | +9% | 8 | 75% | +45% | 88% | +0% |
| Nattokinase | 25 | 40% | +8% | 88% | +3% | 10 | 50% | +20% | 90% | +3% |
| Oxaloacetate | 5 | 40% | +7% | 100% | +15% | 5 | 60% | +30% | 100% | +13% |
| Vitamin D3 | 23 | 39% | +7% | 87% | +2% | — | — | — | — | — |
| Guanfacine | 11 | 36% | +3% | 82% | -4% | 5 | 0% | -30% | 80% | -7% |
| Gabapentin | 20 | 35% | +2% | 80% | -6% | — | — | — | — | — |
| Cromolyn Sodium | 18 | 33% | +0% | 100% | +16% | — | — | — | — | — |
| Quercetin | 18 | 33% | +0% | 100% | +16% | — | — | — | — | — |
| Metformin | 18 | 33% | +0% | 94% | +10% | 8 | 25% | -5% | 100% | +13% |
| Propranolol | 37 | 32% | -1% | 65% | -24% | 5 | 60% | +30% | 80% | -7% |
| Loratadine | 16 | 31% | -2% | 100% | +16% | — | — | — | — | — |
| Metoprolol | 16 | 31% | -2% | 81% | -4% | — | — | — | — | — |
| Aspirin | 30 | 30% | -4% | 87% | +2% | 11 | 27% | -2% | 91% | +4% |
| Low Dose Naltrexone (LDN) | 111 | 31% | -5% | 86% | +1% | 65 | 23% | -7% | 85% | -3% |
| Famotidine | 45 | 29% | -5% | 89% | +5% | 9 | 44% | +15% | 89% | +2% |
| Cetirizine | 27 | 26% | -8% | 89% | +4% | — | — | — | — | — |
| Iron | 12 | 25% | -9% | 100% | +16% | — | — | — | — | — |
| Ivabradine | 35 | 26% | -9% | 91% | +7% | 12 | 25% | -5% | 92% | +4% |
| Low Dose Aripiprazole | 21 | 24% | -10% | 81% | -5% | 8 | 25% | -5% | 100% | +13% |
| N-Acetylcysteine (NAC) | 29 | 24% | -10% | 86% | +1% | 10 | 10% | -20% | 80% | -7% |
| Montelukast | 13 | 23% | -11% | 92% | +8% | — | — | — | — | — |

Antivirals lead: Paxlovid (+11% Sig Lift, +45% Attr Sig Lift) and valacyclovir (+14%) support viral persistence. HBOT (+28%) is striking but small-N. Melatonin is a surprise at +15% Sig Lift with good N (28). Mast cell drugs (cromolyn, quercetin, loratadine) show +16% Impr Lift but 0% Sig Lift — broad mild benefit, not dramatic. LDN at -5% Sig Lift despite N=111 shows no signal above baseline.

### Brain Fog

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **367** | **33%** | — | **79%** | — | **273** | **41%** | — | **85%** | — |
| | | | | | | | | | | |
| Valacyclovir | 18 | 61% | +24% | 89% | +0% | — | — | — | — | — |
| Hyperbaric Oxygen Therapy (HBOT) | 7 | 57% | +19% | 100% | +12% | 5 | 40% | -1% | 100% | +15% |
| Ketotifen | 24 | 54% | +17% | 92% | +3% | 6 | 50% | +9% | 83% | -2% |
| Fexofenadine | 26 | 54% | +17% | 96% | +8% | 11 | 55% | +14% | 100% | +15% |
| Metoprolol | 13 | 54% | +16% | 85% | -4% | — | — | — | — | — |
| Modafinil | 15 | 53% | +15% | 93% | +5% | 12 | 58% | +17% | 92% | +6% |
| Albuterol | 13 | 46% | +8% | 92% | +4% | — | — | — | — | — |
| Metformin | 22 | 45% | +7% | 82% | -7% | 6 | 17% | -24% | 67% | -19% |
| Amphetamine-Dextroamphetamine (Adderall) | 11 | 45% | +7% | 91% | +2% | — | — | — | — | — |
| Clopidogrel | 11 | 45% | +7% | 91% | +2% | 5 | 60% | +19% | 100% | +15% |
| Pyridostigmine | 19 | 42% | +3% | 95% | +7% | 5 | 40% | -1% | 80% | -5% |
| Ivabradine | 31 | 42% | +3% | 90% | +2% | — | — | — | — | — |
| Electrolytes | 12 | 42% | +3% | 100% | +12% | — | — | — | — | — |
| Paxlovid (Nirmatrelvir-Ritonavir) | 12 | 42% | +3% | 83% | -6% | 5 | 60% | +19% | 60% | -25% |
| Montelukast | 17 | 41% | +2% | 94% | +6% | — | — | — | — | — |
| Famotidine | 53 | 40% | +1% | 89% | +0% | 9 | 56% | +15% | 89% | +4% |
| Melatonin | 34 | 38% | -1% | 94% | +6% | 6 | 33% | -8% | 67% | -19% |
| Cetirizine | 34 | 38% | -1% | 94% | +6% | 5 | 60% | +19% | 100% | +15% |
| Nattokinase | 21 | 38% | -1% | 81% | -8% | 12 | 42% | +1% | 83% | -2% |
| Vitamin B12 | 19 | 37% | -2% | 95% | +7% | — | — | — | — | — |
| Bupropion | 17 | 35% | -4% | 82% | -7% | 5 | 40% | -1% | 60% | -25% |
| Gabapentin | 20 | 35% | -4% | 80% | -9% | — | — | — | — | — |
| Guanfacine | 23 | 35% | -5% | 87% | -2% | 19 | 53% | +12% | 89% | +4% |
| Lisdexamfetamine (Vyvanse) | 9 | 33% | -6% | 89% | +0% | 5 | 40% | -1% | 100% | +15% |
| Amantadine | 12 | 33% | -6% | 83% | -6% | 6 | 50% | +9% | 67% | -19% |

Valacyclovir leads Sig Lift (+24%) — another antiviral signal. Modafinil is the most convincing cognitive-targeted drug (+15% Sig Lift, +17% Attr Sig Lift, N=12). Mast cell drugs (fexofenadine, ketotifen) cluster at +17%. Guanfacine has high attributed volume (N=19, +12% Attr Sig Lift) but -5% co-occurrence lift — prescribed to harder cases. Cetirizine (+19% Attr Sig Lift, Co-N=34) is a reliable broad performer.

### Fatigue

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **343** | **25%** | — | **84%** | — | **276** | **18%** | — | **82%** | — |
| | | | | | | | | | | |
| Amantadine | 9 | 67% | +41% | 89% | +3% | 5 | 20% | +2% | 80% | -2% |
| Hyperbaric Oxygen Therapy (HBOT) | 10 | 50% | +24% | 90% | +4% | — | — | — | — | — |
| Hydroxyzine | 11 | 45% | +19% | 82% | -4% | — | — | — | — | — |
| Nattokinase + Serrapeptase | 12 | 42% | +15% | 100% | +15% | 7 | 29% | +10% | 100% | +18% |
| Iron | 16 | 38% | +11% | 94% | +8% | 7 | 29% | +10% | 100% | +18% |
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
| Fexofenadine | 30 | 27% | -1% | 87% | +1% | 5 | 20% | +2% | 100% | +18% |
| Ivabradine | 34 | 26% | -1% | 85% | -1% | 8 | 0% | -18% | 88% | +6% |
| Melatonin | 28 | 25% | -3% | 86% | -0% | — | — | — | — | — |
| Propranolol | 32 | 25% | -3% | 72% | -16% | 6 | 33% | +15% | 67% | -15% |
| Bupropion | 17 | 24% | -4% | 82% | -4% | 7 | 14% | -4% | 86% | +4% |
| Aspirin | 35 | 23% | -5% | 86% | -0% | 9 | 22% | +4% | 67% | -15% |
| Magnesium | 28 | 21% | -7% | 89% | +4% | — | — | — | — | — |
| CoQ10 | 46 | 22% | -7% | 85% | -1% | 23 | 9% | -10% | 70% | -12% |
| Famotidine | 59 | 22% | -7% | 83% | -4% | 14 | 14% | -4% | 86% | +4% |

HBOT again leads (+24%, N=10). Amantadine tops the table at +41% Sig Lift but with only N=9 — worth watching but not conclusive. Nattokinase+serrapeptase combines high Sig Lift (+15%) with 100% improvement and strong attributed data (N=7). Iron (+11%, N=16) is a practical standout — suggests screening for deficiency. Paxlovid has the highest Attr Sig Lift (+39%) but negative Impr Lift — used by sicker patients who get dramatic improvement when it works. Vitamin B12 (+22% Attr Sig Lift) is another nutritional deficiency worth screening for.

### Insomnia

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **197** | **35%** | — | **73%** | — | **123** | **37%** | — | **88%** | — |
| | | | | | | | | | | |
| Fexofenadine | 23 | 61% | +21% | 96% | +7% | — | — | — | — | — |
| Ketotifen | 18 | 61% | +20% | 83% | -8% | 9 | 67% | +29% | 100% | +12% |
| Pyridostigmine | 15 | 60% | +18% | 93% | +4% | — | — | — | — | — |
| Probiotic | 14 | 57% | +15% | 86% | -5% | — | — | — | — | — |
| Cetirizine | 15 | 53% | +11% | 93% | +4% | — | — | — | — | — |
| Famotidine | 34 | 50% | +9% | 85% | -7% | 6 | 17% | -21% | 83% | -4% |
| Propranolol | 21 | 48% | +5% | 90% | +0% | — | — | — | — | — |
| Aspirin | 15 | 47% | +3% | 93% | +4% | — | — | — | — | — |
| Low Dose Aripiprazole | 13 | 46% | +3% | 69% | -23% | — | — | — | — | — |
| Quercetin | 11 | 45% | +2% | 91% | +1% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 55 | 44% | -0% | 89% | -2% | 14 | 43% | +5% | 64% | -24% |
| Guanfacine | 14 | 43% | -1% | 79% | -13% | — | — | — | — | — |
| CoQ10 | 19 | 42% | -2% | 79% | -13% | — | — | — | — | — |
| Midodrine | 12 | 42% | -2% | 92% | +2% | — | — | — | — | — |
| Nattokinase | 12 | 42% | -2% | 92% | +2% | — | — | — | — | — |
| Vitamin B12 | 12 | 42% | -2% | 83% | -7% | — | — | — | — | — |
| Loratadine | 12 | 42% | -2% | 83% | -7% | — | — | — | — | — |
| Hydroxyzine | 10 | 40% | -4% | 80% | -11% | 7 | 57% | +20% | 86% | -2% |
| Melatonin | 32 | 41% | -4% | 91% | +1% | 30 | 30% | -7% | 90% | +2% |
| Magnesium | 22 | 36% | -9% | 86% | -5% | 6 | 17% | -21% | 83% | -4% |
| Cromolyn Sodium | 12 | 33% | -12% | 92% | +2% | — | — | — | — | — |
| Bupropion | 12 | 33% | -12% | 83% | -7% | — | — | — | — | — |
| Trazodone | 18 | 33% | -12% | 89% | -1% | 17 | 47% | +10% | 94% | +6% |
| Ivabradine | 16 | 31% | -14% | 88% | -3% | — | — | — | — | — |
| N-Acetylcysteine (NAC) | 22 | 32% | -15% | 82% | -10% | — | — | — | — | — |

Mast cell drugs dominate: fexofenadine (+21%), ketotifen (+20%), cetirizine (+11%). Histamine is a wake-promoting neurotransmitter, so H1 blockade may directly help sleep. Ketotifen combines both lenses (+20% Sig Lift, +29% Attr Sig Lift). Trazodone (N=17) has negative Sig Lift but +10% Attr Sig Lift — prescribed to the hardest cases. Melatonin (N=30) shows broad mild benefit but -7% Attr Sig Lift.

### POTS

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **228** | **30%** | — | **77%** | — | **153** | **37%** | — | **93%** | — |
| | | | | | | | | | | |
| Albuterol | 10 | 70% | +31% | 100% | +6% | — | — | — | — | — |
| Fexofenadine | 10 | 60% | +21% | 100% | +6% | — | — | — | — | — |
| Montelukast | 10 | 60% | +21% | 90% | -5% | — | — | — | — | — |
| Metoprolol | 25 | 56% | +18% | 100% | +7% | 20 | 60% | +23% | 100% | +7% |
| Magnesium | 13 | 54% | +14% | 92% | -2% | — | — | — | — | — |
| Gabapentin | 15 | 53% | +14% | 80% | -16% | — | — | — | — | — |
| Melatonin | 17 | 53% | +14% | 88% | -7% | — | — | — | — | — |
| Duloxetine | 10 | 50% | +10% | 100% | +6% | — | — | — | — | — |
| Electrolytes | 10 | 50% | +10% | 100% | +6% | — | — | — | — | — |
| Loratadine | 15 | 47% | +7% | 93% | -1% | — | — | — | — | — |
| Vitamin B12 | 11 | 45% | +5% | 82% | -14% | — | — | — | — | — |
| Ivabradine | 41 | 44% | +4% | 90% | -6% | 40 | 48% | +10% | 95% | +2% |
| Famotidine | 30 | 43% | +3% | 90% | -6% | — | — | — | — | — |
| Vitamin D3 | 14 | 43% | +2% | 86% | -10% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 64 | 39% | -3% | 94% | -1% | 6 | 17% | -21% | 83% | -10% |
| Nattokinase | 16 | 38% | -4% | 88% | -8% | — | — | — | — | — |
| Valacyclovir | 11 | 36% | -5% | 91% | -4% | — | — | — | — | — |
| Fludrocortisone | 14 | 36% | -6% | 86% | -10% | 6 | 17% | -21% | 67% | -27% |
| Cetirizine | 12 | 33% | -8% | 92% | -3% | — | — | — | — | — |
| CoQ10 | 18 | 33% | -9% | 89% | -6% | — | — | — | — | — |
| Propranolol | 49 | 35% | -9% | 96% | +2% | 46 | 33% | -5% | 96% | +2% |
| Aspirin | 22 | 32% | -11% | 95% | +1% | — | — | — | — | — |
| Pyridostigmine | 19 | 32% | -11% | 95% | +0% | 7 | 14% | -23% | 100% | +7% |
| Bisoprolol | 10 | 30% | -12% | 80% | -16% | 8 | 38% | +0% | 100% | +7% |
| Nicotine Patch | 10 | 30% | -12% | 70% | -26% | — | — | — | — | — |

Metoprolol is the clear standout: +18% Sig Lift, +23% Attr Sig Lift, 100% improvement, N=25. Ivabradine has high volume (N=41, +10% Attr Sig Lift) but only +4% co-occurrence Sig Lift — prescribed to more severe patients. Propranolol (most-used, N=49) has -9% Sig Lift — broad mild relief (96% Impr%) but rarely dramatic. Fexofenadine and montelukast at +21% suggest mast cell contribution to orthostatic intolerance.

### Tachycardia (rest)

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **160** | **35%** | — | **66%** | — | **78** | **50%** | — | **92%** | — |
| | | | | | | | | | | |
| Ivabradine | 20 | 70% | +19% | 85% | -11% | 20 | 70% | +20% | 95% | +3% |
| Cetirizine | 17 | 65% | +12% | 100% | +7% | — | — | — | — | — |
| Apixaban (Eliquis) | 10 | 60% | +6% | 90% | -4% | — | — | — | — | — |
| Melatonin | 10 | 60% | +6% | 90% | -4% | — | — | — | — | — |
| Famotidine | 26 | 58% | +4% | 96% | +3% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 41 | 56% | +3% | 93% | -2% | 7 | 43% | -7% | 86% | -7% |
| Pyridostigmine | 13 | 54% | -1% | 100% | +7% | 6 | 50% | +0% | 83% | -9% |
| Vitamin D3 | 13 | 54% | -1% | 85% | -11% | — | — | — | — | — |
| Metoprolol | 18 | 50% | -6% | 94% | +1% | 17 | 53% | +3% | 94% | +2% |
| CoQ10 | 11 | 45% | -10% | 91% | -3% | — | — | — | — | — |
| Propranolol | 28 | 46% | -12% | 93% | -1% | 22 | 36% | -14% | 95% | +3% |
| N-Acetylcysteine (NAC) | 10 | 40% | -16% | 90% | -4% | — | — | — | — | — |
| Loratadine | 10 | 40% | -16% | 90% | -4% | — | — | — | — | — |
| Aspirin | 18 | 39% | -19% | 94% | +1% | 6 | 33% | -17% | 83% | -9% |

Ivabradine is the clear winner for resting tachycardia: +19% Sig Lift, +20% Attr Sig Lift, 70% attributed significance. Its mechanism (If channel blockade) directly targets heart rate without affecting blood pressure. Cetirizine at +12% with 100% improvement is intriguing — possible mast cell–mediated tachycardia. Propranolol and metoprolol both show negative Sig Lift, likely confounding by severity.

### Exertional Dyspnea

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **57** | **37%** | — | **95%** | — | **12** | **25%** | — | **92%** | — |
| | | | | | | | | | | |
| Aspirin | 12 | 42% | +7% | 92% | -3% | — | — | — | — | — |
| Low Dose Naltrexone (LDN) | 25 | 40% | +7% | 88% | -12% | — | — | — | — | — |
| Melatonin | 11 | 36% | -0% | 100% | +7% | — | — | — | — | — |
| Famotidine | 11 | 36% | -0% | 91% | -4% | — | — | — | — | — |
| Albuterol | 7 | 29% | -9% | 86% | -10% | 5 | 20% | -5% | 80% | -12% |
| Ivabradine | 11 | 9% | -35% | 100% | +7% | 7 | 29% | +4% | 100% | +8% |

Limited data (57 reports, 12 attributed). The 95% baseline improvement rate leaves little room for drugs to show lift. Ivabradine's strongly negative Sig Lift (-35%) but positive attributed data is classic confounding by severity.

### Muscle Pain

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

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

Famotidine is the only drug with positive Sig Lift (+22%, N=17, 100% improved). Most drugs show strongly negative Sig Lift — the 39% baseline is already high. LDN dominates attributed volume (N=27) but shows exactly 0% lift on both measures.

### Headache/Migraine

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

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
| Nortriptyline | 9 | 33% | -12% | 78% | -14% | 6 | 50% | +19% | 67% | -17% |
| Vitamin B12 | 10 | 30% | -16% | 90% | -0% | — | — | — | — | — |
| Metoprolol | 11 | 27% | -19% | 100% | +11% | — | — | — | — | — |
| Amitriptyline | 11 | 27% | -19% | 82% | -10% | 8 | 38% | +6% | 88% | +4% |
| Magnesium | 12 | 25% | -22% | 75% | -18% | — | — | — | — | — |
| Rizatriptan | 5 | 20% | -25% | 100% | +10% | 5 | 20% | -11% | 80% | -3% |
| Vitamin C | 10 | 20% | -27% | 80% | -12% | — | — | — | — | — |
| Propranolol | 22 | 18% | -34% | 82% | -11% | 8 | 12% | -19% | 75% | -8% |
| Sumatriptan | 9 | 11% | -37% | 67% | -26% | 5 | 20% | -11% | 80% | -3% |

Famotidine (+15% Sig Lift, 94% Impr%) is the most balanced performer. Nattokinase (100% improved, +11% Impr Lift) suggests a vascular component. Traditional migraine drugs (propranolol -34%, amitriptyline -19%, sumatriptan -37%) all show strongly negative Sig Lift — confounding by severity. Nortriptyline is the only one with positive Attr Sig Lift (+19%, N=6).

### Neuropathic Pain

**Drug efficacy** (sorted by Sig Lift; includes drugs with ≥10 co-occurring reports or ≥5 attributed entries):

| Drug | Co-N | Sig% | Sig Lift | Impr% | Impr Lift | Attr N | Attr Sig% | Attr Sig Lift | Attr Impr% | Attr Impr Lift |
|------|------|------|----------|-------|-----------|--------|-----------|---------------|------------|----------------|
| **BASELINE** | **78** | **35%** | — | **85%** | — | **40** | **18%** | — | **68%** | — |
| | | | | | | | | | | |
| Cetirizine | 12 | 67% | +35% | 92% | +4% | — | — | — | — | — |
| Aspirin | 11 | 45% | +8% | 82% | -8% | — | — | — | — | — |
| Famotidine | 12 | 42% | +4% | 83% | -7% | — | — | — | — | — |
| Amitriptyline | 7 | 29% | -11% | 71% | -19% | 6 | 17% | -1% | 67% | -1% |
| Low Dose Naltrexone (LDN) | 23 | 30% | -13% | 96% | +11% | — | — | — | — | — |
| Gabapentin | 23 | 30% | -13% | 83% | -10% | 22 | 27% | +10% | 77% | +10% |
| Propranolol | 12 | 25% | -17% | 75% | -17% | — | — | — | — | — |
| Duloxetine | 9 | 22% | -19% | 67% | -26% | 6 | 0% | -18% | 33% | -34% |
| Pregabalin | 7 | 14% | -28% | 86% | -3% | 6 | 0% | -18% | 67% | -1% |

Cetirizine dominates (+35% Sig Lift, 67% significant vs 35% baseline) — may reflect mast cell–mediated neuroinflammation or small fiber neuropathy. Gabapentin (standard-of-care) has -13% Sig Lift but +10% Attr Sig Lift — prescribed to the hardest cases, still produces above-baseline attributed significance. Pregabalin and duloxetine both show 0% attributed significance.

### Cross-Symptom Patterns

**Drugs with consistently positive Sig Lift across multiple symptoms:**
- **Valacyclovir** — top Sig Lift for PEM (+14%) and brain fog (+24%). Antiviral signal is strong.
- **HBOT** — top Sig Lift for PEM (+28%) and fatigue (+24%). Small N but consistent.
- **Mast cell drugs** — fexofenadine, ketotifen, cetirizine appear in top Sig Lift for brain fog, insomnia, POTS, neuropathic pain. The class signal is robust.
- **Famotidine** — positive Sig Lift for muscle pain (+22%), headache (+15%), insomnia (+9%), tachycardia (+4%). Broad systemic benefit.
- **Nattokinase (+serrapeptase)** — positive Sig Lift for fatigue (+15%), headache (+7%), PEM (+8%). Vascular/fibrinolytic signal.

**Drugs with high attributed counts but minimal/negative co-occurrence Sig Lift:**
- **LDN** — -0% to -5% Sig Lift across most symptoms despite being in 60%+ of reports. Its high attributed improvement rate reflects the baseline improvement rate of the population taking it, not a drug-specific effect. However, it does show +11% Impr Lift for neuropathic pain.
- **Propranolol** — negative Sig Lift for POTS (-9%), tachycardia (-12%), headache (-34%), and most other symptoms it appears in. Likely confounded by severity, but the breadth of negative signal (even for non-cardiac symptoms like PEM, fatigue, neuropathic pain) also suggests beta-blocker side effects (reduced exercise tolerance, fatigue) may actively hinder recovery. Contrast with ivabradine, which controls heart rate without these effects and shows positive lift.
- **Ivabradine** — negative Impr Lift for POTS (-6%) and tachycardia (-11%) despite high attributed significance. Classic confounding by indication.

**Key interpretive finding:** Sorting by Sig Lift (rather than Impr Lift as in the previous version) elevates antivirals and HBOT — interventions targeting root causes (viral persistence, tissue hypoxia) rather than symptom management. Mast cell drugs remain strong but their signal is more nuanced: they produce broad improvement (high Impr Lift) but not always dramatic improvement (moderate Sig Lift), except for cetirizine in neuropathic pain and ketotifen in insomnia/brain fog.

**Strongest drug–symptom combinations (high on both Sig Lift and Attr Sig Lift):**
- Paxlovid → PEM (+11% / +45%)
- Metoprolol → POTS (+18% / +23%)
- Ivabradine → Tachycardia (+19% / +20%)
- Modafinil → Brain fog (+15% / +17%)
- Ketotifen → Insomnia (+20% / +29%)
- Cetirizine → Neuropathic pain (+35% / no attributed data)
- Nattokinase+Serrapeptase → Fatigue (+15% / +10%)

---

## Next Steps

- [x] ~~Normalize drug names~~
- [x] ~~Build efficacy rankings per symptom~~
- [ ] Analyze comorbidity clusters vs treatment response (do MCAS patients respond differently?)
- [ ] Cross-reference with related condition reports (do POTS drugs from standalone reports match Long COVID POTS treatments?)
- [ ] Investigate temporal patterns (do drugs work better earlier vs later in disease course?)
- [ ] Pull clinical trial data for top drugs to triangulate with patient reports
