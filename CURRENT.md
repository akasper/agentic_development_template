---
current_state_version: "0.2"
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
| New-repository GitHub bootstrap guidance and helper | Implemented | — | Pending merge | `scripts/bootstrap_github.py`, updated template docs, and repository diff review | `README.md`, `docs/bootstrap/new-repository-checklist.md`, `.github/copilot-instructions.md` | Unreleased | 2026-05-24 |

## Operational Behavior

| Area | Current Behavior | Evidence | Open Risk |
|---|---|---|---|
| Repository bootstrap | Generated repositories now have documented and scriptable guidance for syncing labels, updating CODEOWNERS, initializing the wiki, enabling delete-branch-on-merge, and applying baseline branch protection. | `scripts/bootstrap_github.py`, `docs/bootstrap/new-repository-checklist.md`, `README.md` | Human decisions are still required for final branch protection policy, project fields, and real epic labels. |
| Issue typing | Issues are expected to carry exactly one PLATE issue type label. | `.github/workflows/label-check.yml` | Requires labels to be applied in each new repository. |
| Feature documentation gate | Feature PRs must modify `CURRENT.md`. | `.github/workflows/pr-documentation-check.yml` | Requires branch protection to make the check mandatory. |
| Wiki synchronization | Disabled by default and opt-in through repository configuration. | `.github/workflows/sync-wiki-on-merge.yml` | Requires `WIKI_TOKEN` and human approval before enabling writes. |

## Known Gaps

| Gap | Tracking Issue | Notes |
|---|---|---|
| Project-specific CI commands are not defined by the generic template. | TBD | Each generated project should replace placeholder CI steps with stack-specific commands. |
| Release automation is scaffolded but not project-specific. | TBD | Release policy should be completed after deployment target selection. |
| GitHub Projects fields are still documented but not automatically provisioned by the template. | TBD | Teams must still create project fields manually to align planning state with PLATE guidance. |
