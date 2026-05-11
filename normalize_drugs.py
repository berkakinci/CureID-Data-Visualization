#!/usr/bin/env python3
"""
Drug name normalization for CureID database.

The mapping lives in the DB table `drug_name_map` (raw_name → canonical_name).
This script helps manage that table and rebuild the view.

Usage:
  python normalize_drugs.py --export      # export current mapping to CSV for editing
  python normalize_drugs.py --import      # import CSV back into DB (merges, doesn't delete)
  python normalize_drugs.py --rebuild     # rebuild the v_drug_outcomes view
  python normalize_drugs.py --stats       # show top drugs after normalization
  python normalize_drugs.py --unmapped    # show high-frequency names not yet mapped
  python normalize_drugs.py --suggest     # fuzzy-match unmapped names to find duplicates
"""

import sqlite3
import csv
import re
import sys
from pathlib import Path
from collections import defaultdict

DB_PATH = Path(__file__).parent / "cureid.db"
MAPPING_FILE = Path(__file__).parent / "drug_name_mapping.csv"


def normalize_key(name):
    """Generate a fuzzy key for grouping likely duplicates."""
    s = name.strip().lower()
    # Remove dosage info: "5 mg oral tablet", "100 mg oral capsule", etc.
    s = re.sub(r'\d+(\.\d+)?\s*(mg|mcg|ml|g|%)\b.*?(tablet|capsule|solution|patch|cream|gel|liquid|spray|injection|oral|transdermal|topical)s?\b', '', s, flags=re.IGNORECASE)
    # Remove bracketed brand names: [Corlanor], [Allegra], etc.
    s = re.sub(r'\[.*?\]', '', s)
    # Remove parenthetical "etc" lists: (Vivitrol, ReViva, etc.)
    s = re.sub(r'\(([^)]*etc\.?)\)', '', s)
    # Remove trailing parenthetical if it's just brand names
    s = re.sub(r'\([\w\s,/\-]+\)\s*$', '', s)
    # Remove common suffixes
    s = re.sub(r'\b(hydrochloride|hcl|succinate|tartrate|fumarate|acetate|bromide|dihydrochloride|dimesylate|disoproxil|er|sr|xl|cr)\b', '', s)
    # Collapse whitespace and trim
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.rstrip(' ,.-')
    return s


def rebuild_view(db_path):
    """(Re)create the normalized outcome view."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("DROP VIEW IF EXISTS v_drug_outcomes")
    cur.execute("""
        CREATE VIEW v_drug_outcomes AS
        SELECT 
            COALESCE(m.canonical_name, TRIM(sod.drug_name)) as drug_name,
            so.symptom,
            so.outcome,
            so.report_id,
            so.duration_amount,
            so.duration_units,
            sod.symptom_outcome_id
        FROM symptom_outcome_drugs sod
        JOIN symptom_outcomes so ON sod.symptom_outcome_id = so.id
        LEFT JOIN drug_name_map m ON LOWER(TRIM(sod.drug_name)) = LOWER(TRIM(m.raw_name))
    """)

    conn.commit()
    conn.close()


def export_mapping(db_path, csv_path):
    """Export current DB mapping to CSV for editing."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT m.raw_name, m.canonical_name, COALESCE(c.cnt, 0) as count
        FROM drug_name_map m
        LEFT JOIN (
            SELECT drug_name, COUNT(*) as cnt 
            FROM symptom_outcome_drugs 
            GROUP BY drug_name
        ) c ON c.drug_name = m.raw_name
        ORDER BY count DESC
    """)
    rows = cur.fetchall()
    conn.close()

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['raw_name', 'canonical_name', 'count'])
        writer.writerows(rows)

    print(f"Exported {len(rows)} mappings to {csv_path}")


def import_mapping(db_path, csv_path):
    """Import CSV mappings into DB (upserts, does not delete existing)."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Ensure table exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS drug_name_map (
            raw_name TEXT PRIMARY KEY,
            canonical_name TEXT NOT NULL
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_drug_name_map_canonical ON drug_name_map(canonical_name)")

    imported = 0
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = row['raw_name']
            canonical = row['canonical_name']
            cur.execute("INSERT OR REPLACE INTO drug_name_map VALUES (?, ?)", (raw, canonical))
            imported += 1

    conn.commit()
    conn.close()

    print(f"Imported {imported} mappings from {csv_path}")
    rebuild_view(db_path)
    print("View v_drug_outcomes rebuilt.")


def show_stats(db_path):
    """Show top drugs after normalization."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(DISTINCT drug_name) FROM symptom_outcome_drugs")
    raw_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(DISTINCT drug_name) FROM v_drug_outcomes")
    norm_count = cur.fetchone()[0]

    print(f"Raw distinct names:       {raw_count}")
    print(f"Normalized distinct names: {norm_count}")
    print(f"Reduction:                 {raw_count - norm_count}")

    cur.execute("""
        SELECT drug_name, COUNT(*) as cnt,
            SUM(CASE WHEN outcome LIKE '%improvement%' OR outcome LIKE '%resolution%' THEN 1 ELSE 0 END) as positive,
            SUM(CASE WHEN outcome LIKE '%worsening%' THEN 1 ELSE 0 END) as worsened
        FROM v_drug_outcomes
        GROUP BY drug_name
        ORDER BY cnt DESC
        LIMIT 30
    """)

    print(f"\n{'Drug':<40} {'Total':>6} {'Pos':>6} {'Worse':>6} {'%Pos':>5}")
    print("-" * 68)
    for name, total, pos, worse in cur.fetchall():
        pct = round(100 * pos / total) if total > 0 else 0
        print(f"{name:<40} {total:>6} {pos:>6} {worse:>6} {pct:>4}%")

    conn.close()


def show_unmapped(db_path, min_count=5):
    """Show drug names not in the mapping table, sorted by frequency."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT sod.drug_name, COUNT(*) as cnt
        FROM symptom_outcome_drugs sod
        LEFT JOIN drug_name_map m ON LOWER(TRIM(sod.drug_name)) = LOWER(TRIM(m.raw_name))
        WHERE m.raw_name IS NULL
        GROUP BY sod.drug_name
        HAVING cnt >= ?
        ORDER BY cnt DESC
    """, (min_count,))

    rows = cur.fetchall()
    conn.close()

    print(f"Unmapped names with >= {min_count} occurrences: {len(rows)}")
    print(f"\n{'Name':<60} {'Count':>5}")
    print("-" * 67)
    for name, cnt in rows:
        print(f"{name:<60} {cnt:>5}")


def suggest_mappings(db_path, min_count=3):
    """Use fuzzy matching to suggest groups of names that might be the same drug."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Get unmapped names
    cur.execute("""
        SELECT sod.drug_name, COUNT(*) as cnt
        FROM symptom_outcome_drugs sod
        LEFT JOIN drug_name_map m ON LOWER(TRIM(sod.drug_name)) = LOWER(TRIM(m.raw_name))
        WHERE m.raw_name IS NULL
        GROUP BY sod.drug_name
        HAVING cnt >= ?
        ORDER BY cnt DESC
    """, (min_count,))
    unmapped = cur.fetchall()
    conn.close()

    # Group by normalized key
    groups = defaultdict(list)
    for name, cnt in unmapped:
        key = normalize_key(name)
        groups[key].append((name, cnt))

    # Only show groups with multiple entries (actual duplicates)
    dupes = {k: v for k, v in groups.items() if len(v) > 1}

    if not dupes:
        print("No obvious duplicate groups found in unmapped names.")
        return

    print(f"Potential duplicate groups ({len(dupes)} groups):\n")
    for key in sorted(dupes, key=lambda k: -sum(c for _, c in dupes[k])):
        entries = dupes[key]
        total = sum(c for _, c in entries)
        print(f"  Key: '{key}' (total: {total})")
        for name, cnt in sorted(entries, key=lambda x: -x[1]):
            print(f"    {cnt:>4}x  {name}")
        print()


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--export" in args:
        export_mapping(DB_PATH, MAPPING_FILE)
    elif "--import" in args:
        import_mapping(DB_PATH, MAPPING_FILE)
    elif "--rebuild" in args:
        rebuild_view(DB_PATH)
        print("View v_drug_outcomes rebuilt.")
    elif "--clean" in args:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("DELETE FROM drug_name_map WHERE raw_name = canonical_name")
        removed = cur.rowcount
        conn.commit()
        conn.close()
        print(f"Removed {removed} identity mappings (raw = canonical).")
    elif "--stats" in args:
        show_stats(DB_PATH)
    elif "--suggest" in args:
        min_c = 3
        for i, a in enumerate(args):
            if a == "--min" and i + 1 < len(args):
                min_c = int(args[i + 1])
        suggest_mappings(DB_PATH, min_c)
    elif "--unmapped" in args:
        min_c = 5
        for i, a in enumerate(args):
            if a == "--min" and i + 1 < len(args):
                min_c = int(args[i + 1])
        show_unmapped(DB_PATH, min_c)
    else:
        print(__doc__)
