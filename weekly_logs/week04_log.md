# Week 04 Log — Bronze Ingestion

**Week:** 4  
**Date range:** 28-07-2026 to 03-08-2026  
**Team:** Team 5  
**Project:** GridPulse – Campus Energy Command Center

---

## 1. Sprint Goal

Ingest the GridPulse source datasets into Databricks Bronze tables while preserving the source data structure and adding ingestion metadata.

The goal was to verify that the source records were loaded correctly and that the Bronze tables were ready for downstream Silver transformations.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created Week 4 Bronze ingestion notebook | Team 5 | Done | `notebooks/02_bronze_ingestion.ipynb` |
| Loaded meters source data | Team 5 | Done | `workspace.gridpulse_bronze.meters_bronze` |
| Loaded buildings source data | Team 5 | Done | `workspace.gridpulse_bronze.buildings_bronze` |
| Loaded consumption source data | Team 5 | Done | `workspace.gridpulse_bronze.consumption_bronze` |
| Added ingestion timestamp metadata | Team 5 | Done | Bronze tables |
| Added source file metadata | Team 5 | Done | Bronze tables |
| Verified source-to-Bronze row counts | Team 5 | Done | `screenshots/week04_bronze_counts.png` |
| Verified Bronze metadata | Team 5 | Done | `screenshots/week04_bronze_table_created.png` |

---

## 3. Key Decisions

- Created a dedicated `workspace.gridpulse_bronze` schema for Bronze-layer tables.
- Preserved the source records while adding `_ingestion_timestamp` and `_source_file` metadata.
- Verified that the Bronze row counts matched the loaded source datasets.
- Used a pandas-based Parquet loading workaround for the consumption sample because the original Parquet timestamp type was not directly supported by the Spark reader.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Spark Parquet reader could not directly read the `TIMESTAMP(NANOS,false)` timestamp type in the consumption sample | Direct Spark ingestion of the sample Parquet file failed | Used pandas to read the Parquet file, converted the timestamp precision, and then created the Spark DataFrame |

---

## 5. Evidence Added to GitHub

- `notebooks/02_bronze_ingestion.ipynb`
- `screenshots/week04_bronze_counts.png`
- `screenshots/week04_bronze_table_created.png`
- `weekly_logs/week04_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the Bronze ingestion workflow and troubleshoot the Parquet timestamp compatibility issue. |
| What we changed after AI suggestion | The consumption Parquet loading approach was adapted to the actual Databricks Spark error by using pandas and converting the timestamp precision before creating the Spark DataFrame. |
| What we verified manually | Bronze table creation, row counts, ingestion metadata, source file metadata, and the loaded datasets were executed and verified in Databricks. |
| What we can explain without AI | We can explain the Bronze layer purpose, the source-to-Bronze ingestion process, the metadata columns, the row-count reconciliation, and why the Parquet workaround was required. |

---

## 7. Next Week Preparation

- Use the Bronze tables as the source for Week 5 Silver transformations.
- Standardize field names and data types.
- Create Silver tables for meters, buildings, and consumption data.
