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
    """Generate drug_outcomes.json — per-drug outcome counts + per-report scores."""
    # Outcome score mapping
    SCORE = {
        'Complete symptom resolution': 3,
        'Significant symptom improvement': 2,
        'Moderate symptom improvement': 1,
        'Mild symptom improvement': 0.5,
        'Symptom was unchanged': 0,
        'Mild symptom worsening': -0.5,
        'Moderate symptom worsening': -1,
        'Significant symptom worsening': -2,
    }

    # Get all attributed outcomes for Long COVID
    cur.execute('''
        SELECT v.drug_name, v.report_id, v.outcome
        FROM v_drug_outcomes v
        JOIN reports r ON v.report_id = r.id
        WHERE r.disease_id = 1988
    ''')

    from collections import defaultdict
    # drug -> report_id -> list of scores
    drug_report_scores = defaultdict(lambda: defaultdict(list))
    # drug -> outcome category counts
    drug_counts = defaultdict(lambda: {'total': 0, 'reports': set(),
        'resolved': 0, 'significant': 0, 'moderate': 0,
        'mild': 0, 'unchanged': 0, 'worsened': 0})

    for drug_name, report_id, outcome in cur.fetchall():
        d = drug_counts[drug_name]
        d['total'] += 1
        d['reports'].add(report_id)

        if outcome == 'Complete symptom resolution':
            d['resolved'] += 1
        elif outcome == 'Significant symptom improvement':
            d['significant'] += 1
        elif outcome == 'Moderate symptom improvement':
            d['moderate'] += 1
        elif outcome == 'Mild symptom improvement':
            d['mild'] += 1
        elif outcome == 'Symptom was unchanged':
            d['unchanged'] += 1
        elif outcome and 'worsening' in outcome:
            d['worsened'] += 1

        score = SCORE.get(outcome)
        if score is not None:
            drug_report_scores[drug_name][report_id].append(score)

    # Build output with per-report average scores
    data = []
    for drug_name, counts in drug_counts.items():
        if counts['total'] < 5:
            continue
        n_reports = len(counts['reports'])

        # Compute per-report average scores
        report_avgs = []
        for report_id, scores in drug_report_scores[drug_name].items():
            if scores:
                report_avgs.append(sum(scores) / len(scores))

        avg_score = sum(report_avgs) / len(report_avgs) if report_avgs else 0

        data.append({
            'drug': drug_name,
            'total': counts['total'],
            'reports': n_reports,
            'avg_score': round(avg_score, 2),
            'resolved': counts['resolved'],
            'significant': counts['significant'],
            'moderate': counts['moderate'],
            'mild': counts['mild'],
            'unchanged': counts['unchanged'],
            'worsened': counts['worsened'],
        })

    data.sort(key=lambda d: -d['total'])
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


def build_html():
    """Embed JSON data into the HTML template."""
    from pathlib import Path
    from datetime import datetime

    template = Path('drug_outcomes_viz_template.html').read_text()
    data_json = Path('drug_outcomes_viz_data.json').read_text()
    details_json = Path('drug_outcomes_viz_details.json').read_text()
    inline = f'let DATA = {data_json};\nlet DETAILS = {details_json};'
    html = template.replace('/*__DATA_PLACEHOLDER__*/', inline)

    # Inject metadata from DB
    import sqlite3
    conn = sqlite3.connect('cureid.db')
    row = conn.execute(
        "SELECT COUNT(*), MAX(updated) FROM reports WHERE disease_id=1988"
    ).fetchone()
    conn.close()
    count = row[0]
    latest = datetime.fromisoformat(row[1].replace('Z', '+00:00')).strftime("%b %-d, %Y")
    meta_str = f"Most recent report updated {latest} · {count} Long COVID reports"
    html = html.replace('/*__META_PLACEHOLDER__*/', meta_str)

    Path('drug_outcomes_viz.html').write_text(html)
    size_kb = Path('drug_outcomes_viz.html').stat().st_size / 1024
    print(f'drug_outcomes_viz.html: {size_kb:.0f} KB (embedded data)')


def main():
    conn = sqlite3.connect('cureid.db')
    cur = conn.cursor()
    build_outcomes(cur)
    build_details(cur)
    conn.close()
    build_html()

if __name__ == '__main__':
    main()
