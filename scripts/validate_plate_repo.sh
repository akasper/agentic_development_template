#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="${1:-.}"
ROOT_DIR="$(cd "$ROOT_DIR" && pwd)"

required_files=(
    "AGENTS.md"
    "CURRENT.md"
    "SPEC.md"
    ".agentic/process.yml"
    ".agentic/skills.yml"
    ".github/copilot-instructions.md"
    ".github/workflows/ci.yml"
)

for rel in "${required_files[@]}"; do
    if [[ ! -f "$ROOT_DIR/$rel" ]]; then
        echo "Required artifact is missing: $rel"
        exit 1
    fi
done

ci_file="$ROOT_DIR/.github/workflows/ci.yml"
copilot_file="$ROOT_DIR/.github/copilot-instructions.md"
current_file="$ROOT_DIR/CURRENT.md"

has_runtime=false
for manifest in package.json pyproject.toml requirements.txt wally.toml default.project.json rojo.json; do
    if [[ -f "$ROOT_DIR/$manifest" ]]; then
        has_runtime=true
        break
    fi
done

if $has_runtime; then
    if grep -q 'echo "Tests would run here"' "$ci_file"; then
        echo "Runtime manifest detected, but CI still uses placeholder test command."
        exit 1
    fi

    if grep -qi 'does not define a local build, lint, or test toolchain yet' "$copilot_file"; then
        echo "Runtime manifest detected, but .github/copilot-instructions.md still claims no concrete toolchain."
        exit 1
    fi

    if grep -qi 'Project-specific CI commands are not defined by the generic template' "$current_file"; then
        echo "Runtime manifest detected, but CURRENT.md still records missing project-specific CI commands."
        exit 1
    fi
fi

echo "PLATE repository validation passed."
