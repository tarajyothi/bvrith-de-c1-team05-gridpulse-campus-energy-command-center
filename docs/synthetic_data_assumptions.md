# Synthetic Data Assumptions

**Week:** 2  
**Purpose:** Document how the GridPulse synthetic campus energy data is created and used.

---

## 1. Synthetic Data Boundary

This project uses **synthetic campus energy data only**. The data does not represent any real campus, organization, customer, or utility. It is intended only for educational and internship purposes.

---

## 2. Domain Assumptions

| Area | Assumption |
|---|---|
| Geography / scope |  Fictional GridPulse Campus |
| Time period | January 2026 (15-minute interval energy readings) |
| Source systems | Parquet, CSV, JSON and JSON Lines source files |
| Event types | Energy readings and meter events  |
| Reference data | Buildings, Meters and Tariff Plans  |

---

## 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|------|------------------|--------|
| consumption_readings.parquet | 300000 | Main energy consumption data |
| buildings.json | 20 | Building master data |
| meters.csv | 120 | Meter reference data |
| tariffs.csv | 9 | Tariff reference data |
| meter_reading_drop_01.json | 100 | Streaming event sample |
| meter_reading_drop_02.json | 100 | Streaming event sample |

---

## 4. Controlled Data Quality Issues

| Issue Type | Approx. Share | Why Include It |
|---|---:|---|
| Duplicate IDs | 0.2%–0.5% | Tests uniqueness |
| Missing values | 1%–3% | Tests completeness |
| Invalid reference keys | 0.5%–1% | Tests referential integrity |
| Negative / impossible values | 0.1%–0.5% | Tests range rules |
| Timestamp inconsistencies | 0.1%–0.3% | Tests chronology |

---

## 5. Manual Verification

Before using generated data, the team must check:

- Row counts are reasonable.
- Key fields exist.
- Dates and numeric values look realistic.
- Controlled defects exist but do not dominate the dataset.
- Source files are different enough to require real standardization.
