# Week 09 Log — Dashboard Refinement and Insight Communication

**Week:** 9  
**Date range:** September 2026  
**Team:** Team 05 – GridPulse  
**Project:** GridPulse: Campus Energy Command Center

---

## 1. Sprint Goal

The goal of Week 9 was to refine the existing Week 8 Gold-only Power BI dashboard and complete the remaining dashboard pages for detailed analysis and operational monitoring.

The work focused on improving dashboard usability, testing slicers and visual interactions, validating dashboard behaviour, and preparing evidence-backed insights without changing the approved Gold KPI definitions.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Refined the existing Week 8 Power BI dashboard | Team 05 | Done | `dashboard/powerbi_dashboard.pbix` |
| Completed Page 1 – Campus Energy Overview | Team 05 | Done | Power BI dashboard / `screenshots/week09_*` |
| Completed Page 2 – Building & Load Analysis | Team 05 | Done | Power BI dashboard / `screenshots/week09_*` |
| Completed Page 3 – Meter Health & Live Operations | Team 05 | Done | Power BI dashboard / `screenshots/week09_*` |
| Added and tested dashboard slicers and visual interactions | Team 05 | Done | Power BI dashboard |
| Added building-level energy, demand, cost and intensity analysis | Team 05 | Done | Page 2 |
| Added meter health, anomaly, completeness and operational visuals | Team 05 | Done | Page 3 |
| Added Week 10 live meter feed placeholder | Team 05 | Done | Page 3 |
| Reviewed dashboard visual hierarchy, labels and readability | Team 05 | Done | Power BI dashboard |
| Validated dashboard behaviour using available Gold exports | Team 05 | Done | Power BI dashboard / Gold CSV exports |
| Prepared dashboard insight documentation | Team 05 | Done | `docs/dashboard_insights.md` |
| Updated dashboard documentation | Team 05 | Done | `dashboard/README.md` |
| Added Week 9 dashboard evidence screenshots | Team 05 | Done | `screenshots/week09_*` |

---

## 3. Key Decisions

- Continued with the same validated Week 8 Gold-only Power BI model instead of rebuilding the dashboard.
- Kept the approved Gold-layer KPI definitions and avoided introducing unsupported KPI logic.
- Used dimensional relationships with single-direction filtering where appropriate.
- Avoided unsafe direct relationships between independent Gold summary tables.
- Kept the `dim_building → dim_meter → agg_meter_health_daily` relationship path for meter-health analysis.
- Used the Week 10 live meter feed as a placeholder on the operational dashboard rather than implementing streaming functionality during Week 9.
- Used evidence-backed observations for dashboard insights instead of inventing unsupported conclusions.
- Kept dashboard pages focused on campus overview, building/load analysis, and meter health/live operations.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Databricks access was unavailable during the Power BI refinement stage | Direct Databricks-side rechecking could not be performed | Continued validation using the approved Gold exports already available |
| Some Gold summary tables contain different grains | Direct relationships between independent summaries could create incorrect filtering | Used dimensional relationships and avoided unnecessary direct joins |
| Live streaming data was not part of the Week 9 scope | Real-time meter feed could not be implemented yet | Week 10 streaming work |

---

## 5. Evidence Added to GitHub

- `dashboard/powerbi_dashboard.pbix`
- `dashboard/README.md`
- `docs/dashboard_insights.md`
- `screenshots/week09_*.png`
- `weekly_logs/week09_log.md`
- `notebooks/06_powerbi_export.ipynb`
- Gold exports in `data_sample/gold_exports/`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped with dashboard planning, Power BI measure structure, relationship troubleshooting, visual selection, documentation structure and insight-writing guidance. |
| What we changed after AI suggestion | Suggestions were adapted to the actual Gold tables, available fields, dashboard requirements and existing Power BI model. |
| What we verified manually | Table fields, relationships, measure behaviour, slicers, visual responses, dashboard values and the final Power BI pages were manually checked. |
| What we can explain without AI | We can explain the dashboard pages, Gold data sources, KPI measures, relationships, slicers, visual purpose and the reasoning behind the dashboard design. |

---

## 7. Next Week Preparation

- Prepare for Week 10 streaming and live meter-data integration.
- Connect the future live meter feed to the operational dashboard where applicable.
- Continue monitoring dashboard behaviour after streaming integration.
- Preserve the approved Gold-layer reporting model while extending the solution for live operations.
