# How to Use This GitHub Starter Repo

This repository is the working template for the ZENAIZ x BVRIT Hyderabad Data Engineering Internship Program.

## Simple Rule

Do not complete all files in Week 1.

Every week, your sprint sheet will tell you exactly which files to update.

---

## Week-wise Files to Update

| Week | Update these files / folders |
|---:|---|
| 1 | `README.md`, `docs/problem_charter.md`, `weekly_logs/week01_log.md` |
| 2 | `docs/data_dictionary.md`, `docs/synthetic_data_assumptions.md`, `src/generate_synthetic_data.py`, `data_sample/raw/` |
| 3 | `notebooks/01_data_exploration.ipynb`, `screenshots/week03_*`, `weekly_logs/week03_log.md` |
| 4 | `notebooks/02_bronze_ingestion.ipynb`, `screenshots/week04_*`, `weekly_logs/week04_log.md` |
| 5 | `notebooks/03_silver_transformations.ipynb`, `screenshots/week05_*`, `weekly_logs/week05_log.md` |
| 6 | `src/data_quality_rules.py`, `notebooks/04_data_quality_checks.ipynb`, `docs/data_quality_summary.md`, `weekly_logs/week06_log.md` |
| 7 | `notebooks/05_gold_aggregations.ipynb`, `docs/gold_metrics_definition.md`, `data_sample/gold_exports/`, `weekly_logs/week07_log.md` |
| 8 | `notebooks/06_powerbi_export.ipynb`, `dashboard/powerbi_dashboard.pbix`, `screenshots/week08_*`, `weekly_logs/week08_log.md` |
| 9 | `docs/dashboard_insights.md`, updated dashboard file, `screenshots/week09_*`, `weekly_logs/week09_log.md` |
| 10 | `notebooks/07_streaming_simulation.ipynb`, `streaming/structured_streaming_design.md`, `streaming/kafka_event_schema.json`, `weekly_logs/week10_log.md` |
| 11 | `docs/pipeline_walkthrough.md`, `docs/references.md`, updated `README.md`, final screenshots, `weekly_logs/week11_log.md` |
| 12 | `final_submission/final_report.md`, `final_submission/final_demo_script.md`, `final_submission/team_contribution.md`, `final_submission/final_submission_checklist.md`, `weekly_logs/week12_log.md` |

---

## Mandatory AI Transparency Note

AI can help with explanation, debugging, SQL suggestions, documentation polishing, dashboard wording, and review preparation.

But AI cannot replace student understanding.

Every weekly log must include an AI transparency note with four points:

```text
AI used for:
Team changed / corrected:
Manually verified by:
Can explain without AI:
```

A team should not submit any AI-generated work that no team member can explain during mentor review.

---

## Power BI File-Size Rule

Preferred evidence:

```text
dashboard/powerbi_dashboard.pbix
screenshots/week08_*
screenshots/week09_*
docs/dashboard_insights.md
```

If the `.pbix` file becomes too large to manage cleanly in GitHub, do not repeatedly upload heavy versions.

In that case, commit:

- final dashboard screenshots,
- dashboard insight notes,
- Gold export evidence,
- and a short note in `dashboard/README.md` explaining where the PBIX is stored for mentor review.

The dashboard must still be built from Gold outputs only.

---

## GitHub Commit Guidance

Use simple, meaningful commit messages.

Examples:

```text
init project repository
add problem charter and week 01 log
add data dictionary and synthetic assumptions
add databricks exploration notebook
build bronze ingestion notebook
add silver transformation logic
add data quality summary
add gold metrics and export files
add power bi dashboard screenshots
add streaming simulation notebook
finalize pipeline walkthrough
add final report and demo script
```

---

## Evidence Rule

If work is not visible in GitHub, screenshots, notebooks, or final outputs, it is not reviewable.

Build weekly. Commit weekly. Explain what you built.
