#!/usr/bin/env python3
"""Build JSON data files for the drug outcomes visualization.

Generates:
  - drug_outcomes.json (per-drug outcome counts for the bar chart)
  - drug_report_details.json (per-drug case list for the drill-down panel)
"""

import sqlite3
import json
import os


def build_outcomes(cur):
    """Generate drug_outcomes.json — per-drug outcome counts."""
    cur.execute('''
        SELECT v.drug_name,
            COUNT(*) as total,
            SUM(CASE WHEN v.outcome = 'Complete symptom resolution' THEN 1 ELSE 0 END) as resolved,
            SUM(CASE WHEN v.outcome = 'Significant symptom improvement' THEN 1 ELSE 0 END) as significant,
            SUM(CASE WHEN v.outcome = 'Moderate symptom improvement' THEN 1 ELSE 0 END) as moderate,
            SUM(CASE WHEN v.outcome = 'Mild symptom improvement' THEN 1 ELSE 0 END) as mild,
            SUM(CASE WHEN v.outcome = 'Symptom was unchanged' THEN 1 ELSE 0 END) as unchanged,
            SUM(CASE WHEN v.outcome LIKE '%worsening%' THEN 1 ELSE 0 END) as worsened
        FROM v_drug_outcomes v
        JOIN reports r ON v.report_id = r.id
        WHERE r.disease_id = 1988
        GROUP BY v.drug_name
        HAVING total >= 5
        ORDER BY total DESC
    ''')
    data = []
    for row in cur.fetchall():
        data.append({
            'drug': row[0], 'total': row[1],
            'resolved': row[2], 'significant': row[3],
            'moderate': row[4], 'mild': row[5],
            'unchanged': row[6], 'worsened': row[7]
        })
    with open('drug_outcomes_viz_data.json', 'w') as f:
        json.dump(data, f, separators=(',', ':'))
    print(f'drug_outcomes_viz_data.json: {len(data)} drugs ({os.path.getsize("drug_outcomes_viz_data.json")/1024:.0f} KB)')

def build_details(cur):
    """Generate drug_report_details.json — per-drug case list with metadata."""

    # For each drug, get the reports using it with useful metadata
    cur.execute('''
        SELECT COALESCE(m.canonical_name, TRIM(d.name)) as drug_name,
               r.id as report_id,
               r.outcome_computed,
               r.author_qualification,
               p.sex, p.age_group, p.country_treated,
               ef.symptoms_duration
        FROM report_drugs rd
        JOIN drugs d ON rd.drug_id = d.id
        LEFT JOIN drug_name_map m ON LOWER(TRIM(d.name)) = LOWER(TRIM(m.raw_name))
        JOIN reports r ON rd.report_id = r.id
        JOIN patients p ON r.id = p.report_id
        LEFT JOIN extra_fields ef ON r.id = ef.report_id
        WHERE r.disease_id = 1988
        ORDER BY drug_name, r.id
    ''')

    drug_reports = {}
    for row in cur.fetchall():
        drug = row[0]
        if drug not in drug_reports:
            drug_reports[drug] = []
        drug_reports[drug].append({
            'id': row[1],
            'outcome': row[2],
            'author': row[3],
            'sex': row[4],
            'age': row[5],
            'country': row[6],
            'duration': row[7]
        })

    # Get symptom outcomes attributed to each drug (normalize drug names)
    cur.execute('''
        SELECT COALESCE(m.canonical_name, TRIM(sod.drug_name)) as drug_name,
               so.report_id,
               so.symptom,
               so.outcome
        FROM symptom_outcome_drugs sod
        JOIN symptom_outcomes so ON sod.symptom_outcome_id = so.id
        LEFT JOIN drug_name_map m ON LOWER(TRIM(sod.drug_name)) = LOWER(TRIM(m.raw_name))
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988
    ''')

    # Build drug -> report_id -> list of {symptom, outcome}
    drug_symptom_outcomes = {}
    for row in cur.fetchall():
        drug, report_id, symptom, outcome = row
        if drug not in drug_symptom_outcomes:
            drug_symptom_outcomes[drug] = {}
        if report_id not in drug_symptom_outcomes[drug]:
            drug_symptom_outcomes[drug][report_id] = []
        # Shorten symptom names for JSON size
        short_symptom = symptom.split('(')[0].strip()[:50]
        if outcome:
            short_outcome = outcome.replace('symptom ', '').replace('Significant ', 'Sig ').replace('Complete ', '').replace('improvement', 'impr').replace('resolution', 'resolved').replace('Moderate ', 'Mod ').replace('Mild ', 'Mild ').replace('worsening', 'worse')
        else:
            short_outcome = '?'
        drug_symptom_outcomes[drug][report_id].append({
            's': short_symptom,
            'o': short_outcome
        })

    # Merge symptom outcomes into drug_reports
    for drug, reports in drug_reports.items():
        for report in reports:
            rid = report['id']
            symptoms = drug_symptom_outcomes.get(drug, {}).get(rid, [])
            if symptoms:
                report['sx'] = symptoms

    # Stats
    total_drugs = len(drug_reports)
    total_entries = sum(len(v) for v in drug_reports.values())
    print(f'{total_drugs} drugs, {total_entries} report entries')

    with open('drug_outcomes_viz_details.json', 'w') as f:
        json.dump(drug_reports, f, separators=(',', ':'))

    size = os.path.getsize('drug_outcomes_viz_details.json')
    print(f'drug_outcomes_viz_details.json: {total_drugs} drugs, {total_entries} cases ({size/1024:.0f} KB)')


def main():
    conn = sqlite3.connect('cureid.db')
    cur = conn.cursor()
    build_outcomes(cur)
    build_details(cur)
    conn.close()

if __name__ == '__main__':
    main()
