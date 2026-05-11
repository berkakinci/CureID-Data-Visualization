#!/usr/bin/env python3
"""
Per-symptom drug efficacy analysis for CureID Long COVID data.

Two complementary views:
1. Attributed: patient explicitly linked drug → symptom → outcome
2. Co-occurrence: patient was taking drug AND symptom improved (no attribution required)

Both compared against baseline improvement rate for each symptom.

Usage:
  python symptom_drug_efficacy.py                    # top 10 symptoms, top drugs for each
  python symptom_drug_efficacy.py "brain fog"        # specific symptom
  python symptom_drug_efficacy.py --all              # all symptoms with enough data
  python symptom_drug_efficacy.py --export           # export full results to CSV
"""

import sqlite3
import csv
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent / "cureid.db"

# Short labels for the verbose symptom names
SYMPTOM_SHORT = {
    "Post-Exert": "PEM",
    "Brain fog": "Brain Fog",
    "Cognitive": "Brain Fog",
    "General fatigue": "Fatigue",
    "Insomnia": "Insomnia",
    "Postural orthostatic tachycardia": "POTS",
    "Tachycardia/arrhythmia at rest": "Tachycardia (rest)",
    "Exertional dyspnea": "Exertional Dyspnea",
    "Myalgia": "Muscle Pain",
    "Orthostatic syncope": "Orthostatic Presyncope",
    "Migraine": "Headache/Migraine",
    "Muscle weakness": "Muscle Weakness",
    "Tinnitus": "Tinnitus",
    "Arthralgia": "Joint Pain",
    "Hot flashes": "Temperature Dysregulation",
    "Short-term memory": "Memory Loss",
    "Neuropathic pain": "Neuropathic Pain",
    "Nausea": "Nausea",
    "Tremors": "Tremors",
    "Anxiety": "Anxiety",
    "Dizziness": "Dizziness",
    "Shortness of breath": "Dyspnea",
}


def get_short_name(full_symptom):
    """Get short display name for a symptom."""
    for key, short in SYMPTOM_SHORT.items():
        if key.lower() in full_symptom.lower():
            return short
    # Fallback: first 40 chars
    return full_symptom[:40]


def analyze_symptom(cur, symptom_pattern, min_drug_reports=5):
    """
    Analyze drug efficacy for a given symptom.
    Returns (symptom_full_name, baseline_stats, drug_results).
    """
    # Find the actual symptom name
    cur.execute("""
        SELECT so.symptom, COUNT(*) as cnt FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988 AND so.symptom LIKE ?
        GROUP BY so.symptom
        ORDER BY cnt DESC
        LIMIT 1
    """, (f"%{symptom_pattern}%",))
    row = cur.fetchone()
    if not row:
        return None, None, []
    symptom_name = row[0]

    # Baseline: all reports with this symptom outcome
    cur.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN outcome LIKE '%improvement%' OR outcome LIKE '%resolution%' THEN 1 ELSE 0 END) as improved,
            SUM(CASE WHEN outcome = 'Significant symptom improvement' OR outcome = 'Complete symptom resolution' THEN 1 ELSE 0 END) as sig_improved,
            SUM(CASE WHEN outcome LIKE '%worsening%' THEN 1 ELSE 0 END) as worsened
        FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988 AND so.symptom = ?
    """, (symptom_name,))
    baseline = cur.fetchone()
    baseline_stats = {
        "total": baseline[0],
        "improved": baseline[1],
        "sig_improved": baseline[2],
        "worsened": baseline[3],
    }

    # Get all reports that have this symptom outcome
    cur.execute("""
        SELECT so.report_id,
            CASE WHEN outcome LIKE '%improvement%' OR outcome LIKE '%resolution%' THEN 1 ELSE 0 END as improved,
            CASE WHEN outcome = 'Significant symptom improvement' OR outcome = 'Complete symptom resolution' THEN 1 ELSE 0 END as sig_improved
        FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988 AND so.symptom = ?
    """, (symptom_name,))
    report_outcomes = {row[0]: (row[1], row[2]) for row in cur.fetchall()}
    all_report_ids = set(report_outcomes.keys())

    # Get drugs for each of these reports (normalized via drug_name_map)
    placeholders = ",".join("?" * len(all_report_ids))
    cur.execute(f"""
        SELECT rd.report_id, COALESCE(m.canonical_name, TRIM(d.name)) as drug_name
        FROM report_drugs rd
        JOIN drugs d ON rd.drug_id = d.id
        LEFT JOIN drug_name_map m ON LOWER(TRIM(d.name)) = LOWER(TRIM(m.raw_name))
        WHERE rd.report_id IN ({placeholders})
    """, list(all_report_ids))

    # Build drug → set of report_ids
    from collections import defaultdict
    drug_reports = defaultdict(set)
    for report_id, drug_name in cur.fetchall():
        drug_reports[drug_name].add(report_id)

    # Attributed outcomes (from v_drug_outcomes)
    cur.execute("""
        SELECT drug_name,
            COUNT(*) as total,
            SUM(CASE WHEN outcome LIKE '%improvement%' OR outcome LIKE '%resolution%' THEN 1 ELSE 0 END) as improved,
            SUM(CASE WHEN outcome = 'Significant symptom improvement' OR outcome = 'Complete symptom resolution' THEN 1 ELSE 0 END) as sig_improved,
            SUM(CASE WHEN outcome LIKE '%worsening%' THEN 1 ELSE 0 END) as worsened
        FROM v_drug_outcomes
        WHERE symptom = ?
        GROUP BY drug_name
        HAVING total >= ?
    """, (symptom_name, min_drug_reports))
    attributed = {row[0]: {"total": row[1], "improved": row[2], "sig_improved": row[3], "worsened": row[4]} for row in cur.fetchall()}

    # Build results per drug
    results = []
    for drug_name, report_ids in drug_reports.items():
        n_with_drug = len(report_ids)
        if n_with_drug < min_drug_reports:
            continue

        # Co-occurrence stats
        improved_with = sum(1 for rid in report_ids if report_outcomes[rid][0] == 1)
        sig_with = sum(1 for rid in report_ids if report_outcomes[rid][1] == 1)

        # Without drug
        without_ids = all_report_ids - report_ids
        n_without = len(without_ids)
        improved_without = sum(1 for rid in without_ids if report_outcomes[rid][0] == 1)

        # Rates
        rate_with = improved_with / n_with_drug if n_with_drug > 0 else 0
        rate_without = improved_without / n_without if n_without > 0 else 0
        lift = rate_with - rate_without  # positive = drug associated with better outcomes

        # Attributed stats (if available)
        attr = attributed.get(drug_name, None)

        results.append({
            "drug": drug_name,
            "cooccur_n": n_with_drug,
            "cooccur_improved": improved_with,
            "cooccur_sig": sig_with,
            "cooccur_rate": rate_with,
            "cooccur_lift": lift,
            "baseline_rate": rate_without,
            "attr_n": attr["total"] if attr else 0,
            "attr_improved": attr["improved"] if attr else 0,
            "attr_sig": attr["sig_improved"] if attr else 0,
            "attr_worsened": attr["worsened"] if attr else 0,
            "attr_rate": attr["improved"] / attr["total"] if attr and attr["total"] > 0 else None,
        })

    # Sort by co-occurrence lift (how much better than baseline)
    results.sort(key=lambda r: -r["cooccur_lift"])

    return symptom_name, baseline_stats, results


def print_symptom_results(symptom_name, baseline, results, top_n=20):
    """Print formatted results for one symptom."""
    short = get_short_name(symptom_name)
    bl_rate = baseline["improved"] / baseline["total"] * 100 if baseline["total"] > 0 else 0
    bl_sig = baseline["sig_improved"] / baseline["total"] * 100 if baseline["total"] > 0 else 0

    print(f"\n{'='*90}")
    print(f"  {short}")
    print(f"  Baseline: {baseline['total']} reports, {bl_rate:.0f}% improved, {bl_sig:.0f}% significant+resolved")
    print(f"{'='*90}")

    # Show top drugs by co-occurrence lift (min 10 reports for meaningful signal)
    filtered = [r for r in results if r["cooccur_n"] >= 10]
    filtered.sort(key=lambda r: -r["cooccur_lift"])

    print(f"\n  Top by co-occurrence lift (min 10 reports taking drug):")
    print(f"  {'Drug':<32} {'N':>4} {'Rate':>5} {'Lift':>6} | {'Attr N':>6} {'Attr%':>5} {'Sig%':>5}")
    print(f"  {'-'*32} {'-'*4} {'-'*5} {'-'*6} | {'-'*6} {'-'*5} {'-'*5}")

    for r in filtered[:top_n]:
        drug = r["drug"][:32]
        co_n = r["cooccur_n"]
        co_rate = f"{r['cooccur_rate']*100:.0f}%"
        lift = f"{r['cooccur_lift']*100:+.0f}%"
        attr_n = r["attr_n"] if r["attr_n"] else "-"
        attr_rate = f"{r['attr_rate']*100:.0f}%" if r["attr_rate"] is not None else "-"
        attr_sig = f"{r['attr_sig']/r['attr_n']*100:.0f}%" if r["attr_n"] else "-"

        print(f"  {drug:<32} {co_n:>4} {co_rate:>5} {lift:>6} | {attr_n:>6} {attr_rate:>5} {attr_sig:>5}")

    # Also show top by attributed significant improvement rate (min 5 attributed)
    attr_results = [r for r in results if r["attr_n"] >= 5]
    attr_results.sort(key=lambda r: -(r["attr_sig"] / r["attr_n"] if r["attr_n"] else 0))

    if attr_results:
        print(f"\n  Top by attributed significant+resolved rate (min 5 attributed):")
        print(f"  {'Drug':<32} {'Attr N':>6} {'Sig%':>5} {'Impr%':>5} {'Worse':>5} | {'Co-N':>5} {'Lift':>6}")
        print(f"  {'-'*32} {'-'*6} {'-'*5} {'-'*5} {'-'*5} | {'-'*5} {'-'*6}")

        for r in attr_results[:top_n]:
            drug = r["drug"][:32]
            attr_n = r["attr_n"]
            attr_sig = f"{r['attr_sig']/r['attr_n']*100:.0f}%"
            attr_rate = f"{r['attr_rate']*100:.0f}%" if r["attr_rate"] is not None else "-"
            attr_worse = r["attr_worsened"]
            co_n = r["cooccur_n"]
            lift = f"{r['cooccur_lift']*100:+.0f}%"

            print(f"  {drug:<32} {attr_n:>6} {attr_sig:>5} {attr_rate:>5} {attr_worse:>5} | {co_n:>5} {lift:>6}")


def export_results(db_path, output_path):
    """Export full results for all major symptoms to CSV."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Get top symptoms
    cur.execute("""
        SELECT symptom, COUNT(*) as cnt FROM symptom_outcomes so
        JOIN reports r ON so.report_id = r.id
        WHERE r.disease_id = 1988
        GROUP BY symptom ORDER BY cnt DESC
    """)
    symptoms = cur.fetchall()

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'symptom', 'symptom_short', 'drug', 'baseline_reports',
            'baseline_improve_rate', 'cooccur_n', 'cooccur_rate', 'cooccur_lift',
            'attr_n', 'attr_rate', 'attr_sig_rate', 'attr_worsened'
        ])

        for symptom_name, cnt in symptoms:
            if cnt < 20:
                continue
            short = get_short_name(symptom_name)
            _, baseline, results = analyze_symptom(cur, symptom_name, min_drug_reports=3)
            if not baseline:
                continue
            bl_rate = baseline["improved"] / baseline["total"] if baseline["total"] > 0 else 0

            for r in results:
                writer.writerow([
                    symptom_name, short, r["drug"], baseline["total"],
                    f"{bl_rate:.3f}", r["cooccur_n"], f"{r['cooccur_rate']:.3f}",
                    f"{r['cooccur_lift']:.3f}", r["attr_n"],
                    f"{r['attr_rate']:.3f}" if r["attr_rate"] is not None else "",
                    f"{r['attr_sig']/r['attr_n']:.3f}" if r["attr_n"] else "",
                    r["attr_worsened"] if r["attr_n"] else ""
                ])

    conn.close()
    print(f"Exported to {output_path}")


TOP_SYMPTOMS = [
    "Post-Exert",
    "Brain fog",
    "General fatigue",
    "Insomnia",
    "Postural orthostatic tachycardia",
    "Tachycardia/arrhythmia at rest",
    "Exertional dyspnea",
    "Myalgia",
    "Migraine",
    "Neuropathic pain",
]


if __name__ == "__main__":
    args = sys.argv[1:]
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if "--export" in args:
        export_results(DB_PATH, Path(__file__).parent / "symptom_drug_efficacy.csv")
    elif "--all" in args:
        cur.execute("""
            SELECT symptom, COUNT(*) as cnt FROM symptom_outcomes so
            JOIN reports r ON so.report_id = r.id WHERE r.disease_id = 1988
            GROUP BY symptom HAVING cnt >= 50 ORDER BY cnt DESC
        """)
        for symptom_name, cnt in cur.fetchall():
            _, baseline, results = analyze_symptom(cur, symptom_name)
            if baseline and results:
                print_symptom_results(symptom_name, baseline, results)
    elif args and not args[0].startswith("-"):
        # Specific symptom search
        pattern = args[0]
        symptom_name, baseline, results = analyze_symptom(cur, pattern)
        if symptom_name:
            print_symptom_results(symptom_name, baseline, results)
        else:
            print(f"No symptom matching '{pattern}' found.")
    else:
        # Default: top 10 symptoms
        for pattern in TOP_SYMPTOMS:
            symptom_name, baseline, results = analyze_symptom(cur, pattern)
            if symptom_name and results:
                print_symptom_results(symptom_name, baseline, results, top_n=15)

    conn.close()
