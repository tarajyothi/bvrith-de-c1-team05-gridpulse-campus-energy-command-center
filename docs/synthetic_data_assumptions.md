# Synthetic Data Assumptions

**Week:** 2  
**Purpose:** Document how educational data is created.

---

## 1. Synthetic Data Boundary

This project uses synthetic educational data only. It must not be presented as real company, customer, citizen, player, patient, government, or platform data.

---

## 2. Domain Assumptions

| Area | Assumption |
|---|---|
| Geography / scope | [Example: Hyderabad and nearby regions] |
| Time period | [Example: July to September 2026] |
| Source systems | [Example: Two different operational feeds] |
| Event types | [Example: booking, scan, alert, transaction] |
| Reference data | [Example: zones, categories, products, venues] |

---

## 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|---|---:|---|
| `[source_file_1].csv` | [rows] | [reason] |
| `[source_file_2].csv` | [rows] | [reason] |
| `[reference_file].csv` | [rows] | [reason] |
| `[streaming_events].json` | [rows] | [reason] |

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
