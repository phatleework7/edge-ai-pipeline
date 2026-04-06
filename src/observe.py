import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / "device" / "logs" / "predictions.jsonl"


def main():
    if not LOG_PATH.exists():
        print("no predictions yet")
        return

    rows = [json.loads(line) for line in LOG_PATH.read_text().splitlines() if line.strip()]
    avg_latency = sum(row["latency_ms"] for row in rows) / len(rows)
    per_label = {}
    for row in rows:
        per_label[row["prediction"]] = per_label.get(row["prediction"], 0) + 1

    print(json.dumps({
        "requests": len(rows),
        "avg_latency_ms": round(avg_latency, 3),
        "predictions": per_label,
    }, indent=2))


if __name__ == "__main__":
    main()
