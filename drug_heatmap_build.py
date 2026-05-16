#!/usr/bin/env python3
"""Build the symptom × drug efficacy heatmap visualization.

Generates heatmap_viz.html with embedded JSON data (no server needed).

Data includes:
  - symptoms: list of {name, short, baseline_n, baseline_sig_rate}
  - drugs: list of unique drug names (columns)
  - cells: list of {symptom, drug, cooccur_n, cooccur_sig_rate, cooccur_sig_lift,
                    attr_n, attr_sig_rate, attr_sig_lift}

Only includes drugs that appear for ≥3 symptoms with ≥5 co-occurring reports,
and symptoms with ≥50 total reports.
"""

import sqlite3
import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from symptom_drug_efficacy import analyze_symptom, get_short_name

DB_PATH = Path(__file__).parent / "cureid.db"
HTML_PATH = Path(__file__).parent / "drug_heatmap_viz.html"
TEMPLATE_PATH = Path(__file__).parent / "drug_heatmap_viz_template.html"
CONFIG_PATH = Path(__file__).parent / "config.json"

# Minimum thresholds
MIN_SYMPTOM_REPORTS = 50
MIN_COOCCUR = 5
MIN_SYMPTOMS_PER_DRUG = 3


def load_config():
    """Load disease config from config.json."""
    with open(CONFIG_PATH) as f:
        return json.load(f)


def build_data():
    """Query DB and return the heatmap data dict."""
    config = load_config()
    disease_id = config["disease_id"]
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Get all symptoms with enough reports
    cur.execute("""
        SELECT symptom, COUNT(*) as cnt FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = ?
        GROUP BY symptom HAVING cnt >= ?
        ORDER BY cnt DESC
    """, (disease_id, MIN_SYMPTOM_REPORTS,))
    symptom_rows = cur.fetchall()

    symptoms_meta = []
    all_cells = []
    drug_symptom_count = {}

    # Preload normalized drug names for outcome distribution lookup
    from normalize_drugs import load_name_map, normalize_name
    name_map = load_name_map()

    # --- Build report-level data for drill-down ---
    # Outcome abbreviations
    OUTCOME_MAP = {
        'Complete symptom resolution': 'resolved',
        'Significant symptom improvement': 'significant',
        'Moderate symptom improvement': 'moderate',
        'Mild symptom improvement': 'mild',
        'Symptom was unchanged': 'unchanged',
        'Mild symptom worsening': 'worsened',
        'Moderate symptom worsening': 'worsened',
        'Significant symptom worsening': 'worsened',
    }

    # All reports with patient info
    reports_data = {}
    for r in cur.execute("""
        SELECT r.id, p.sex, p.age_group, p.country_treated
        FROM reports r JOIN patients p ON p.report_id = r.id
        WHERE r.disease_id = ?
    """, (disease_id,)).fetchall():
        reports_data[r[0]] = {
            'sex': (r[1] or '?')[0],
            'age': r[2] or '',
            'country': r[3] or '',
            'drugs': [],
            'sx': [],
        }

    # Add drugs per report
    for r in cur.execute("""
        SELECT rd.report_id, d.name, rd.dose_amount, rd.unit_of_measurement, rd.frequency
        FROM report_drugs rd JOIN drugs d ON rd.drug_id = d.id
        JOIN reports rep ON rd.report_id = rep.id WHERE rep.disease_id = ?
    """, (disease_id,)).fetchall():
        rid = r[0]
        if rid not in reports_data:
            continue
        drug_name = normalize_name(r[1], name_map)
        dose = ''
        if r[2]:
            unit = (r[3] or '').replace('milligram (mg)', 'mg').replace('microgram (mcg)', 'mcg')
            dose = f"{r[2]}{unit}" if unit else r[2]
        entry = {'n': drug_name}
        if dose:
            entry['d'] = dose
        reports_data[rid]['drugs'].append(entry)

    # Add symptom outcomes per report
    for r in cur.execute("""
        SELECT so.report_id, so.symptom, so.outcome
        FROM symptom_outcomes so JOIN reports rep ON so.report_id = rep.id
        WHERE rep.disease_id = ?
    """, (disease_id,)).fetchall():
        rid = r[0]
        if rid not in reports_data:
            continue
        outcome_short = OUTCOME_MAP.get(r[2], '')
        if not outcome_short:
            continue
        short_sx = get_short_name(r[1])
        reports_data[rid]['sx'].append({'s': short_sx, 'o': outcome_short})

    # Build symptom -> report_ids and drug -> report_ids for cell mapping
    sym_report_ids = defaultdict(set)
    for r in cur.execute("""
        SELECT so.report_id, so.symptom FROM symptom_outcomes so
        JOIN reports rep ON so.report_id = rep.id WHERE rep.disease_id = ?
    """, (disease_id,)).fetchall():
        sym_report_ids[get_short_name(r[1])].add(r[0])

    drug_report_ids = defaultdict(set)
    for r in cur.execute("""
        SELECT rd.report_id, d.name FROM report_drugs rd
        JOIN drugs d ON rd.drug_id = d.id
        JOIN reports rep ON rd.report_id = rep.id WHERE rep.disease_id = ?
    """, (disease_id,)).fetchall():
        drug_report_ids[normalize_name(r[1], name_map)].add(r[0])

    # --- End report-level data ---

    for symptom_name, cnt in symptom_rows:
        short = get_short_name(symptom_name)
        symptom_name_full, baseline, results = analyze_symptom(cur, symptom_name, min_drug_reports=MIN_COOCCUR, disease_id=disease_id)
        if not baseline or not results:
            continue

        bl_sig = baseline["sig_improved"] / baseline["total"] if baseline["total"] > 0 else 0
        bl_impr = baseline["improved"] / baseline["total"] if baseline["total"] > 0 else 0

        symptoms_meta.append({
            "name": symptom_name_full,
            "short": short,
            "n": baseline["total"],
            "sig_rate": round(bl_sig, 3),
            "impr_rate": round(bl_impr, 3),
        })

        # Build outcome distribution for each drug × this symptom
        # Get all report_ids with this symptom and their outcomes
        cur.execute("""
            SELECT so.report_id, so.outcome
            FROM symptom_outcomes so
            JOIN reports r ON so.report_id = r.id
            WHERE r.disease_id = ? AND so.symptom = ?
        """, (disease_id, symptom_name_full,))
        report_outcome_map = {}
        for rid, outcome in cur.fetchall():
            report_outcome_map[rid] = outcome

        # Get drugs per report (normalized)
        all_rids = list(report_outcome_map.keys())
        if all_rids:
            placeholders = ",".join("?" * len(all_rids))
            cur.execute(f"""
                SELECT rd.report_id, d.name
                FROM report_drugs rd
                JOIN drugs d ON rd.drug_id = d.id
                WHERE rd.report_id IN ({placeholders})
            """, all_rids)
            drug_to_rids = defaultdict(set)
            for rid, raw_name in cur.fetchall():
                norm = normalize_name(raw_name, name_map)
                drug_to_rids[norm].add(rid)

        for r in results:
            drug = r["drug"]
            if drug not in drug_symptom_count:
                drug_symptom_count[drug] = 0
            drug_symptom_count[drug] += 1

            # Compute outcome distribution for this drug × symptom
            dist = {"resolved": 0, "significant": 0, "moderate": 0,
                    "mild": 0, "unchanged": 0, "worsened": 0}
            if all_rids:
                for rid in drug_to_rids.get(drug, []):
                    outcome = report_outcome_map.get(rid, "")
                    if outcome == "Complete symptom resolution":
                        dist["resolved"] += 1
                    elif outcome == "Significant symptom improvement":
                        dist["significant"] += 1
                    elif outcome == "Moderate symptom improvement":
                        dist["moderate"] += 1
                    elif outcome == "Mild symptom improvement":
                        dist["mild"] += 1
                    elif outcome == "Symptom was unchanged":
                        dist["unchanged"] += 1
                    elif outcome and "worsening" in outcome:
                        dist["worsened"] += 1

            all_cells.append({
                "symptom": short,
                "drug": drug,
                "cooccur_n": r["cooccur_n"],
                "cooccur_sig_rate": round(r["cooccur_sig_rate"], 3),
                "cooccur_sig_lift": round(r["cooccur_sig_lift"], 3),
                "cooccur_impr_rate": round(r["cooccur_rate"], 3),
                "cooccur_impr_lift": round(r["cooccur_lift"], 3),
                "attr_n": r["attr_n"],
                "attr_sig_rate": round(r["attr_sig_rate"], 3) if r.get("attr_sig_rate") is not None else None,
                "attr_sig_lift": round(r.get("attr_sig_lift") or 0, 3) if r.get("attr_sig_lift") is not None else None,
                "dist": dist,
            })

    # Filter to drugs appearing across enough symptoms
    keep_drugs = {d for d, c in drug_symptom_count.items() if c >= MIN_SYMPTOMS_PER_DRUG}
    filtered_cells = [c for c in all_cells if c["drug"] in keep_drugs]

    # Sort drugs by average sig lift across symptoms (descending)
    drug_lifts = defaultdict(list)
    for c in filtered_cells:
        drug_lifts[c["drug"]].append(c["cooccur_sig_lift"])
    drugs_sorted = sorted(drug_lifts.keys(), key=lambda d: -(sum(drug_lifts[d]) / len(drug_lifts[d])))

    # Build cell -> report_id mapping (using numeric indices for compactness)
    # Only for cells that made it through filtering
    cell_drug_sym_pairs = {(c["symptom"], c["drug"]) for c in filtered_cells}
    all_report_ids_in_cells = set()
    cell_rids_raw = {}
    for sym, drug in cell_drug_sym_pairs:
        rids = sym_report_ids.get(sym, set()) & drug_report_ids.get(drug, set())
        key = f"{sym}|{drug}"
        cell_rids_raw[key] = sorted(rids)
        all_report_ids_in_cells.update(rids)

    # Create compact index: report_id -> integer index
    rid_list = sorted(all_report_ids_in_cells)
    rid_to_idx = {rid: i for i, rid in enumerate(rid_list)}
    cell_rids_compact = {k: [rid_to_idx[r] for r in v] for k, v in cell_rids_raw.items()}

    # Filter reports_data to only those referenced
    reports_compact = []
    for rid in rid_list:
        rd = reports_data.get(rid, {})
        reports_compact.append({
            'id': rid,
            'sex': rd.get('sex', '?'),
            'age': rd.get('age', ''),
            'country': rd.get('country', ''),
            'drugs': rd.get('drugs', []),
            'sx': rd.get('sx', []),
        })

    output = {
        "symptoms": symptoms_meta,
        "drugs": drugs_sorted,
        "cells": filtered_cells,
        "reports": reports_compact,
        "cellReports": cell_rids_compact,
        "meta": {
            "min_cooccur": MIN_COOCCUR,
            "min_symptom_reports": MIN_SYMPTOM_REPORTS,
            "min_symptoms_per_drug": MIN_SYMPTOMS_PER_DRUG,
            "total_cells": len(filtered_cells),
            "total_drugs": len(drugs_sorted),
            "total_symptoms": len(symptoms_meta),
            "total_reports": len(reports_compact),
        }
    }

    conn.close()
    return output


def get_meta_string():
    """Build the data metadata string from report timestamps and count."""
    config = load_config()
    disease_id = config["disease_id"]
    disease_name = config["disease_name"]
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT COUNT(*), MAX(updated) FROM reports WHERE disease_id=?", (disease_id,)
    ).fetchone()
    conn.close()
    count = row[0]
    latest = datetime.fromisoformat(row[1].replace('Z', '+00:00')).strftime("%b %-d, %Y")
    return f"Most recent report updated {latest} · {count} {disease_name} reports"


def main():
    config = load_config()
    disease_name = config["disease_name"]
    data = build_data()

    # Read template and inject data + meta + disease name
    template = TEMPLATE_PATH.read_text()
    data_json = json.dumps(data, separators=(',', ':'))
    html = template.replace('/*__DATA_PLACEHOLDER__*/', f'const DATA = {data_json};')
    html = html.replace('/*__META_PLACEHOLDER__*/', get_meta_string())
    html = html.replace('/*__DISEASE_NAME__*/', disease_name)

    HTML_PATH.write_text(html)
    size_kb = HTML_PATH.stat().st_size / 1024
    meta = data["meta"]
    print(f"{HTML_PATH.name}: {meta['total_symptoms']} symptoms × {meta['total_drugs']} drugs, {meta['total_cells']} cells ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
