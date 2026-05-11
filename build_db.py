#!/usr/bin/env python3
"""
Build a local SQLite database from CureID raw API JSON files.

Usage:
    python build_db.py

Reads from raw_api_data/ and produces cureid.db in the same directory.
"""

import json
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "raw_api_data"
DB_PATH = Path(__file__).parent / "cureid.db"

# All report files to ingest
REPORT_FILES = [
    ("long_covid_reports.json", "Long COVID", 1988),
    ("dysautonomia_pots_reports.json", "Dysautonomia/POTS", 2120),
    ("mcas_reports.json", "MCAS", 2146),
    ("mecfs_reports.json", "ME/CFS", 2121),
    ("fibromyalgia_reports.json", "Fibromyalgia", 2122),
    ("ehlers_danlos_reports.json", "Ehlers-Danlos Syndrome", 2064),
    ("small_fiber_neuropathy_reports.json", "Small Fiber Neuropathy", 2086),
    ("chronic_lyme_reports.json", "Chronic Lyme", 2125),
    ("lyme_acute_reports.json", "Lyme (Acute)", 1736),
    ("epstein_barr_reports.json", "Epstein-Barr Virus", 1664),
    ("cytomegalovirus_reports.json", "Cytomegalovirus", 1632),
    ("herpes_simplex_reports.json", "Herpes Simplex", 1705),
    ("herpes_zoster_reports.json", "Herpes Zoster", 1706),
    ("herpes_labialis_reports.json", "Herpes Labialis", 1704),
    ("genital_herpes_reports.json", "Genital Herpes", 1681),
    ("infectious_mononucleosis_reports.json", "Infectious Mononucleosis", 1712),
    ("encephalitis_reports.json", "Encephalitis", 1649),
    ("myelitis_reports.json", "Myelitis", 1766),
    ("colitis_reports.json", "Colitis", 1619),
    ("crohns_disease_reports.json", "Crohn's Disease", 2099),
    ("myasthenia_gravis_reports.json", "Myasthenia Gravis", 2193),
    ("cipn_reports.json", "CIPN", 2174),
]


def create_schema(conn: sqlite3.Connection):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS reports (
        id TEXT PRIMARY KEY,
        disease_id INTEGER NOT NULL,
        report_type TEXT,          -- 'patient' or 'clinician'
        form_type TEXT,            -- 'pasc', 'default', 'ehr'
        author_qualification TEXT,
        author_first_name TEXT,
        author_last_name TEXT,
        status TEXT,
        created TEXT,
        updated TEXT,
        outcome_computed TEXT,
        unusual TEXT,
        additional_info TEXT,
        FOREIGN KEY (disease_id) REFERENCES diseases(id)
    );

    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        report_id TEXT NOT NULL,
        sex TEXT,
        age_group TEXT,
        ethnicity TEXT,
        country_treated TEXT,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS patient_races (
        patient_id INTEGER NOT NULL,
        race TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    );

    CREATE TABLE IF NOT EXISTS comorbidities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        value TEXT NOT NULL,
        timing TEXT DEFAULT 'pre',  -- 'pre' = before disease, 'post' = developed after
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    );

    CREATE TABLE IF NOT EXISTS drugs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        rxnorm_id TEXT,
        category TEXT,
        fda_approved INTEGER
    );

    CREATE TABLE IF NOT EXISTS report_drugs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        drug_id INTEGER NOT NULL,
        dose_amount TEXT,
        unit_of_measurement TEXT,
        frequency TEXT,
        route TEXT,
        duration_amount TEXT,
        duration_units TEXT,
        treatment_begin TEXT,
        treatment_end TEXT,
        treatment_on_going INTEGER,
        is_initial_regimen INTEGER,
        long_drug_str TEXT,
        FOREIGN KEY (report_id) REFERENCES reports(id),
        FOREIGN KEY (drug_id) REFERENCES drugs(id)
    );

    CREATE TABLE IF NOT EXISTS symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        symptom TEXT NOT NULL,
        symptom_short TEXT,
        severity TEXT,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS symptom_outcomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        symptom TEXT NOT NULL,
        outcome TEXT,
        duration_amount TEXT,
        duration_units TEXT,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS symptom_outcome_drugs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symptom_outcome_id INTEGER NOT NULL,
        drug_name TEXT NOT NULL,
        FOREIGN KEY (symptom_outcome_id) REFERENCES symptom_outcomes(id)
    );

    CREATE TABLE IF NOT EXISTS extra_fields (
        report_id TEXT PRIMARY KEY,
        care_acute_covid TEXT,
        doses_of_vaccine TEXT,
        vaccine_status TEXT,
        symptoms_duration TEXT,
        previously_approved INTEGER,
        research_prioritizing TEXT,
        drug_additional_details TEXT,
        when_symptom_acute_covid_year TEXT,
        when_symptom_acute_covid_month TEXT,
        -- EHR fields
        bmi TEXT,
        gfr TEXT,
        wbc TEXT,
        pulse_ox TEXT,
        creatinine TEXT,
        hospitalization_length TEXT,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS vaccines_received (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        vaccine TEXT NOT NULL,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS comorbidities_after (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        value TEXT NOT NULL,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );

    CREATE TABLE IF NOT EXISTS regular_medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT NOT NULL,
        drug_id INTEGER,
        drug_name TEXT NOT NULL,
        FOREIGN KEY (report_id) REFERENCES reports(id)
    );
    """)


def ingest_report(conn: sqlite3.Connection, case: dict, disease_id: int):
    """Ingest a single case report into the database."""
    report_id = case["id"]
    rpt = case["report"]
    author = case.get("author", {})
    patient = rpt.get("patient", {})
    extra = rpt.get("extra_fields") or {}

    # Insert report
    conn.execute("""
        INSERT OR IGNORE INTO reports
        (id, disease_id, report_type, form_type, author_qualification,
         author_first_name, author_last_name, status, created, updated,
         outcome_computed, unusual, additional_info)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        report_id, disease_id, case.get("report_type"), case.get("form_type"),
        author.get("qualification"), author.get("first_name"), author.get("last_name"),
        case.get("status"), case.get("created"), case.get("updated"),
        rpt.get("outcome_computed"), rpt.get("unusual"), rpt.get("additional_info"),
    ))

    # Insert patient
    patient_id = patient.get("id")
    if patient_id:
        conn.execute("""
            INSERT OR IGNORE INTO patients
            (id, report_id, sex, age_group, ethnicity, country_treated)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            patient_id, report_id, patient.get("sex"), patient.get("age_group"),
            patient.get("ethnicity"), patient.get("country_treated"),
        ))

        # Races
        for race in patient.get("race", []) or []:
            if race:
                conn.execute(
                    "INSERT OR IGNORE INTO patient_races (patient_id, race) VALUES (?, ?)",
                    (patient_id, race)
                )

        # Comorbidities (pre-existing)
        for c in patient.get("comorbidity", []) or []:
            val = c.get("value") or c.get("label")
            if val:
                conn.execute(
                    "INSERT INTO comorbidities (patient_id, value, timing) VALUES (?, ?, 'pre')",
                    (patient_id, val)
                )

    # Drugs from regimens
    for reg in rpt.get("regimens", []):
        drug = reg.get("drug", {})
        drug_id = drug.get("id")
        if drug_id:
            conn.execute("""
                INSERT OR IGNORE INTO drugs (id, name, rxnorm_id, category, fda_approved)
                VALUES (?, ?, ?, ?, ?)
            """, (
                drug_id, drug.get("name", ""), drug.get("rxnorm_id"),
                drug.get("category"), 1 if drug.get("fda_approved") else 0,
            ))

            conn.execute("""
                INSERT INTO report_drugs
                (report_id, drug_id, dose_amount, unit_of_measurement, frequency,
                 route, duration_amount, duration_units, treatment_begin, treatment_end,
                 treatment_on_going, is_initial_regimen, long_drug_str)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                report_id, drug_id, reg.get("dose_amount"),
                reg.get("unit_of_measurement"), reg.get("frequency"),
                reg.get("route"), reg.get("duration_amount"),
                reg.get("unit_of_measurement_duration"),
                reg.get("treatment_begin"), reg.get("treatment_end"),
                1 if reg.get("treatment_on_going") else 0,
                1 if reg.get("is_initial_regimen") else 0,
                reg.get("long_drug_str_lc"),
            ))

    # Symptoms (severity)
    for s in extra.get("symptoms_severity", []):
        conn.execute("""
            INSERT INTO symptoms (report_id, symptom, symptom_short, severity)
            VALUES (?, ?, ?, ?)
        """, (
            report_id, s.get("symptom", ""), s.get("symptom_short"), s.get("severity"),
        ))

    # Symptom outcomes (drug → symptom → outcome)
    for o in extra.get("symptoms_outcome", []):
        symptom = o.get("long_covid_symptom") or o.get("symptom") or ""
        if not symptom:
            continue
        cursor = conn.execute("""
            INSERT INTO symptom_outcomes
            (report_id, symptom, outcome, duration_amount, duration_units)
            VALUES (?, ?, ?, ?, ?)
        """, (
            report_id, symptom, o.get("long_covid_outcome"),
            o.get("duration_amount"), o.get("duration_units"),
        ))
        outcome_id = cursor.lastrowid
        for drug_name in o.get("long_covid_drugs", []) or []:
            conn.execute("""
                INSERT INTO symptom_outcome_drugs (symptom_outcome_id, drug_name)
                VALUES (?, ?)
            """, (outcome_id, drug_name))

    # Extra fields
    conn.execute("""
        INSERT OR IGNORE INTO extra_fields
        (report_id, care_acute_covid, doses_of_vaccine, vaccine_status,
         symptoms_duration, previously_approved, research_prioritizing,
         drug_additional_details, when_symptom_acute_covid_year,
         when_symptom_acute_covid_month, bmi, gfr, wbc, pulse_ox,
         creatinine, hospitalization_length)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        report_id, extra.get("care_acute_covid"), extra.get("doses_of_vaccine"),
        extra.get("vaccine_status_generic"), extra.get("symptoms_duration"),
        1 if extra.get("previously_approved") else 0,
        extra.get("research_prioritizing"), extra.get("drug_additional_details"),
        extra.get("when_symptom_acute_covid_year"),
        extra.get("when_symptom_acute_covid_month"),
        extra.get("BMI"), extra.get("GFR"), extra.get("WBC"),
        extra.get("Pulse_ox"), extra.get("creatinine"),
        extra.get("hospitalization_length"),
    ))

    # Vaccines received
    for v in extra.get("vaccine_received", []) or []:
        val = v.get("value") if isinstance(v, dict) else v
        if val:
            conn.execute(
                "INSERT INTO vaccines_received (report_id, vaccine) VALUES (?, ?)",
                (report_id, val)
            )

    # Comorbidities developed after (Long COVID specific)
    for c in extra.get("comorbidities_after_pasc", []) or []:
        val = c.get("value") if isinstance(c, dict) else c
        if val:
            conn.execute(
                "INSERT INTO comorbidities_after (report_id, value) VALUES (?, ?)",
                (report_id, val)
            )

    # Regular medicines
    for m in extra.get("regular_medicines", []) or []:
        conn.execute(
            "INSERT INTO regular_medicines (report_id, drug_id, drug_name) VALUES (?, ?, ?)",
            (report_id, m.get("id"), m.get("name", ""))
        )


def main():
    if DB_PATH.exists():
        DB_PATH.unlink()
        print(f"Removed existing {DB_PATH.name}")

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")

    create_schema(conn)

    total_reports = 0
    for filename, disease_name, disease_id in REPORT_FILES:
        filepath = DATA_DIR / filename
        if not filepath.exists():
            print(f"  SKIP {filename} (not found)")
            continue

        conn.execute(
            "INSERT OR IGNORE INTO diseases (id, name) VALUES (?, ?)",
            (disease_id, disease_name)
        )

        data = json.loads(filepath.read_text())
        reports = data.get("results", [])
        for case in reports:
            ingest_report(conn, case, disease_id)
        total_reports += len(reports)
        print(f"  {filename}: {len(reports)} reports")

    conn.commit()

    # Create useful indexes
    conn.executescript("""
        CREATE INDEX IF NOT EXISTS idx_reports_disease ON reports(disease_id);
        CREATE INDEX IF NOT EXISTS idx_patients_report ON patients(report_id);
        CREATE INDEX IF NOT EXISTS idx_report_drugs_report ON report_drugs(report_id);
        CREATE INDEX IF NOT EXISTS idx_report_drugs_drug ON report_drugs(drug_id);
        CREATE INDEX IF NOT EXISTS idx_symptoms_report ON symptoms(report_id);
        CREATE INDEX IF NOT EXISTS idx_symptoms_symptom ON symptoms(symptom);
        CREATE INDEX IF NOT EXISTS idx_symptom_outcomes_report ON symptom_outcomes(report_id);
        CREATE INDEX IF NOT EXISTS idx_symptom_outcomes_symptom ON symptom_outcomes(symptom);
        CREATE INDEX IF NOT EXISTS idx_symptom_outcome_drugs_outcome ON symptom_outcome_drugs(symptom_outcome_id);
        CREATE INDEX IF NOT EXISTS idx_symptom_outcome_drugs_name ON symptom_outcome_drugs(drug_name);
        CREATE INDEX IF NOT EXISTS idx_comorbidities_patient ON comorbidities(patient_id);
        CREATE INDEX IF NOT EXISTS idx_comorbidities_after_report ON comorbidities_after(report_id);
    """)
    conn.commit()

    # Print summary
    print(f"\n{'='*50}")
    print(f"Database: {DB_PATH}")
    print(f"Total reports ingested: {total_reports}")
    for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
        count = conn.execute(f"SELECT COUNT(*) FROM [{row[0]}]").fetchone()[0]
        print(f"  {row[0]}: {count} rows")

    conn.close()


if __name__ == "__main__":
    main()
