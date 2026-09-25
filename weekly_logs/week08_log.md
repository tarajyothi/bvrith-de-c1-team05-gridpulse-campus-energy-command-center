# Week 08 Log — Power BI Foundation

**Week:** 8  
**Date range:** [11-09-26 to 17-09-26]  
**Team:** Team 05 — GridPulse  
**Project:** GridPulse: Campus Energy Command Center

---

## 1. Sprint Goal

The goal of Week 08 was to establish the Power BI reporting foundation using the approved Gold data outputs. The team exported the required Gold tables, created the Power BI data model and relationships, defined the required measures, and developed the first working dashboard page.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed approved Gold tables required for Power BI | Team 05 | Done | Gold export files |
| Exported Gold tables for Power BI use | Team 05 | Done | `data_sample/gold_exports/` |
| Loaded approved Gold tables into Power BI | Team 05 | Done | Power BI model |
| Set appropriate field data types | Team 05 | Done | Power BI Model/Data view |
| Created dimension-to-fact relationships | Team 05 | Done | Power BI Model view |
| Built the Campus Energy Overview page | Team 05 | Done | Power BI Page 1 |
| Created energy, demand, cost and building KPI measures | Team 05 | Done | Power BI DAX measures |
| Added KPI cards and dashboard slicers | Team 05 | Done | Power BI Page 1 |
| Added daily energy, building consumption, campus demand and energy cost visuals | Team 05 | Done | Power BI Page 1 |
| Checked dashboard values and slicer behaviour | Team 05 | Done | Power BI dashboard |
| Documented the Power BI source and model structure | Team 05 | Done | `dashboard/README.md` |

---

## 3. Key Decisions

- Power BI uses the approved Gold outputs as the reporting source.
- Dashboard design was based on the required business questions rather than creating a visual for every Gold table.
- Dimension-to-fact relationships were configured as one-to-many with controlled filter direction.
- Unsupported direct relationships between independent Gold summaries were avoided.
- Page 1 was designed as the overall campus energy overview with KPIs, trends, comparisons and filters.
- The Week 08 Power BI report was retained as the foundation for Week 09 refinement.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Databricks access was not available during the Power BI development stage | Direct querying of Gold data from Databricks was not possible | Used the approved Gold exports for Power BI development |
| An incorrect relationship direction was identified during model development | Could affect filtering and KPI results | Reviewed and corrected relationship cardinality and filter direction |
| Some Gold tables are independent summaries | Direct relationships could create incorrect filtering or ambiguity | Kept unsupported direct relationships separate |

---

## 5. Evidence Added to GitHub

- `notebooks/06_powerbi_export.ipynb`
- `data_sample/gold_exports/`
- `dashboard/powerbi_dashboard.pbix`
- `dashboard/README.md`
- `screenshots/week08_*`
- `weekly_logs/week08_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped with Power BI dashboard planning, DAX syntax, relationship troubleshooting, visual selection and explaining Power BI features. |
| What we changed after AI suggestion | Suggestions were reviewed against the actual GridPulse Gold tables and project requirements. Only relevant visuals, measures and relationships were retained. |
| What we verified manually | Gold table fields, Power BI relationships, measure behaviour, slicers, chart responses and dashboard values were checked manually in Power BI. |
| What we can explain without AI | The team can explain the Gold-to-Power-BI flow, table relationships, KPI measures, dashboard structure and the purpose of the Page 1 visuals. |

---

## 7. Next Week Preparation

- Continue with the validated Week 08 Power BI model.
- Complete and refine the detailed analysis and meter-health dashboard pages.
- Test slicer and visual interactions.
- Reconcile important dashboard values with their owning Gold tables.
- Prepare evidence-backed dashboard insights.
