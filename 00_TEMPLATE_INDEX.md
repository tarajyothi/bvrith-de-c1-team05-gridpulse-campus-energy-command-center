# Template Index — Where the Student Templates Are

This file explains exactly where templates are located inside the GitHub starter repo.

## Onboarding Files to Open First

| Open this file first | Why it matters |
|---|---|
| `00_START_HERE.md` | Explains the repo purpose, weekly working method, and AI transparency rule |
| `README.md` | Becomes the project home page for the team repo |
| `REPO_USAGE_GUIDE.md` | Shows week-wise files to update and evidence rules |
| `GITHUB_SETUP_INSTRUCTIONS.md` | Shows the preferred GitHub template setup path and backup ZIP path |
| `00_TEMPLATE_INDEX.md` | Maps every template file to the week in which it is used |

---

## Week-wise Template / Placeholder Files

| Week | Student updates these template files |
|---:|---|
| 1 | `README.md`, `docs/problem_charter.md`, `weekly_logs/week01_log.md` |
| 2 | `docs/data_dictionary.md`, `docs/synthetic_data_assumptions.md`, `src/generate_synthetic_data.py`, `data_sample/raw/` |
| 3 | `notebooks/01_data_exploration.ipynb`, `screenshots/`, `weekly_logs/week03_log.md` |
| 4 | `notebooks/02_bronze_ingestion.ipynb`, `screenshots/`, `weekly_logs/week04_log.md` |
| 5 | `notebooks/03_silver_transformations.ipynb`, `screenshots/`, `weekly_logs/week05_log.md` |
| 6 | `src/data_quality_rules.py`, `notebooks/04_data_quality_checks.ipynb`, `docs/data_quality_summary.md` |
| 7 | `notebooks/05_gold_aggregations.ipynb`, `docs/gold_metrics_definition.md`, `data_sample/gold_exports/` |
| 8 | `notebooks/06_powerbi_export.ipynb`, `dashboard/README.md`, `dashboard/powerbi_dashboard.pbix` |
| 9 | `docs/dashboard_insights.md`, updated dashboard file, screenshots |
| 10 | `notebooks/07_streaming_simulation.ipynb`, `streaming/structured_streaming_design.md`, `streaming/kafka_event_schema.json` |
| 11 | `docs/pipeline_walkthrough.md`, `docs/references.md`, updated `README.md`, final screenshots |
| 12 | `final_submission/final_report.md`, `final_submission/final_demo_script.md`, `final_submission/team_contribution.md`, `final_submission/final_submission_checklist.md` |

---

## Documentation Templates

| Template file | Purpose |
|---|---|
| `docs/problem_charter.md` | Define project problem, scope, success criteria |
| `docs/requirements.md` | List functional, data, dashboard and evidence requirements |
| `docs/data_dictionary.md` | Define source files, fields, types, keys and Silver design |
| `docs/synthetic_data_assumptions.md` | Document synthetic data rules and controlled defects |
| `docs/data_quality_summary.md` | Summarize DQ rules, failures and impact |
| `docs/gold_metrics_definition.md` | Define dashboard-ready KPI formulas and grain |
| `docs/dashboard_insights.md` | Explain Power BI pages and key insights |
| `docs/pipeline_walkthrough.md` | Explain full run order and architecture |
| `docs/references.md` | List official docs, GitHub references and AI references |

---

## Notebook Templates

| Notebook | Purpose |
|---|---|
| `notebooks/01_data_exploration.ipynb` | Load data, inspect schema, counts and nulls |
| `notebooks/02_bronze_ingestion.ipynb` | Create Bronze tables with metadata |
| `notebooks/03_silver_transformations.ipynb` | Create standardized Silver tables |
| `notebooks/04_data_quality_checks.ipynb` | Run DQ checks and document failures |
| `notebooks/05_gold_aggregations.ipynb` | Create Gold metric tables |
| `notebooks/06_powerbi_export.ipynb` | Export Gold outputs for Power BI |
| `notebooks/07_streaming_simulation.ipynb` | Simulate streaming using Auto Loader / Structured Streaming |

---

## Code Templates

| File | Purpose |
|---|---|
| `src/generate_synthetic_data.py` | Generate small synthetic CSV and JSON samples |
| `src/data_quality_rules.py` | Optional reusable Python/PySpark DQ helper functions |

---

## Data Sample Folders

| Folder | Purpose |
|---|---|
| `data_sample/raw/` | Small Week 2 sample CSV/reference files only |
| `data_sample/streaming/` | Small JSON event samples for Week 10 simulation |
| `data_sample/gold_exports/` | Small Gold output extracts for Power BI evidence |

---

## Final Submission Templates

| Template file | Purpose |
|---|---|
| `final_submission/final_report.md` | Final project report |
| `final_submission/final_demo_script.md` | Demo speaking flow |
| `final_submission/team_contribution.md` | Student-wise ownership and contribution |
| `final_submission/final_submission_checklist.md` | Final readiness checklist |
