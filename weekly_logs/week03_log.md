# Week 03 Log — Databricks Data Exploration

**Week:** 3  
**Date range:** 25 July 2026 – 31 July 2026  
**Team:** Team 05 / GridPulse  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Set up the Databricks environment for the GridPulse project, upload the project datasets to Unity Catalog Volume, explore the data using PySpark and Spark SQL, and create a Week 03 Bronze demonstration table for understanding the data pipeline.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Created Catalog, Schema and Volume | Team | Done | Databricks Workspace |
| Uploaded project source files | Team | Done | Volume Files |
| Imported Week 03 Data Exploration Notebook | Team | Done | 01_data_exploration.ipynb |
| Read datasets using PySpark | Team | Done | Notebook Output |
| Displayed DataFrames and Schemas | Team | Done | Notebook Output |
| Created Temporary SQL Views | Team | Done | SQL Queries |
| Performed basic data exploration | Team | Done | SQL Results |
| Created Bronze Demo Table | Team | Done | Notebook Output |
| Created Lineage Demo View | Team | Done | Catalog Explorer |

---

## 3. Key Decisions

- Used Databricks Unity Catalog and Volume to manage project datasets.
- Used Spark SQL as the primary language for data exploration with PySpark for reading and displaying datasets.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---------|--------|-------------|
| Understanding Unity Catalog Volume paths | Medium | Mentor guidance and Databricks documentation |
| Configuring Databricks environment correctly | Medium | Practice with Databricks workspace |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/01_data_exploration.ipynb`
- Added Week 03 execution screenshots
- Updated `weekly_logs/week03_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | AI helped explain Databricks concepts, PySpark syntax, Spark SQL queries, and notebook structure. |
| What we changed after AI suggestion | We modified the notebook to match the GridPulse project, dataset names, and repository requirements. |
| What we verified manually | We verified dataset uploads, notebook execution, SQL outputs, and project-specific details before updating GitHub. |
| What we can explain without AI | We can explain the Databricks workflow, source datasets, PySpark DataFrames, Spark SQL queries, Bronze demo table, and data exploration process. |

---

## 7. Next Week Preparation

- Build the complete Bronze Layer using the project datasets.
- Perform data quality validation and begin the Silver Layer implementation.
