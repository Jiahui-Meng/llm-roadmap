#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: scripts/start_day.sh <day-number> <slug>"
  echo "Example: scripts/start_day.sh 02 embeddings"
  exit 1
fi

DAY_NUM="$1"
SLUG="$2"
NOTES_DIR="notes"
TARGET_FILE="$NOTES_DIR/day${DAY_NUM}_${SLUG}.md"
TEMPLATE="docs/daily-template.md"

mkdir -p "$NOTES_DIR"

if [ -f "$TARGET_FILE" ]; then
  echo "Note already exists: $TARGET_FILE"
  exit 0
fi

cp "$TEMPLATE" "$TARGET_FILE"
echo "Created: $TARGET_FILE"
