# Structured Streaming Design

## GridPulse – Campus Energy Command Center

**Week:** 10  
**Team:** Team 05  
**Notebook:** `notebooks/07_streaming_simulation.ipynb`

---

## 1. Purpose

Week 10 implements a controlled streaming simulation for GridPulse meter events.

The objective is to demonstrate how incoming JSON meter-reading events can be processed using Databricks Structured Streaming with:

- Explicit event schema
- Event timestamp parsing
- 15-minute watermark
- Event deduplication
- Reference validation
- Business-rule validation
- Sequence validation
- Trusted and quarantine outputs
- Checkpoint-based replay protection
- Raw payload retention for malformed/schema-drift records

This implementation uses controlled JSON file drops rather than a live Kafka broker.

---

## 2. Input Files

The streaming simulation uses two controlled JSON drops:

- `meter_reading_drop_01.json`
- `meter_reading_drop_02.json`

Input location used in Databricks:

`/Volumes/workspace/default/week10_streaming/`

The second drop intentionally contains invalid and edge-case events to demonstrate streaming data-quality controls.

---

## 3. Event Schema

The streaming event contains 15 fields:

| Field | Type |
|---|---|
| event_id | string |
| schema_version | string |
| event_ts | string |
| event_type | string |
| meter_id | string |
| building_id | string |
| tariff_plan_id | string |
| energy_kwh | double |
| active_power_kw | double |
| voltage_v | double |
| current_a | double |
| power_factor | double |
| meter_status | string |
| event_sequence_no | integer |
| producer_run_id | string |

The canonical schema is documented in:

`streaming/kafka_event_schema.json`

---

## 4. Streaming Processing Flow

```text
JSON Drop 01
     |
     v
Structured Streaming
     |
     v
Schema Parsing
     |
     v
Timestamp Parsing
     |
     v
15-Minute Watermark
     |
     v
Event ID Deduplication
     |
     v
Reference + Business Validation
     |
     +----------------------+
     |                      |
     v                      v
 TRUSTED                QUARANTINE
     |                      |
     v                      v
trusted_silver_       quarantine_
meter_events          meter_events
     |
     v
fact_meter_event_week10_final
