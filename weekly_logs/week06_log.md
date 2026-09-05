# Week 06 Log — Data Quality Checks

**Week:** 6  
**Date range:** [Add actual Week 6 dates]  
**Team:** [Add your team name / number]  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Run meaningful data quality checks on the GridPulse Silver data, identify any failed records, and document the results and business impact.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created Week 6 Data Quality notebook | Team | Done | `notebooks/04_data_quality_checks.ipynb` |
| Required-field NULL check | Team | Done | `week06_dq_results.png` |
| Duplicate `reading_id` check | Team | Done | `week06_dq_results.png` |
| Negative `energy_kwh` check | Team | Done | `week06_dq_results.png` |
| Future `reading_ts` check | Team | Done | `week06_dq_results.png` |
| Meter reference check | Team | Done | `week06_dq_results.png` |
| Failed-record evidence | Team | Done | `week06_failed_records_sample.png` |
| DQ results documentation | Team | Done | `docs/data_quality_summary.md` |

---

## 3. Key Decisions

- Used the GridPulse Silver consumption data as the primary dataset for Week 6 DQ checks.
- Added checks for required fields, duplicate readings, negative energy values, future timestamps, and missing meter references.
- Reported the actual Databricks results without creating artificial failures.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| No data quality failures were found in the current Silver dataset | No failed-record examples were available for quarantine testing | None |

---

## 5. Evidence Added to GitHub

- `notebooks/04_data_quality_checks.ipynb`
- `screenshots/week06_dq_results.png`
- `screenshots/week06_failed_records_sample.png`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the Week 6 data quality checks and organize the DQ documentation. |
| What we changed after AI suggestion | The suggested checks were adapted to the actual GridPulse Silver table names and fields. |
| What we verified manually | All DQ queries and failure counts were executed and verified in Databricks. |
| What we can explain without AI | We can explain the purpose of each DQ rule, the zero-failure results, and how data quality issues could affect Gold metrics and dashboards. |

---

## 7. Next Week Preparation

- Prepare for Week 7 Gold aggregations and business metrics.
- Review the Silver tables and DQ results before creating Gold tables.
