# Week 06 Log — Data Quality Checks

**Week:** 6  
**Date range:** [Add actual Week 6 dates]  
**Team:** [Add your team name / number]  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Implement the eight governed Week 06 Data Quality (DQ) rules, identify failed records, route DQ-invalid records to quarantine, retain trusted records, reconcile candidate/trusted/quarantine counts, and document business impact.

---

## 2. Work Completed

| Task | Status | Evidence |
|---|---|---|
| Created/updated Week 06 Data Quality notebook | Done | `notebooks/04_data_quality_checks.ipynb` |
| Implemented DQ-RDG-001 to DQ-RDG-006 | Done | `week06_dq_results.png` |
| Implemented DQ-MTR-001 | Done | `week06_dq_results.png` |
| Implemented DQ-TRF-001 | Done | `week06_dq_results.png` |
| Created Trusted and Quarantine outputs | Done | Databricks DQ results |
| Captured failed meter records | Done | `week06_failed_records_sample.png` |
| Completed controlled replay | Done | `week06_replay_closure_evidence.png` |
| Retained original quarantined record after replay | Done | `week06_replay_quarantine_closed.png` |
| Updated DQ results documentation | Done | `docs/data_quality_summary.md` |

---

## 3. DQ Results

| Rule ID | Failed Records |
|---|---:|
| DQ-MTR-001 | 90 |
| DQ-RDG-001 | 0 |
| DQ-RDG-002 | 0 |
| DQ-RDG-003 | 0 |
| DQ-RDG-004 | 0 |
| DQ-RDG-005 | 0 |
| DQ-RDG-006 | 0 |
| DQ-TRF-001 | 2 |

### Important DQ observations

- 90 meter master records failed DQ-MTR-001 because of invalid meter-to-building references and/or invalid meter master data.
- 2 tariff master records failed DQ-TRF-001 because of an incompatible effective time-band overlap.
- Reading-level tariff resolution succeeded for all 500 consumption readings.
- No consumption reading records were quarantined.
- No silent deletion of failed physical records was performed.

---

## 4. Trusted and Quarantine Routing

| Entity | Candidate | Trusted | Quarantine | Reconciliation Variance |
|---|---:|---:|---:|---:|
| Buildings | 5 | 5 | 0 | 0 |
| Meters | 120 | 30 | 90 | 0 |
| Consumption Readings | 500 | 500 | 0 | 0 |
| Tariffs | 9 | 7 | 2 | 0 |

Trusted and quarantine outputs were kept separate, and candidate counts reconciled to trusted plus quarantine counts with zero variance.

---

## 5. Business Impact

- 75% of meter master records were quarantined.
- Quarantined meters must not be used for trusted building attribution or downstream Gold aggregation.
- Invalid meter references can affect building-level energy metrics if they are allowed into trusted joins.
- Two tariff master records were quarantined because of an incompatible effective time-band overlap.
- The failed records were retained for controlled correction/replay rather than being silently deleted.

---

## 6. Controlled Replay

A controlled training replay was performed using:

**Source record:** `SRC-MTR-0031`  
**Meter:** `MTR0031`  
**Original building:** `BLD006`  
**Corrected building:** `BLD001`  
**Rule:** `DQ-MTR-001`

The correction was explicitly treated as:

`CONTROLLED_TRAINING_REWORK`

After replay, DQ-MTR-001 returned **0 failed records** and the replay status was **PASS**.

The original quarantined record remained retained in quarantine as evidence.

---

## 7. Blockers / Risks / Limitations

- No approved numeric engineering-limit configuration was available for the upper-bound portions of DQ-RDG-004, so no limits were invented.
- No approved formula tolerance was available for the energy/power consistency portion of DQ-RDG-006, so no unsupported failure threshold was invented.
- No explicit expected active-meter schedule configuration was available for inferring missing intervals in DQ-RDG-005; observable interval continuity and duplicate checks were performed without inventing a schedule.
- The controlled replay correction was a training rework and is not presented as proof of the real source building assignment.

---

## 8. Evidence Added to GitHub

- `notebooks/04_data_quality_checks.ipynb`
- `screenshots/week06_dq_results.png`
- `screenshots/week06_failed_records_sample.png`
- `screenshots/week06_replay_closure_evidence.png`
- `screenshots/week06_replay_quarantine_closed.png`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

---

## 9. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assistance was used to structure the Week 06 DQ implementation and documentation. |
| What was adapted | The implementation was adapted to the actual GridPulse Bronze/Silver tables, fields, rule IDs, and Databricks environment. |
| What was verified manually | All DQ queries, failure counts, routing results, reconciliation checks, and replay results were executed and verified in Databricks. |
| Numeric thresholds | No numeric engineering limits or formula tolerances were invented when approved configuration was unavailable. |
| Final responsibility | The team validated the DQ results, quarantine routing, evidence, and business impact in Databricks. |

---

## 10. Next Week Preparation

- Prepare for Week 07 Gold aggregations and business metrics.
- Use only trusted Silver records for downstream Gold processing.
- Review quarantined records and controlled rework opportunities before downstream aggregation.
