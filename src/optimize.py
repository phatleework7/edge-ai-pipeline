import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "build"
MODEL_PATH = BUILD_DIR / "model.json"
OPTIMIZED_PATH = BUILD_DIR / "model.optimized.json"


def optimize(model):
    optimized = dict(model)
    optimized["deployment_target"] = "edge-device"
    optimized["optimized"] = True
    optimized["runtime"] = "python-simulated"
    return optimized


def main():
    model = json.loads(MODEL_PATH.read_text())
    optimized = optimize(model)
    OPTIMIZED_PATH.write_text(json.dumps(optimized, indent=2))
    print(f"optimized model saved to {OPTIMIZED_PATH}")


if __name__ == "__main__":
    main()
