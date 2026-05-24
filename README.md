# PLATE Template

This is the official template repository for the Process Lifecycle Exec / Agentic Task Execution Systems (PLATES).

## Agentic Task Triggers

PLATES uses fully GitHub-native triggers for autonomous progression:

- When `#question` issues are closed → usage is logged to `.agentic/COSTS.md`
- When all blockers on a Feature/Epic are resolved → `status:ready-to-work` label is applied and agent work is automatically started.

See `.github/workflows/plates-agentic-orchestrator.yml` and `AGENTS.md` for full details.

## Quick Start

...