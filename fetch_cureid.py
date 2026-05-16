#!/usr/bin/env python3
"""Check for and download CureID data (Long COVID + related conditions).

Usage:
  python fetch_cureid.py          # check if new data is available
  python fetch_cureid.py --fetch  # download all reports + drugs (overwrites raw_api_data/)
"""

import json
import sqlite3
import time
import sys
from pathlib import Path
from urllib.request import urlopen

API = "https://cure-api.ncats.io/v2"
LIMIT = 50
DB_PATH = Path(__file__).parent / "cureid.db"
OUT_DIR = Path(__file__).parent / "raw_api_data"

# All datasets to fetch: (filename, endpoint_type, disease_id)
DATASETS = [
    # Core
    ("long_covid_reports.json", "reports", 1988),
    ("long_covid_drugs.json", "drugs", 1988),
    # ("covid19_acute_drugs.json", "drugs", 1589),  # not used in any pipeline
    # Post-infectious / Overlap
    ("dysautonomia_pots_reports.json", "reports", 2120),
    ("mcas_reports.json", "reports", 2146),
    ("mecfs_reports.json", "reports", 2121),
    ("fibromyalgia_reports.json", "reports", 2122),
    ("ehlers_danlos_reports.json", "reports", 2064),
    ("small_fiber_neuropathy_reports.json", "reports", 2086),
    # Viral Persistence / Reactivation
    ("epstein_barr_reports.json", "reports", 1664),
    ("cytomegalovirus_reports.json", "reports", 1632),
    ("herpes_simplex_reports.json", "reports", 1705),
    ("herpes_zoster_reports.json", "reports", 1706),
    ("herpes_labialis_reports.json", "reports", 1704),
    ("genital_herpes_reports.json", "reports", 1681),
    ("infectious_mononucleosis_reports.json", "reports", 1712),
    # Autoimmune / Neuroinflammatory
    ("encephalitis_reports.json", "reports", 1649),
    ("myelitis_reports.json", "reports", 1766),
    ("colitis_reports.json", "reports", 1619),
    ("crohns_disease_reports.json", "reports", 2099),
    ("myasthenia_gravis_reports.json", "reports", 2193),
    ("cipn_reports.json", "reports", 2174),
    # Infection-Triggered
    ("chronic_lyme_reports.json", "reports", 2125),
    ("lyme_acute_reports.json", "reports", 1736),
]


def api_get(url):
    with urlopen(url) as resp:
        return json.loads(resp.read())


def fetch_paginated(endpoint, disease_id):
    """Fetch all results from a paginated endpoint."""
    first = api_get(f"{API}/{endpoint}?disease={disease_id}&limit=1")
    total = first["count"]
    if total == 0:
        return []

    all_results = []
    offset = 0
    while offset < total:
        data = api_get(f"{API}/{endpoint}?disease={disease_id}&limit={LIMIT}&offset={offset}")
        all_results.extend(data["results"])
        offset += LIMIT
        time.sleep(0.4)
    return all_results


def local_count(filepath):
    """Get record count from a local JSON file."""
    if not filepath.exists():
        return 0
    data = json.loads(filepath.read_text())
    if isinstance(data, dict) and "results" in data:
        return len(data["results"])
    if isinstance(data, list):
        return len(data)
    return 0


def check():
    """Compare remote counts against local files for all datasets."""
    has_new = False
    for filename, endpoint, disease_id in DATASETS:
        remote = api_get(f"{API}/{endpoint}?disease={disease_id}&limit=1")
        remote_count = remote["count"]
        local = local_count(OUT_DIR / filename)

        if remote_count != local:
            diff = remote_count - local
            print(f"  ⚠️  {filename}: remote {remote_count}, local {local} ({diff:+d})")
            has_new = True
        else:
            print(f"  ✓  {filename}: {local}")

        time.sleep(0.3)

    print()
    if has_new:
        print("New data available. Run with --fetch to download.")
    else:
        print("✓ All datasets up to date.")


def fetch():
    """Download all datasets, saving in API response format ({count, results})."""
    OUT_DIR.mkdir(exist_ok=True)

    for filename, endpoint, disease_id in DATASETS:
        print(f"  {filename}...", end=" ", flush=True)
        results = fetch_paginated(endpoint, disease_id)
        output = {"count": len(results), "results": results}
        (OUT_DIR / filename).write_text(json.dumps(output, indent=1))
        print(f"{len(results)} records")
        print(f"{len(results)} records")

    print(f"\nDone. All files written to {OUT_DIR.name}/")
    print("\nNext steps:")
    print("  python build_db.py")
    print("  python drug_outcomes_viz_build.py")
    print("  python drug_heatmap_build.py")


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        check()
