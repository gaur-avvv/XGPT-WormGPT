#!/usr/bin/env sh
# install-skill.sh
# Install one skill file into a local skills directory.
#
# Usage:
#   sh install-skill.sh <skill-file> [target-dir]
#
# The skill file can be:
#   - a path to a .txt prompt file
#   - a path to any plain text skill file
#
# Default target: ./.skills

SKILL_FILE="$1"
TARGET_DIR="${2:-./.skills}"

if [ -z "$SKILL_FILE" ]; then
  echo "Usage: sh install-skill.sh <skill-file> [target-dir]" >&2
  exit 1
fi

if [ ! -f "$SKILL_FILE" ]; then
  echo "Skill file not found: $SKILL_FILE" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp -- "$SKILL_FILE" "$TARGET_DIR/"

echo "Installed: $(basename "$SKILL_FILE") -> $TARGET_DIR/$(basename "$SKILL_FILE")"
