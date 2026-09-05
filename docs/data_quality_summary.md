# Data Quality Summary

**Week:** 6  
**Project:** GridPulse – Campus Energy Command Center  
**Purpose:** Summarize data quality rules, failures and business impact.

---

## 1. Quality Rule Results

| Rule ID | Rule Name | Severity | Failed Count | Business Impact |
|---|---|---|---:|---|
| DQ-01 | Required fields NULL check | High | 0 | Missing reading IDs, meter IDs, timestamps, or energy values would make records unreliable for analysis. |
| DQ-02 | Duplicate reading_id check | High | 0 | Duplicate readings could double-count consumption and distort dashboard metrics. |
| DQ-03 | Negative energy_kwh check | High | 0 | Negative consumption values could produce incorrect energy totals and misleading analytics. |
| DQ-04 | Future reading_ts check | Medium | 0 | Future-dated readings could affect time-based trends, reporting periods, and operational analysis. |
| DQ-05 | Meter reference check | High | 0 | Consumption records with unknown meters could not be reliably linked to meter and building information. |

---

## 2. Failed Record Examples

No failed records were found in the current Silver dataset.

| Rule ID | Sample Record ID | Failure Reason | Action / Handling |
|---|---|---|---|
| — | — | No failures detected | No records required quarantine or exclusion. |

---

## 3. What Should Block Gold Metrics?

The following conditions should block or flag records before Gold metrics are generated:

- **DQ-01 — Required fields:** Records missing required identifiers, timestamps, or energy values should be flagged because they cannot be reliably analyzed.
- **DQ-02 — Duplicate readings:** Duplicate `reading_id` records should be flagged to prevent double-counting.
- **DQ-03 — Negative energy:** Negative `energy_kwh` values should be flagged because they can distort consumption metrics.
- **DQ-05 — Missing meter reference:** Records whose `meter_id` does not exist in the meter master should be flagged because building-level joins may fail.

Future timestamps (DQ-04) should also be flagged for investigation before they are used in time-based Gold metrics.

---

## 4. Quality Summary

The Week 6 data quality checks were executed against the GridPulse Silver consumption dataset.  
Five meaningful data quality rules were evaluated covering required fields, duplicates, negative energy values, future timestamps, and meter reference integrity.  
All five rules returned zero failed records in the current dataset.  
No failed records were available for quarantine or exclusion, so no artificial failures were created.  
The absence of failures indicates that the current Silver consumption data is structurally consistent with the tested quality rules.  
Duplicate readings and negative energy values are particularly important because they could directly distort campus energy metrics.  
Missing meter references could affect joins between consumption, meters, and buildings.  
The mentor should review the DQ rule definitions and evidence screenshots to confirm that the checks are appropriate for the GridPulse pipeline.

---

## 5. AI Transparency Note

AI assistance was used to help structure and refine the data quality checks and documentation.  
The DQ rules were reviewed against the GridPulse project requirements, and the reported failure counts were taken from actual Databricks execution results.  
No synthetic failures were introduced merely to demonstrate the DQ process.
