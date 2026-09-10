# Week 06 Log — Data Quality Checks

**Week:** 6  
**Date range:**  
**Team:** Team 5  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Implement and validate the Week 06 Data Quality checks on the trusted Silver data.

Identify nulls, duplicate readings, negative energy values, future timestamps, and missing meter references before downstream Gold processing.

---

## 2. Work Completed

| Task | Status | Evidence |
|---|---|---|
| Created/updated Week 06 Data Quality notebook | Done | `notebooks/04_data_quality_checks.ipynb` |
| Implemented DQ-01 required fields check | Done | `week06_dq_results.png` |
| Implemented DQ-02 duplicate `reading_id` check | Done | `week06_dq_results.png` |
| Implemented DQ-03 negative `energy_kwh` check | Done | `week06_dq_results.png` |
| Implemented DQ-04 future `reading_ts` check | Done | `week06_dq_results.png` |
| Implemented DQ-05 missing meter reference check | Done | `week06_dq_results.png` |
| Created DQ summary output | Done | `week06_dq_results.png` |
| Captured failed-record validation | Done | `week06_failed_records_sample.png` |

---

## 3. DQ Results

| Rule ID | DQ Rule | Failed Records |
|---|---|---:|
| DQ-01 | Required fields NULL check | 0 |
| DQ-02 | Duplicate `reading_id` check | 0 |
| DQ-03 | Negative `energy_kwh` check | 0 |
| DQ-04 | Future `reading_ts` check | 0 |
| DQ-05 | Missing meter reference check | 0 |

### Important DQ observations

- No NULL values were found in the required reading fields.
- No duplicate `reading_id` values were found.
- No negative `energy_kwh` values were found.
- No future-dated readings were found.
- No consumption readings referenced a missing meter.
- No failed records were identified in the current Silver dataset.
- No records were silently deleted.

---

## 4. DQ Validation Summary

| Check | Result |
|---|---|
| Required fields validation | PASS |
| Duplicate reading validation | PASS |
| Negative energy validation | PASS |
| Future timestamp validation | PASS |
| Meter reference validation | PASS |

All implemented DQ checks returned zero failed records for the current Silver dataset.

---

## 5. Business Impact

- The current Silver consumption dataset passed all implemented Week 06 validation checks.
- No invalid consumption records required quarantine based on the checks executed.
- Validating meter references before Gold processing helps prevent orphan meter records from affecting downstream building-level metrics.
- Validating timestamps and energy values helps protect downstream energy and demand calculations.
- The DQ results provide evidence that the current sample is suitable for the next Gold-layer processing stage.

---

## 6. Failed Record Validation

A failed-record validation was executed after the DQ checks.

Result:

- DQ-01: 0 failed records
- DQ-02: 0 failed records
- DQ-03: 0 failed records
- DQ-04: 0 failed records
- DQ-05: 0 failed records

No failed records were available for a quarantine sample in the current Silver dataset.

---

## 7. Blockers / Risks / Limitations

- The current Week 06 implementation covers the DQ checks that were executed and verified in Databricks.
- No artificial defects were introduced merely to produce failed-record screenshots.
- The current sample contains no failures for the implemented checks, so quarantine behavior was not demonstrated with an actual failed consumption record.
- Additional governed DQ rules can be added when their approved configuration and implementation are available.

---

## 8. Evidence Added to GitHub

- `notebooks/04_data_quality_checks.ipynb`
- `screenshots/week06_dq_results.png`
- `screenshots/week06_failed_records_sample.png`
- `weekly_logs/week06_log.md`

---

## 9. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assistance was used to structure the Week 06 DQ notebook, explain validation logic, and organize the DQ documentation. |
| What was adapted | The suggested checks were adapted to the actual GridPulse Silver table names, fields, and Databricks environment. |
| What was verified manually | All DQ queries and their results were executed and checked directly in Databricks. |
| Failure handling | No artificial failures were created when the actual dataset returned zero failures. |
| Final responsibility | The team validated the DQ results and evidence in Databricks and is responsible for the final interpretation. |

---

## 10. Next Week Preparation

- Prepare the validated Silver data for Week 07 Gold processing.
- Build the approved Gold dimensions, facts, and aggregate tables.
- Validate Gold table grain, joins, and business metrics before dashboard development.
