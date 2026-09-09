#!/usr/bin/env sh
# install-all-skills.sh
# Install every .txt file in the repository as a skill.
#
# Usage:
#   sh install-all-skills.sh [target-dir]
#
# Default target: ./.skills
# Only .txt files anywhere in the repository are installed as skills.
# Non-.txt files are ignored.

TARGET_DIR="${1:-./.skills}"

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$TARGET_DIR"

copied=0
find "$REPO_ROOT" -type f -name '*.txt' | while IFS= read -r file; do
  cleaned_name="$(basename "$file")"
  cp -- "$file" "$TARGET_DIR/$cleaned_name"
  copied=$((copied + 1))
done

if [ "$copied" -eq 0 ]; then
  echo "No .txt files found in $REPO_ROOT" >&2
else
  echo "Installed $copied skill file(s) into $TARGET_DIR/"
fi
