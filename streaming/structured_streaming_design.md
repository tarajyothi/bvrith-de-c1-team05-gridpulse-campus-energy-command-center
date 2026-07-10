# Structured Streaming Design

**Week:** 10  
**Purpose:** Explain the streaming simulation.

---

## 1. Streaming Scenario

Describe the event flow.

Example:

> New JSON event files arrive in a streaming input path. Databricks Auto Loader detects the files, Structured Streaming processes them, and the output is written to a Streaming Bronze table.

---

## 2. Event Source

| Item | Description |
|---|---|
| Event file format | JSON |
| Input path | `/Volumes/workspace/default/<project_name>/streaming_input/` |
| Processing method | Auto Loader / Structured Streaming |
| Output table | `bronze_streaming_events` |
| Checkpoint path | `/Volumes/workspace/default/<project_name>/checkpoints/...` |

---

## 3. Near-Real-Time Metric

Define one simple live metric.

Example:

| Metric | Formula | Use |
|---|---|---|
| Event count by severity | Count events grouped by severity | Shows alert pressure |

---

## 4. Limitations

- This is a student streaming simulation, not a production event platform.
- Kafka is documented as production architecture awareness only.
- Streaming events are synthetic and educational.
