# Data Dictionary

**Week:** 2  
**Purpose:** Define raw, reference, Silver, and streaming fields.

---

## 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|---|---|---|---:|---|
| `[source_file_1].csv` | One row per [entity/event] | [Purpose] | [rows] | [notes] |
| `[source_file_2].csv` | One row per [entity/event] | [Purpose] | [rows] | [notes] |
| `[reference_file].csv` | One row per [reference item] | [Purpose] | [rows] | [notes] |
| `[streaming_events].json` | One row per event | Streaming simulation | [rows] | JSON event files |

---

## 2. Raw File Schema: `[source_file_1].csv`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `source_id` | string | Yes | `SRC-0001` | Unique source record ID |
| `[field_name]` | string | Yes/No | `[example]` | [description] |

---

## 3. Raw File Schema: `[source_file_2].csv`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `source_id` | string | Yes | `SRC2-0001` | Unique source record ID |

---

## 4. Reference File Schema

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `reference_id` | string | Yes | `REF-001` | Reference key |

---

## 5. Canonical Silver Table Design

Final Silver table name:

```text
silver_[project_specific_table_name]
```

| Silver Field | Data Type | Source Mapping | Business Meaning |
|---|---|---|---|
| `record_id` | string | `[source field]` | Canonical record ID |
| `event_date` | date | `[source field]` | Date used for analytics |
| `[silver_field]` | [type] | [mapping] | [meaning] |

---

## 6. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `event_id` | string | Yes | `EVT-0001` | Unique event ID |
| `event_timestamp` | timestamp | Yes | `2026-07-03T10:15:00+05:30` | Event time |
| `event_type` | string | Yes | `[event type]` | Event category |
