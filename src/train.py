import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "train.csv"
BUILD_DIR = ROOT / "build"
MODEL_PATH = BUILD_DIR / "model.json"


def train_centroid_model(rows):
    grouped = defaultdict(list)
    for x, y, label in rows:
        grouped[label].append((float(x), float(y)))

    centroids = {}
    for label, points in grouped.items():
        avg_x = sum(point[0] for point in points) / len(points)
        avg_y = sum(point[1] for point in points) / len(points)
        centroids[label] = {"x": avg_x, "y": avg_y}

    return {
        "model_type": "centroid_classifier",
        "version": "v1",
        "classes": sorted(centroids.keys()),
        "centroids": centroids,
    }


def load_rows(path):
    with path.open() as handle:
        reader = csv.DictReader(handle)
        return [(row["x"], row["y"], row["label"]) for row in reader]


def main():
    rows = load_rows(DATA_PATH)
    model = train_centroid_model(rows)
    BUILD_DIR.mkdir(exist_ok=True)
    MODEL_PATH.write_text(json.dumps(model, indent=2))
    print(f"trained model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
