# Week 10 Log — Streaming Simulation

**Week:** 10  
**Date range:** [02/10/26 - 09/10/26]  
**Team:** Team 05  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Implement a controlled Structured Streaming simulation for GridPulse meter events using JSON file drops in Databricks.

The pipeline validates incoming events, handles duplicates and invalid records, applies a 15-minute watermark, separates trusted and quarantine events, and validates checkpoint-based replay behavior.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Defined explicit 15-field streaming event schema | Team 05 | Done | `streaming/kafka_event_schema.json` |
| Implemented controlled JSON file streaming | Team 05 | Done | `notebooks/07_streaming_simulation.ipynb` |
| Added event timestamp parsing and 15-minute watermark | Team 05 | Done | Week 10 notebook |
| Added event ID deduplication | Team 05 | Done | Week 10 notebook |
| Added meter and building reference validation | Team 05 | Done | Week 10 notebook |
| Added business-rule validation | Team 05 | Done | Week 10 notebook |
| Created trusted streaming output | Team 05 | Done | `workspace.default.trusted_silver_meter_events` |
| Created quarantine output | Team 05 | Done | `workspace.default.quarantine_meter_events` |
| Validated malformed/schema-drift payload handling | Team 05 | Done | `screenshots/week10_raw_payload_evidence.png` |
| Performed sequence validation | Team 05 | Done | Week 10 notebook |
| Validated checkpoint replay behavior | Team 05 | Done | `screenshots/week10_replay_evidence.png` |
| Created final trusted event fact table | Team 05 | Done | `workspace.default.fact_meter_event_week10_final` |
| Documented streaming architecture | Team 05 | Done | `streaming/structured_streaming_design.md` |

---

## 3. Key Decisions

- Used controlled JSON file streaming instead of deploying a live Kafka broker because the Week 10 requirement is a controlled streaming simulation.
- Used an explicit 15-field event schema instead of relying on automatic schema inference.
- Applied a 15-minute watermark and event ID deduplication.
- Separated trusted and quarantine records so invalid events are not silently treated as trusted.
- Used checkpoint locations to validate replay behavior.
- Used available GridPulse event reference data because the project environment did not provide permission to use the existing Silver schema.
- Stored Week 10 streaming outputs under `workspace.default` because `workspace.gridpulse_silver` was not writable by the notebook user.
- Performed sequence validation as a batch validation step because the required non-time-window `lag()` operation was not supported directly in the streaming query.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| No `USE SCHEMA` permission on `workspace.gridpulse_silver` | Streaming outputs could not be written to the existing Silver schema | Environment/admin permission if Silver placement is required |
| Non-time-window `lag()` not supported directly in streaming query | Sequence validation was implemented as a separate batch validation step | No immediate help required |
| Controlled file streaming environment rather than live Kafka | Kafka broker was not deployed | No immediate help required; controlled simulation satisfies the current implementation |
| Source files contained malformed and intentionally invalid records | Required quarantine and raw-payload validation | Handled within Week 10 pipeline |

---

## 5. Evidence Added to GitHub

- `notebooks/07_streaming_simulation.ipynb`
- `streaming/structured_streaming_design.md`
- `streaming/kafka_event_schema.json`
- `weekly_logs/week10_log.md`
- `screenshots/week10_streaming_validation.png`
- `screenshots/week10_quarantine_evidence.png`
- `screenshots/week10_raw_payload_evidence.png`
- `screenshots/week10_replay_evidence.png`

---

## 6. Validation Results

| Validation | Result |
|---|---:|
| Trusted records | 190 |
| Quarantine records | 8 |
| Total validated records | 198 |
| Distinct trusted event IDs | 190 |
| Distinct meters | 21 |
| Distinct buildings | 5 |
| Sequence anomaly records | 2 |
| Watermark | 15 minutes |
| Deduplication | PASS |
| Reference validation | PASS |
| Replay/checkpoint test | PASS |
| No-new-file test | PASS |
| Raw payload retention | PASS |
| Quarantine handling | PASS |

The final trusted fact table is:

`workspace.default.fact_meter_event_week10_final`

with **190 trusted records**.

---

## 7. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted with Structured Streaming code guidance, debugging, validation planning, documentation drafting, and troubleshooting Databricks permission issues. |
| What we changed after AI suggestion | The streaming implementation was adapted to the actual Databricks environment, including the available volume location and the `workspace.default` output location. |
| What we verified manually | Input files, schema fields, streaming outputs, trusted/quarantine counts, reference validation, sequence anomalies, raw payload evidence, checkpoint replay behavior, and final fact-table counts were verified in Databricks. |
| What we can explain without AI | The team can explain the streaming architecture, schema, watermarking, deduplication, validation rules, quarantine handling, checkpointing, sequence validation, and trusted event flow. |

---

## 8. Final Status

**Week 10 Status: COMPLETED**

The controlled streaming simulation successfully processed the GridPulse event drops and produced trusted and quarantine outputs.

Final results:

- **190 trusted events**
- **8 quarantine events**
- **198 validated parsed events**
- **2 sequence anomalies identified**
- **21 distinct meters**
- **5 distinct buildings**
- **15-minute watermark configured**
- **Checkpoint replay test passed**
- **No-new-file test passed**

---

## 9. Next Week Preparation

- Connect Databricks Gold/streaming outputs to Power BI.
- Configure the Databricks SQL connection required for Power BI.
- Validate that dashboard data loads correctly.
- Build dashboard visuals using the GridPulse Gold metrics.
- Prepare dashboard evidence/screenshots for the next sprint.
