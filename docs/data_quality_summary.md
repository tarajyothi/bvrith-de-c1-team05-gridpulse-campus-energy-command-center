# Data Quality Summary

**Week:** 6  
**Project:** GridPulse – Campus Energy Command Center  
**Purpose:** Summarize governed data quality rules, failures, quarantine routing, reconciliation, and business impact.

---

## 1. Quality Rule Results

| Rule ID | Rule Name | Severity | Failed Count | Business Impact |
|---|---|---|---:|---|
| DQ-RDG-001 | Reading ID present/unique and meter-timestamp uniqueness | Critical | 0 | Duplicate or missing reading identifiers could cause incorrect consumption counts and unreliable analysis. |
| DQ-RDG-002 | Meter resolves to valid building assignment at reading timestamp | Critical | 0 | Invalid meter/building resolution could cause incorrect building attribution and downstream aggregation. |
| DQ-RDG-003 | Timestamp validity, 15-minute boundary, project-window and future-date checks | Major | 0 | Invalid timestamps could distort time-based reporting and operational analysis. |
| DQ-RDG-004 | Required numeric fields, non-negative values and supported validity checks | Critical | 0 | Invalid energy or electrical measurements could produce unreliable energy and load metrics. |
| DQ-RDG-005 | 15-minute interval, gap and duplicate-interval checks | Major | 0 | Missing or duplicated intervals could affect meter health and time-series completeness. |
| DQ-RDG-006 | Power-factor validity and energy/power consistency evidence | Major | 0 | Physically inconsistent readings could affect energy and load calculations. |
| DQ-MTR-001 | Building/meter master validity and meter-to-building reference integrity | Critical | 90 | Invalid meter master records cannot safely participate in trusted building-level joins or downstream Gold aggregation. |
| DQ-TRF-001 | Tariff validity, overlap and effective tariff resolution | Critical | 0* | Ambiguous tariff definitions could cause incorrect cost calculations and tariff assignment. |

\* Reading-level tariff resolution returned 0 failures across 500 readings. Separately, 2 tariff master records were quarantined because TRF003 and TRF009 contain an incompatible effective-date overlap.

---

## 2. Failed Record Examples

### DQ-MTR-001

**Failed physical records:** 90

The failures are primarily caused by invalid meter-to-building references. The failed records include meter IDs such as `MTR0031` onward that reference building IDs that do not resolve against the supplied building master.

One additional failed meter record, `SRC-MTR-0120`, contains invalid master-data values including a negative capacity and an invalid effective-date range.

Example:

| source_record_id | meter_id | building_id | capacity_kw | effective_from | effective_to |
|---|---|---|---:|---|---|
| SRC-MTR-0031 | MTR0031 | BLD006 | 140 | 2026-01-01 | 2026-12-31 |
| SRC-MTR-0032 | MTR0032 | BLD006 | 190 | 2026-01-01 | 2026-12-31 |
| SRC-MTR-0037 | MTR0037 | BLD007 | 140 | 2026-01-01 | 2026-12-31 |
| SRC-MTR-0043 | MTR0043 | BLD008 | 170 | 2026-01-01 | 2026-12-31 |
| SRC-MTR-0050 | MTR0050 | BLD009 | 110 | 2026-01-01 | 2026-12-31 |

All failed meter records were routed to the meter quarantine output.

### DQ-TRF-001

Two tariff master records were quarantined because of an incompatible effective-date overlap between:

- `TRF003`
- `TRF009`

The overlap occurs within the same tariff plan and time band.

---

## 3. Trusted and Quarantine Routing

| Entity | Candidate | Trusted | Quarantine | Reconciliation Variance |
|---|---:|---:|---:|---:|
| Buildings | 5 | 5 | 0 | 0 |
| Meters | 120 | 30 | 90 | 0 |
| Consumption Readings | 500 | 500 | 0 | 0 |
| Tariffs | 9 | 7 | 2 | 0 |

For every implemented entity:

**Candidate = Trusted + Quarantine**

No physical records were silently deleted.

The physical record key used for reconciliation is `source_record_id`.

---

## 4. What Should Block Gold Metrics?

The following conditions should block or prevent affected records from being used in trusted Gold metrics:

- **DQ-RDG-001:** Invalid or duplicate reading identifiers.
- **DQ-RDG-002:** Reading records that cannot resolve to a valid meter/building assignment.
- **DQ-RDG-003:** Invalid, misaligned, outside-window, or future timestamps.
- **DQ-RDG-004:** Invalid required numeric measurements or unsupported physical values.
- **DQ-RDG-005:** Interval and duplicate/gap issues requiring data-quality handling.
- **DQ-RDG-006:** Invalid power factor or approved energy/power consistency failures.
- **DQ-MTR-001:** Invalid meter master records or unresolved building references.
- **DQ-TRF-001:** Invalid or ambiguous tariff definitions or tariff resolution failures.

Quarantined records must not be relabelled as Trusted without controlled correction and replay.

---

## 5. Business Impact

### Meter Master Impact

120 meter master records were evaluated.

**90 records were quarantined, representing 75.0% of the meter candidate data.**

These records cannot safely participate in trusted building-level joins until their master-data issues are corrected.

Using the affected records could cause:

- Incorrect building attribution.
- Incorrect downstream aggregations.
- Unreliable Gold-level campus energy metrics.
- Incorrect relationships between meters, buildings and tariffs.

### Tariff Impact

Two tariff records were quarantined because of an incompatible effective-date overlap.

Seven tariff records remain Trusted.

Reading-level tariff resolution succeeded for all 500 consumption readings evaluated.

### Record Preservation

Failed records were retained in quarantine for controlled correction and replay.

No physical records were silently deleted.

---

## 6. Reconciliation

The DQ implementation verifies that physical records are routed exactly once:

**Candidate = Trusted + Quarantine**

Results:

- Buildings: 5 = 5 + 0
- Meters: 120 = 30 + 90
- Consumption readings: 500 = 500 + 0
- Tariffs: 9 = 7 + 2

All reconciliation variances are **0**.

Trusted and quarantine outputs are therefore disjoint and collectively reconcile to their candidate datasets.

---

## 7. Configuration and Limitations

No approved numeric engineering-limit configuration was available for the upper-bound checks required by DQ-RDG-004.

No approved numeric tolerance was available for the formula-based energy/power consistency check required by DQ-RDG-006.

Therefore:

- Unsupported numeric thresholds were not invented.
- Power-factor validity checks were executed.
- Energy/power consistency was inspected as evidence, but an unsupported pass/fail tolerance was not applied.
- The limitation is explicitly documented rather than hidden.

Similarly, DQ-RDG-005 evaluated observable 15-minute interval continuity and duplicate intervals. An explicit expected-meter schedule configuration was not available, so unsupported expected-reading schedules were not invented.

---

## 8. Evidence

The following evidence was generated from the Databricks execution:

- `week06_dq_results.png` — final DQ rule results and Trusted/Quarantine routing.
- `week06_failed_records_sample.png` — sample of DQ-MTR-001 failed meter records.
- Tariff quarantine output — demonstrates the TRF003/TRF009 effective-date overlap.

---

## 9. AI Transparency Note

AI assistance was used to help structure the Week 06 DQ implementation and documentation.

All rule IDs, fields, failure counts, routing results, and reconciliation results were executed and validated in Databricks against the supplied GridPulse candidate data.

No numeric engineering limits or formula tolerances were invented. Checks requiring approved numeric configuration were reported as not configured rather than assigning unsupported thresholds.

DQ failures were retained at the physical-record level and routed to quarantine without silently deleting records.
