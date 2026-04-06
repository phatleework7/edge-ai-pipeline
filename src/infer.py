import argparse
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEVICE_DIR = ROOT / "device"
ACTIVE_MODEL_PATH = DEVICE_DIR / "current" / "model.json"
LOG_PATH = DEVICE_DIR / "logs" / "predictions.jsonl"


def load_model():
    return json.loads(ACTIVE_MODEL_PATH.read_text())


def predict(model, x, y):
    best_label = None
    best_distance = None
    for label, centroid in model["centroids"].items():
        distance = math.dist((x, y), (centroid["x"], centroid["y"]))
        if best_distance is None or distance < best_distance:
            best_label = label
            best_distance = distance
    return best_label, best_distance


def write_log(x, y, label, distance, latency_ms):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "x": x,
        "y": y,
        "prediction": label,
        "distance": round(distance, 4),
        "latency_ms": round(latency_ms, 3),
    }
    with LOG_PATH.open("a") as handle:
        handle.write(json.dumps(event) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, required=True)
    parser.add_argument("--y", type=float, required=True)
    args = parser.parse_args()

    model = load_model()
    started = time.perf_counter()
    label, distance = predict(model, args.x, args.y)
    latency_ms = (time.perf_counter() - started) * 1000
    write_log(args.x, args.y, label, distance, latency_ms)
    print(json.dumps({"prediction": label, "distance": round(distance, 4)}))


if __name__ == "__main__":
    main()
