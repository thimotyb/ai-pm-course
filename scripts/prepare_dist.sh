#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

# Publish root HTML pages (index + modules + risk forms)
cp -a "$ROOT_DIR"/*.html "$DIST_DIR"/ || true

# Publish static resources used by the pages
if [ -d "$ROOT_DIR/assets" ]; then
  cp -a "$ROOT_DIR/assets" "$DIST_DIR/assets"
fi
if [ -d "$ROOT_DIR/scripts" ]; then
  cp -a "$ROOT_DIR/scripts" "$DIST_DIR/scripts"
fi
