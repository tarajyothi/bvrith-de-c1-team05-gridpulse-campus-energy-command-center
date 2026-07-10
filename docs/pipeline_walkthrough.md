# Pipeline Walkthrough

**Week:** 11  
**Purpose:** Explain the full end-to-end project flow.

---

## 1. Pipeline Run Order

| Step | Notebook / File | Output |
|---:|---|---|
| 1 | `src/generate_synthetic_data.py` | Raw and streaming sample data |
| 2 | `notebooks/01_data_exploration.ipynb` | Exploration and profiling evidence |
| 3 | `notebooks/02_bronze_ingestion.ipynb` | Bronze tables |
| 4 | `notebooks/03_silver_transformations.ipynb` | Silver tables |
| 5 | `notebooks/04_data_quality_checks.ipynb` | DQ rule results |
| 6 | `notebooks/05_gold_aggregations.ipynb` | Gold metric tables |
| 7 | `notebooks/06_powerbi_export.ipynb` | Gold exports for Power BI |
| 8 | `notebooks/07_streaming_simulation.ipynb` | Streaming Bronze and live metric |

---

## 2. Architecture Explanation

Write 8–12 lines explaining the full flow:

Raw Sources → Bronze → Silver → Data Quality → Gold → Power BI → Streaming Simulation

---

## 3. Known Limitations

List honest limitations.

- [Limitation]
- [Limitation]

---

## 4. How to Reproduce

Write the steps a mentor should follow to review or reproduce the project.

1. Clone / open repository.
2. Review README and data assumptions.
3. Upload or generate data.
4. Run notebooks in sequence.
5. Review outputs and screenshots.
6. Open Power BI dashboard.
7. Review streaming simulation evidence.
