# Week 07 Log — Gold Layer & Dashboard Metrics

**Week:** 7  
**Date range:**   
**Team:** Team 5  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Build the approved Gold layer for GridPulse using trusted Silver data.

Create dashboard-ready dimensions, facts, and aggregate tables while preserving the approved data grain, tariff logic, data-quality status, and lineage requirements.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created Gold schema | Team 5 | Done | `workspace.gridpulse_gold` |
| Created `dim_date` | Team 5 | Done | `week07_dim_date_validation.png` |
| Created `dim_time_band` | Team 5 | Done | `week07_dim_time_band_validation.png` |
| Created `dim_building` | Team 5 | Done | `week07_dim_building_validation.png` |
| Created `dim_meter` | Team 5 | Done | `week07_dim_meter_validation.png` |
| Created `dim_tariff` from trusted tariff data | Team 5 | Done | `week07_dim_tariff_validation.png` |
| Created `fact_meter_reading` | Team 5 | Done | `week07_fact_meter_reading_validation.png` |
| Created schema-ready `fact_meter_event` | Team 5 | Done | `week07_fact_meter_event_validation.png` |
| Created `agg_building_consumption_daily` | Team 5 | Done | `week07_agg_building_consumption_daily.png` |
| Created `agg_peak_load_interval` | Team 5 | Done | `week07_agg_peak_load_interval.png` |
| Created `agg_meter_health_daily` | Team 5 | Done | `week07_agg_meter_health_daily.png` |
| Created `agg_energy_cost_daily` | Team 5 | Done | `week07_agg_energy_cost_daily.png` |
| Created `agg_campus_anomaly_daily` | Team 5 | Done | `week07_agg_campus_anomaly_daily.png` |
| Validated Gold outputs with SQL queries | Team 5 | In progress | Gold validation screenshots |

---

## 3. Key Decisions

- Used `workspace.gridpulse_gold` as the dedicated Gold schema.
- Built the approved Gold dimensions: `dim_date`, `dim_time_band`, `dim_building`, `dim_meter`, and `dim_tariff`.
- Built the approved Gold facts: `fact_meter_reading` and schema-ready `fact_meter_event`.
- Used trusted Silver records with `dq_status = 'PASS'` for Gold fact and aggregate calculations.
- Kept `fact_meter_event` schema-ready and empty until Week 10 streaming events are available.
- Calculated campus peak demand using the sum of active power across meters at the same reading interval rather than taking the maximum individual meter power.
- Used the approved tariff records without inventing missing tariff rates.
- Preserved tariff-matching results so that unmatched tariff intervals remain visible instead of being silently assigned an assumed rate.
- Created daily building consumption, peak-load interval, meter-health, energy-cost, and campus-anomaly aggregates.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| PLAN-A has no approved tariff covering the 18:00–22:00 interval | Some PLAN-A readings do not have a matching tariff ID or estimated cost | Confirm tariff configuration from the approved source; do not invent a tariff rate |
| Final Gold reconciliation and orphan/grain validation still need to be completed | Week 07 Gold layer is not yet fully signed off | Complete final validation before marking the sprint fully complete |

---

## 5. Evidence Added to GitHub

- `notebooks/05_gold_aggregations.ipynb`
- `screenshots/week07_dim_date_validation.png`
- `screenshots/week07_dim_time_band_validation.png`
- `screenshots/week07_dim_building_validation.png`
- `screenshots/week07_dim_meter_validation.png`
- `screenshots/week07_dim_tariff_validation.png`
- `screenshots/week07_fact_meter_reading_validation.png`
- `screenshots/week07_fact_meter_event_validation.png`
- `screenshots/week07_agg_building_consumption_daily.png`
- `screenshots/week07_agg_peak_load_interval.png`
- `screenshots/week07_agg_meter_health_daily.png`
- `screenshots/week07_agg_energy_cost_daily.png`
- `screenshots/week07_agg_campus_anomaly_daily.png`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used to help structure the Gold-layer SQL, explain the approved Gold architecture, suggest validation queries, and identify appropriate evidence screenshots. |
| What we changed after AI suggestion | The team reviewed the suggested SQL against the actual Silver schemas and project playbook, then adjusted table names, joins, fields, and validation queries to match the actual GridPulse data. |
| What we verified manually | Gold table creation, row counts, schemas, sample records, tariff matches, aggregate outputs, and SQL query results were checked directly in Databricks. |
| What we can explain without AI | The team can explain the Bronze-to-Silver-to-Gold flow, Gold dimensions and facts, trusted-data filtering, tariff matching, aggregate calculations, campus peak-load calculation, and the purpose of each Gold output. |

---

## 7. Next Week Preparation

- Review and complete final Gold grain, orphan-key, and reconciliation checks.
- Prepare the validated Gold layer for Power BI dashboard development in Week 08.
