---
current_state_version: "0.1"
process_version: "PLATE 0.6"
last_verified_at: "2026-05-24"
last_verified_commit: "pending-merge"
---

# Current Project State

`CURRENT.md` describes what the project currently does and what evidence proves it. Agents must update this file whenever a merge changes user-visible behavior, supported workflows, operational behavior, or major technical capability.

## Implemented Features

| Feature | Status | Issue | Pull Request | Tests / Evidence | Wiki / Docs | Release | Last Verified |
|---|---|---|---|---|---|---|---|
| Template process baseline | Implemented | — | #2 | Repository files and workflow scaffolds | `README.md`, `AGENTS.md` | Unreleased | 2026-05-24 |

## Operational Behavior

| Area | Current Behavior | Evidence | Open Risk |
|---|---|---|---|
| Issue typing | Issues are expected to carry exactly one PLATE issue type label. | `.github/workflows/label-check.yml` | Requires labels to be applied in each new repository. |
| Feature documentation gate | Feature PRs must modify `CURRENT.md`. | `.github/workflows/pr-documentation-check.yml` | Requires branch protection to make the check mandatory. |
| Wiki synchronization | Disabled by default and opt-in through repository configuration. | `.github/workflows/sync-wiki-on-merge.yml` | Requires `WIKI_TOKEN` and human approval before enabling writes. |
| Autonomous mode | Disabled by default. Create `.github/AUTONOMOUS_MODE` to enable; delete it to disable. When active, agents may auto-merge eligible `risk:low` PRs labeled `auto-merge`. | `.github/workflows/auto-merge.yml`, `AGENTS.md §Autonomous Mode` | Requires `allow_auto_merge: true` and Actions write permissions (`default_workflow_permissions=write`) on the repository. |

## Known Gaps

| Gap | Tracking Issue | Notes |
|---|---|---|
| Project-specific CI commands are not defined by the generic template. | TBD | Each generated project should replace placeholder CI steps with stack-specific commands. |
| Release automation is scaffolded but not project-specific. | TBD | Release policy should be completed after deployment target selection. |
