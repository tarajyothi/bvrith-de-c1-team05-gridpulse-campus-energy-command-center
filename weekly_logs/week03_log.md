# Week 03 Log — Databricks Data Exploration

**Week:** 3  
**Date range:** 25 July 2026 – 31 July 2026  
**Team:** Team 05 / GridPulse  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Set up the Databricks environment for the GridPulse project, access the project datasets from the Unity Catalog Volume, and explore the sample datasets using PySpark and Spark SQL.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Created Catalog, Schema and Volume | Team | Done | Databricks Workspace |
| Uploaded/accessed project sample files | Team | Done | Unity Catalog Volume |
| Imported Week 03 Data Exploration Notebook | Team | Done | `01_data_exploration.ipynb` |
| Read meter dataset using PySpark | Team | Done | Notebook Output |
| Read building dataset using PySpark | Team | Done | Notebook Output |
| Read consumption dataset using PySpark | Team | Done | Notebook Output |
| Displayed DataFrames and inspected schemas | Team | Done | Notebook Output |
| Created temporary SQL views | Team | Done | Notebook |
| Performed basic data exploration | Team | Done | Notebook Output |
| Checked NULL values | Team | Done | All checked consumption columns returned 0 NULLs |
| Checked negative energy readings | Team | Done | 0 negative readings found |
| Checked future timestamps | Team | Done | 0 future readings found |
| Checked missing meter IDs | Team | Done | 0 missing meter references found |

---

## 3. Dataset Exploration Results

The sample datasets were successfully loaded into Databricks.

| Dataset | Records |
|---------|---------|
| Meters | 20 |
| Buildings | 5 |
| Consumption Readings | 500 |

The schemas and available fields were inspected for all three datasets.

---

## 4. Data Quality Signals Observed

The following initial checks were performed on the consumption sample:

- NULL values: 0
- Negative energy readings: 0
- Future timestamps: 0
- Consumption records with missing meter IDs: 0

The sample used for Week 03 did not show these defects. No artificial defects were added to the dataset.

---

## 5. Technical Issues Resolved

### Parquet Timestamp Compatibility

The consumption Parquet file initially produced a timestamp compatibility error in Spark because of the timestamp precision used in the source file.

The data was read using pandas and the timestamp columns were converted to microsecond precision before creating the Spark DataFrame.

### Multi-line JSON

The buildings JSON file contained multi-line JSON content. Spark JSON reading was configured with the `multiLine` option to successfully load the dataset.

---

## 6. Key Decisions

- Used Databricks Unity Catalog Volume for project sample data.
- Used PySpark for dataset loading and exploration.
- Used Spark SQL temporary views for SQL-based exploration.
- Kept the sample data unchanged and reported the actual quality-check results.

---

## 7. Blockers / Risks

| Issue | Impact | Resolution |
|------|--------|------------|
| Parquet timestamp precision compatibility | Medium | Converted timestamp precision before creating Spark DataFrame |
| Multi-line JSON format | Low | Enabled multi-line JSON reading |
| Understanding Unity Catalog Volume paths | Medium | Practiced using the Volume path in Databricks |

---

## 8. Evidence Added to GitHub

- Updated `notebooks/01_data_exploration.ipynb`
- Updated `weekly_logs/week03_log.md`

Only completed and verified Week 03 work is documented.

---

## 9. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | AI helped explain Databricks concepts, PySpark syntax, Spark SQL queries, and troubleshooting steps. |
| What we changed after AI suggestion | We adapted the suggested code and troubleshooting steps to the GridPulse datasets and Databricks environment. |
| What we verified manually | We verified dataset loading, record counts, schemas, temporary views, and data-quality query results in Databricks. |
| What we can explain without AI | We can explain the basic Databricks workflow, Unity Catalog Volume paths, Spark DataFrames, temporary SQL views, and the Week 03 exploration checks. |

---

## 10. Next Week Preparation

- Begin Week 04 Bronze Layer ingestion.
- Organize the raw/sample datasets for Bronze processing.
- Preserve source data without silently deleting records.
