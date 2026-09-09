#!/usr/bin/env sh
# list-skills.sh
# List every .txt file in the repository as a skill.
#
# Usage:
#   sh list-skills.sh
#
# Only .txt files anywhere in the repository are listed.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

found=0
find "$REPO_ROOT" -type f -name '*.txt' | while IFS= read -r file; do
  cleaned_name="$(basename "$file")"
  echo "$cleaned_name"
  found=1
done

if [ "$found" -eq 0 ]; then
  echo "No .txt files found in $REPO_ROOT" >&2
fi
