#!/usr/bin/env sh
# install.sh
# Install all skill .txt files from the skills directory into a local skills directory.
#
# Usage:
#   sh install.sh [target-dir]
#
# Default target: ./.skills
# Only .txt files in the skills directory are installed.

TARGET_DIR="${1:-./.skills}"

SKILLS_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "Skills directory not found: $SKILLS_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

copied=0
for file in "$SKILLS_DIR"/*.txt; do
  if [ -f "$file" ]; then
    cleaned_name="$(basename "$file")"
    cp -- "$file" "$TARGET_DIR/$cleaned_name"
    copied=$((copied + 1))
  fi
done

if [ "$copied" -eq 0 ]; then
  echo "No .txt skill files found in $SKILLS_DIR" >&2
  exit 1
fi

echo "Installed $copied skill file(s) into $TARGET_DIR/"
