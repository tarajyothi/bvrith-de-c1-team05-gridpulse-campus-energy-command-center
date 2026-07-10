"""
Synthetic Data Generator Template

Week: 2
Purpose:
    Generate small educational CSV/JSON sample datasets for the assigned project.

Important:
    - Do not generate or use real personal/company/customer data.
    - Keep GitHub sample files small.
    - Use a fixed random seed so data can be recreated.
    - Update this file based on your project-specific manual.
"""

from pathlib import Path
import csv
import json
import random
from datetime import datetime, timedelta

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data_sample" / "raw"
STREAMING_DIR = BASE_DIR / "data_sample" / "streaming"

RAW_DIR.mkdir(parents=True, exist_ok=True)
STREAMING_DIR.mkdir(parents=True, exist_ok=True)


def generate_reference_file() -> None:
    """Create a small reference file. Replace fields with project-specific values."""
    output_path = RAW_DIR / "reference_master.csv"
    rows = [
        {"reference_id": "REF-001", "reference_name": "Sample A", "category": "Category 1"},
        {"reference_id": "REF-002", "reference_name": "Sample B", "category": "Category 2"},
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def generate_source_file(row_count: int = 100) -> None:
    """Create a simple raw source file. Replace fields based on assigned project."""
    output_path = RAW_DIR / "source_events_raw.csv"
    start_time = datetime(2026, 7, 3, 9, 0, 0)

    fieldnames = ["source_record_id", "reference_id", "event_timestamp", "event_type", "amount", "status"]
    statuses = ["completed", "pending", "cancelled"]
    event_types = ["type_a", "type_b", "type_c"]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, row_count + 1):
            ts = start_time + timedelta(minutes=random.randint(0, 3000))
            writer.writerow({
                "source_record_id": f"SRC-{i:06d}",
                "reference_id": random.choice(["REF-001", "REF-002", "REF-999"]),  # REF-999 is intentional defect
                "event_timestamp": ts.isoformat(),
                "event_type": random.choice(event_types),
                "amount": round(random.uniform(10, 500), 2),
                "status": random.choice(statuses),
            })


def generate_streaming_events(batch_number: int = 1, event_count: int = 25) -> None:
    """Create JSON lines file for streaming simulation."""
    output_path = STREAMING_DIR / f"stream_events_batch_{batch_number:03d}.json"
    start_time = datetime(2026, 7, 3, 18, 0, 0)

    with output_path.open("w", encoding="utf-8") as f:
        for i in range(1, event_count + 1):
            event = {
                "event_id": f"EVT-{batch_number:03d}-{i:05d}",
                "event_timestamp": (start_time + timedelta(seconds=i * 30)).isoformat(),
                "event_type": random.choice(["alert", "update", "transaction"]),
                "entity_id": f"ENT-{random.randint(1, 50):04d}",
                "severity": random.choice(["low", "medium", "high"]),
            }
            f.write(json.dumps(event) + "\n")


def main() -> None:
    generate_reference_file()
    generate_source_file(row_count=100)
    generate_streaming_events(batch_number=1, event_count=25)
    print("Synthetic sample data generated successfully.")


if __name__ == "__main__":
    main()
