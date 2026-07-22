# Data Dictionary

**Week:** 2  
**Purpose:** Define raw, reference, Silver, and streaming fields.

---

## 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|-----------|-------|---------|--------------|------|
| consumption_readings.parquet | One row per meter reading | Stores energy consumption readings | 300000 | Main fact dataset |
| buildings.json | One row per building | Building master data | 20 | Reference data |
| meters.csv | One row per meter | Meter information | 120 | Links meters to buildings |
| tariffs.csv | One row per tariff | Tariff reference data | 9 | Electricity tariff details |
| meter_reading_drop_01.json | One row per event | Streaming simulation | 100 | JSON event file |
| meter_reading_drop_02.json | One row per event | Streaming simulation | 100 | JSON event file |


---

## 2. Raw File Schema: `[source_file_1].csv`

|------------|-----------|-----------|---------|-------------|
| reading_id | string | Yes | RD-000001 | Unique reading ID |
| meter_id | string | Yes | MTR-001 | Meter identifier |
| timestamp | timestamp | Yes | 2026-01-01T00:15:00 | Reading time |
| consumption_kwh | double | Yes | 12.45 | Energy consumed |

---

## 3. Raw File Schema: `[source_file_2].csv`

|------------|-----------|-----------|---------|-------------|
| meter_id | string | Yes | MTR-001 | Unique meter ID |
| building_id | string | Yes | BLD-01 | Building identifier |
| meter_type | string | Yes | Smart Meter | Meter category |
---

## 4. Reference File Schema

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| building_id | string | Yes | BLD-01 | Building ID |
| building_name | string | Yes | Academic Block | Building name |
---

## 5. Canonical Silver Table Design

Final Silver table name:

```text
silver_energy_consumption
```

| Silver Field | Data Type | Source Mapping | Business Meaning |
|--------------|-----------|----------------|------------------|
| reading_id | string | reading_id | Unique record |
| meter_id | string | meter_id | Meter identifier |
| building_id | string | building_id | Building identifier |
| event_date | date | timestamp | Analytics date |
| consumption_kwh | double | consumption_kwh | Energy consumed |
---

## 6. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| event_id | string | Yes | EVT-0001 | Unique event ID |
| event_timestamp | timestamp | Yes | 2026-07-03T10:15:00+05:30 | Event time |
| meter_id | string | Yes | MTR-001 | Meter identifier |
| event_type | string | Yes | meter_reading | Event category |
| reading_value | double | Yes | 15.8 | Reading value |
