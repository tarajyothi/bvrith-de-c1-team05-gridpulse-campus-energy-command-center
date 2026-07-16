# [GridPulse: Campus Energy Command Center]

> **Student note:** Start with `00_START_HERE.md` and `00_TEMPLATE_INDEX.md`. The placeholder files inside this repo are the templates.

**Program:** ZENAIZ x BVRIT Hyderabad Data Engineering Internship Program  
**Track:** Data Engineering  
**Duration:** 12 Weeks  
**Team:** [ Team 05 / GridPulse ]  
**Students:** [Ms.Diddala Tara Jyothi], [Ms.Hari Nanditha], [Ms. Shiva Sri]  
**AI Teammate:** Used responsibly for explanation, debugging, review, and documentation support.

---

## 1. Project Summary

- **Domain:** Campus Energy Management
- **Core engineering problem:** Transform raw campus energy consumption data into accurate, reliable, and actionable insights for monitoring and decision-making.
- **Main pipeline:** Raw Energy Data → Bronze Layer → Silver Layer → Data Quality Checks → Gold Layer → Power BI Dashboard → Streaming Simulation
- **Final outcome:** GitHub repository, Databricks notebooks, Bronze/Silver/Gold datasets, Power BI dashboard, streaming simulation, and final project demonstration.
---

## 2. Tools Used

| Tool | Purpose |
|---|---|
| Databricks Free Edition | Process campus energy data using Spark SQL, PySpark, and Bronze/Silver/Gold architecture |
| GitHub | Repository management, version control, weekly documentation, screenshots, and commits |
| Power BI Desktop | Visualize Gold layer data through interactive dashboards |
| AI Assistant | Used responsibly for explanation, debugging, code review, and documentation support with manual verification |

---


## 3. Repository Navigation

| Folder / File | Purpose |
|---|---|
| `docs/` | Project documentation, data dictionary, DQ summary, Gold metric definitions |
| `src/` | Data generation and reusable quality helper scripts |
| `notebooks/` | Databricks notebooks for exploration, Bronze, Silver, DQ, Gold, export, streaming |
| `data_sample/` | Small sample raw/streaming data only; do not store large files |
| `dashboard/` | Power BI `.pbix` file and dashboard notes |
| `streaming/` | Streaming design, JSON event schema, Kafka-style design awareness |
| `screenshots/` | Weekly evidence screenshots |
| `weekly_logs/` | Weekly execution logs and AI transparency notes |
| `final_submission/` | Final report, demo script, team contribution, checklist |

---

## 4. 12-Week Execution Map

| Week | Focus | Main Evidence |
|---:|---|---|
| 1 | Project framing + GitHub | README, problem charter, Week 1 log |
| 2 | Dataset design | Data dictionary, assumptions, sample data plan |
| 3 | Databricks exploration | Exploration notebook, schema/count screenshots |
| 4 | Bronze ingestion | Bronze notebook, raw-to-Bronze reconciliation |
| 5 | Silver standardization | Silver notebook, canonical mapping evidence |
| 6 | Data quality | DQ rules, DQ notebook, DQ summary |
| 7 | Gold metrics | Gold tables and metric definitions |
| 8 | Power BI draft | Gold export and first dashboard draft |
| 9 | Dashboard refinement | Final dashboard screenshots and insights |
| 10 | Streaming simulation | Auto Loader / Structured Streaming notebook and live metric |
| 11 | Integration | Pipeline walkthrough, cleaned README, final evidence |
| 12 | Final demo | Final report, demo script, contribution note |

---

## 5. Important Rules

- Do not connect Power BI directly to raw CSV files. Power BI must use Gold outputs.
- Do not submit copied internet GitHub repositories as your own project.
- External references must be listed in `docs/references.md`.
- AI-generated code or content must be verified and explainable.
- Every week must have a GitHub commit and weekly log.
- Keep sample data small in GitHub. Large generated data should be recreated using scripts or uploaded to Databricks separately.

---

## 6. Final Project Proof

By Week 12, this repository should prove:

- We designed source datasets.
- We processed batch data in Databricks.
- We created Bronze tables.
- We standardized Silver tables.
- We implemented data quality checks.
- We created Gold metric tables.
- We built Power BI dashboards from Gold outputs.
- We simulated streaming JSON events.
- We documented weekly evidence in GitHub.
- We can explain and defend the full project.
