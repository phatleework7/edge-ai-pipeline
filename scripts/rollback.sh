#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DEVICE_DIR="$ROOT_DIR/device"
VERSIONS_DIR="$DEVICE_DIR/versions"
CURRENT_DIR="$DEVICE_DIR/current"

CURRENT_VERSION="$(cat "$CURRENT_DIR/version.txt")"
PREVIOUS_VERSION="$(ls "$VERSIONS_DIR" | sed 's/.json$//' | grep -v "^$CURRENT_VERSION$" | sort | tail -n 1 || true)"

if [ -z "$PREVIOUS_VERSION" ]; then
  echo "no previous version to rollback"
  exit 1
fi

cp "$VERSIONS_DIR/$PREVIOUS_VERSION.json" "$CURRENT_DIR/model.json"
echo "$PREVIOUS_VERSION" > "$CURRENT_DIR/version.txt"
echo "rolled back to $PREVIOUS_VERSION"
