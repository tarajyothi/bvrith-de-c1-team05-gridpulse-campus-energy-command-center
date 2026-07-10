# Project Requirements

**Week:** 1  
**Purpose:** Define what the project must produce.

---

## 1. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Ingest raw source files into Bronze tables | Must have |
| FR-02 | Create standardized Silver table(s) | Must have |
| FR-03 | Implement data quality rules | Must have |
| FR-04 | Create Gold metric tables | Must have |
| FR-05 | Build Power BI dashboard from Gold outputs | Must have |
| FR-06 | Simulate streaming JSON events | Must have |

---

## 2. Data Requirements

| ID | Requirement |
|---|---|
| DR-01 | Raw files must have realistic fields and keys |
| DR-02 | Synthetic data assumptions must be documented |
| DR-03 | Data quality defects should be intentionally included |
| DR-04 | Sample data kept in GitHub must remain small |

---

## 3. Dashboard Requirements

| ID | Requirement |
|---|---|
| BI-01 | Dashboard must use Gold outputs only |
| BI-02 | Dashboard should include KPI cards, trends, comparisons and filters |
| BI-03 | Dashboard insights must be documented in `docs/dashboard_insights.md` |

---

## 4. Evidence Requirements

| ID | Requirement |
|---|---|
| EV-01 | Weekly logs must be committed |
| EV-02 | Screenshots must be saved in `screenshots/` |
| EV-03 | External references must be listed in `docs/references.md` |
| EV-04 | AI usage must be disclosed in weekly logs |
