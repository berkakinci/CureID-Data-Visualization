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

# Minimum thresholds
MIN_SYMPTOM_REPORTS = 50
MIN_COOCCUR = 5
MIN_SYMPTOMS_PER_DRUG = 3


def build_data():
    """Query DB and return the heatmap data dict."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Get all symptoms with enough reports
    cur.execute("""
        SELECT symptom, COUNT(*) as cnt FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988
        GROUP BY symptom HAVING cnt >= ?
        ORDER BY cnt DESC
    """, (MIN_SYMPTOM_REPORTS,))
    symptom_rows = cur.fetchall()

    symptoms_meta = []
    all_cells = []
    drug_symptom_count = {}

    for symptom_name, cnt in symptom_rows:
        short = get_short_name(symptom_name)
        symptom_name_full, baseline, results = analyze_symptom(cur, symptom_name, min_drug_reports=MIN_COOCCUR)
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

        for r in results:
            drug = r["drug"]
            if drug not in drug_symptom_count:
                drug_symptom_count[drug] = 0
            drug_symptom_count[drug] += 1

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
            })

    # Filter to drugs appearing across enough symptoms
    keep_drugs = {d for d, c in drug_symptom_count.items() if c >= MIN_SYMPTOMS_PER_DRUG}
    filtered_cells = [c for c in all_cells if c["drug"] in keep_drugs]

    # Sort drugs by average sig lift across symptoms (descending)
    drug_lifts = defaultdict(list)
    for c in filtered_cells:
        drug_lifts[c["drug"]].append(c["cooccur_sig_lift"])
    drugs_sorted = sorted(drug_lifts.keys(), key=lambda d: -(sum(drug_lifts[d]) / len(drug_lifts[d])))

    output = {
        "symptoms": symptoms_meta,
        "drugs": drugs_sorted,
        "cells": filtered_cells,
        "meta": {
            "min_cooccur": MIN_COOCCUR,
            "min_symptom_reports": MIN_SYMPTOM_REPORTS,
            "min_symptoms_per_drug": MIN_SYMPTOMS_PER_DRUG,
            "total_cells": len(filtered_cells),
            "total_drugs": len(drugs_sorted),
            "total_symptoms": len(symptoms_meta),
        }
    }

    conn.close()
    return output


def get_meta_string():
    """Build the data metadata string from report timestamps and count."""
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT COUNT(*), MAX(updated) FROM reports WHERE disease_id=1988"
    ).fetchone()
    conn.close()
    count = row[0]
    latest = datetime.fromisoformat(row[1].replace('Z', '+00:00')).strftime("%b %-d, %Y")
    return f"Most recent report updated {latest} · {count} Long COVID reports"


def main():
    data = build_data()

    # Read template and inject data + meta
    template = TEMPLATE_PATH.read_text()
    data_json = json.dumps(data, separators=(',', ':'))
    html = template.replace('/*__DATA_PLACEHOLDER__*/', f'const DATA = {data_json};')
    html = html.replace('/*__META_PLACEHOLDER__*/', get_meta_string())

    HTML_PATH.write_text(html)
    size_kb = HTML_PATH.stat().st_size / 1024
    meta = data["meta"]
    print(f"{HTML_PATH.name}: {meta['total_symptoms']} symptoms × {meta['total_drugs']} drugs, {meta['total_cells']} cells ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
