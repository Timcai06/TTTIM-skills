#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$ROOT_DIR/skills"

TARGETS=(
  "$HOME/.agents/skills"
  "$HOME/.gemini/config/skills"
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
)

for skill_path in "$SKILLS_DIR"/*; do
  [ -d "$skill_path" ] || continue
  [ -f "$skill_path/SKILL.md" ] || continue
  skill_name="$(basename "$skill_path")"
  for dir in "${TARGETS[@]}"; do
    mkdir -p "$dir"
    ln -sfn "$skill_path" "$dir/$skill_name"
    echo "Linked: $dir/$skill_name -> $skill_path"
  done
done
