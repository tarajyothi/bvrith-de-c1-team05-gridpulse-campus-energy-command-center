# Gold Metrics Definition

**Week:** 7  
**Purpose:** Define dashboard-ready Gold tables and KPI formulas.

---

## 1. Gold Table Catalog

| Gold Table Name | Grain | Source Table(s) | Purpose |
|---|---|---|---|
| `gold_[metric_table_1]` | One row per [grain] | `silver_[table]` | [purpose] |
| `gold_[metric_table_2]` | One row per [grain] | `silver_[table]` | [purpose] |

---

## 2. KPI Definitions

| KPI Name | Formula | Grain | Dashboard Page | Notes |
|---|---|---|---|---|
| `[KPI 1]` | `[formula]` | `[daily / weekly / category]` | `[page]` | `[notes]` |
| `[KPI 2]` | `[formula]` | `[grain]` | `[page]` | `[notes]` |

---

## 3. Validation Checks

Before using Gold tables in Power BI, verify:

- Gold row counts are reasonable.
- No unexpected nulls exist in key dashboard fields.
- KPI totals match manual spot checks.
- Power BI connects to Gold outputs only.
- Metric definitions are documented clearly.
