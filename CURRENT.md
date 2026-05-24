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
| Autonomous mode | Implemented | — | Pending | `AGENTS.md §Autonomous Mode`, `auto-merge.yml`, `.github/AUTONOMOUS_MODE` marker | `AGENTS.md`, `CURRENT.md` | Unreleased | 2026-05-24 |
| Autopilot doctrine | Implemented | — | Pending | `AGENTS.md §Autopilot Doctrine`, `copilot-instructions.md` | `AGENTS.md` | Unreleased | 2026-05-24 |
| Issue artifact rules | Implemented | — | Pending | `AGENTS.md §Issue Artifact Rules`, `docs/research/`, `docs/design/` | `AGENTS.md` | Unreleased | 2026-05-24 |
| Design issue type | Implemented | — | Pending | `labels.yml`, `.github/ISSUE_TEMPLATE/design.yml`, `label-check.yml` | `AGENTS.md §Label Rules` | Unreleased | 2026-05-24 |
| PR issue-link check | Implemented | — | Pending | `.github/workflows/pr-issue-link-check.yml` | `AGENTS.md §Prohibited Actions`, `PULL_REQUEST_TEMPLATE.md` | Unreleased | 2026-05-24 |

## Operational Behavior

| Area | Current Behavior | Evidence | Open Risk |
|---|---|---|---|
| Issue typing | Issues are expected to carry exactly one PLATE issue type label (`Bug`, `Feature`, `Epic`, `Research`, `Design`, `Audit`, `Migration`). | `.github/workflows/label-check.yml` | Requires labels to be applied in each new repository. |
| Feature documentation gate | Feature PRs must modify `CURRENT.md`. | `.github/workflows/pr-documentation-check.yml` | Requires branch protection to make the check mandatory. |
| PR issue-link check | PRs that resolve issues must include a closing keyword (`Closes #N`). Feature/Bug PRs fail CI without it; other types receive a warning. PRs labeled `no-issue` are exempt. | `.github/workflows/pr-issue-link-check.yml` | Soft warning for non-Feature/Bug types; relies on agent compliance for those. |
| Issue artifact requirement | Research, Design, Audit, and Migration issues must close with a committed artifact (see `AGENTS.md §Issue Artifact Rules`). | `AGENTS.md`, `docs/research/README.md`, `docs/design/README.md` | No automated enforcement on issue close; relies on PR content review. |
| Wiki synchronization | Disabled by default and opt-in through repository configuration. | `.github/workflows/sync-wiki-on-merge.yml` | Requires `WIKI_TOKEN` and human approval before enabling writes. |
| Autonomous mode | Disabled by default. Create `.github/AUTONOMOUS_MODE` to enable; delete it to disable. When active, agents may auto-merge eligible `risk:low` PRs labeled `auto-merge`. | `.github/workflows/auto-merge.yml`, `AGENTS.md §Autonomous Mode` | Requires `allow_auto_merge: true` and Actions write permissions (`default_workflow_permissions=write`) on the repository. |

## Known Gaps

| Gap | Tracking Issue | Notes |
|---|---|---|
| Project-specific CI commands are not defined by the generic template. | TBD | Each generated project should replace placeholder CI steps with stack-specific commands. |
| Release automation is scaffolded but not project-specific. | TBD | Release policy should be completed after deployment target selection. |
