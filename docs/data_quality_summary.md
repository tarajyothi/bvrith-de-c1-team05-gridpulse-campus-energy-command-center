# Data Quality Summary

**Week:** 6  
**Purpose:** Summarize data quality rules, failures and business impact.

---

## 1. Quality Rule Results

| Rule ID | Rule Name | Severity | Passed Count | Failed Count | Business Impact |
|---|---|---|---:|---:|---|
| DQ-01 | Required ID not null | High | [count] | [count] | Records without IDs cannot be trusted |
| DQ-02 | Duplicate key check | High | [count] | [count] | Duplicate keys distort metrics |
| DQ-03 | Valid reference key | Medium | [count] | [count] | Invalid references affect joins |
| DQ-04 | Valid timestamp order | Medium | [count] | [count] | Time-based metrics may be wrong |

---

## 2. Failed Record Examples

| Rule ID | Sample Record ID | Failure Reason | Action / Handling |
|---|---|---|---|
| DQ-01 | `[id]` | `[reason]` | `[action]` |

---

## 3. What Should Block Gold Metrics?

List rules that should block or flag Gold table generation.

- [Rule and reason]
- [Rule and reason]

---

## 4. Quality Summary

Write 5–8 lines explaining the overall health of the dataset.

Prompts:

- Which rule failed the most?
- Which failures matter most for dashboards?
- Did the team fix, flag, or exclude bad records?
- What should the mentor review carefully?
