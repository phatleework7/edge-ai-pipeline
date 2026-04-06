#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build"
DEVICE_DIR="$ROOT_DIR/device"
VERSIONS_DIR="$DEVICE_DIR/versions"
CURRENT_DIR="$DEVICE_DIR/current"

mkdir -p "$VERSIONS_DIR" "$CURRENT_DIR"

if [ ! -f "$BUILD_DIR/model.optimized.json" ]; then
  echo "optimized model not found. run python3 src/optimize.py first"
  exit 1
fi

VERSION="$(python3 - <<'PY'
import json
from pathlib import Path
model = json.loads(Path("build/model.optimized.json").read_text())
print(model.get("version", "unknown"))
PY
)"

cp "$BUILD_DIR/model.optimized.json" "$VERSIONS_DIR/$VERSION.json"
cp "$BUILD_DIR/model.optimized.json" "$CURRENT_DIR/model.json"
echo "$VERSION" > "$CURRENT_DIR/version.txt"
echo "deployed version $VERSION"
