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
| New-repository GitHub bootstrap guidance and helper | Implemented | — | Pending merge | `scripts/bootstrap_github.sh`, `scripts/BootstrapGitHub.ps1`, updated template docs, and repository diff review | `README.md`, `docs/bootstrap/new-repository-checklist.md`, `.github/copilot-instructions.md` | Unreleased | 2026-05-24 |
| Autonomous mode | Implemented | — | Pending | `AGENTS.md §Autonomous Mode`, `auto-merge.yml`, `.github/AUTONOMOUS_MODE` marker | `AGENTS.md`, `CURRENT.md` | Unreleased | 2026-05-24 |
| Autopilot doctrine | Implemented | — | Pending | `AGENTS.md §Autopilot Doctrine`, `copilot-instructions.md` | `AGENTS.md` | Unreleased | 2026-05-24 |
| Issue artifact rules | Implemented | — | Pending | `AGENTS.md §Issue Artifact Rules`, `docs/research/`, `docs/design/` | `AGENTS.md` | Unreleased | 2026-05-24 |
| Design issue type | Implemented | — | Pending | `labels.yml`, `.github/ISSUE_TEMPLATE/design.yml`, `label-check.yml` | `AGENTS.md §Label Rules` | Unreleased | 2026-05-24 |
| Question issue handling | Implemented | #12 | Pending | `.github/ISSUE_TEMPLATE/question.yml`, `.github/workflows/question-handling.yml`, `scripts/question_batch.sh`, `scripts/QuestionBatch.ps1`, `label-check.yml` | `AGENTS.md §Question`, `.agentic/skills.yml`, `.agentic/extensions.yml` | Unreleased | 2026-05-24 |
| PR issue-link check | Implemented | — | Pending | `.github/workflows/pr-issue-link-check.yml` | `AGENTS.md §Prohibited Actions`, `PULL_REQUEST_TEMPLATE.md` | Unreleased | 2026-05-24 |
| Upstream template synchronization guidance | Implemented | — | Pending | `AGENTS.md §Upstream PLATE Template Synchronization`, `.agentic/skills.yml template-sync`, `README.md §Keeping Your Fork Current` | `AGENTS.md`, `.agentic/skills.yml`, `README.md` | Unreleased | 2026-05-25 |
| Workflow consolidation — CI label gate + question-handling cleanup | Implemented | #24 | #25 | `ci.yml` is the single PR label gate with repair comments; `label-check.yml` is issues-only; `question-handling.yml` is issue_comment-only | `AGENTS.md §Label Rules`, `copilot-instructions.md` | Unreleased | 2026-05-25 |
| Auto-address PR feedback from third-party agents | Implemented | #22 | #30 | `plates-address-pr-feedback.yml` fires on `pull_request_review` and `pull_request_review_comment`; posts `@copilot` invocation comment for known agent reviewers via `COPILOT_TRIGGER_PAT` (human PAT) for correct routing; concurrency-safe; instructs Copilot to apply suggestions, resolve threads, and escalate human-judgment items | `AGENTS.md §Third-Party Agent Feedback`, `copilot-instructions.md`, `.agentic/skills.yml` | Unreleased | 2026-05-25 |
| Custom agent packaging | Implemented | #23 | Pending | `.github/agents/plate-configurator.agent.md`, `.agentic/extensions.yml`, `.agentic/skills.yml`, `docs/research/custom-agent-packaging.md` | `docs/research/custom-agent-packaging.md` | Unreleased | 2026-05-25 |

## Operational Behavior

| Area | Current Behavior | Evidence | Open Risk |
|---|---|---|---|
| Repository bootstrap | Generated repositories now have documented and scriptable guidance for syncing labels, updating CODEOWNERS, initializing the wiki, enabling delete-branch-on-merge, and applying baseline branch protection. Wiki initialization is opt-in. Auth tokens are not embedded in clone URLs to avoid credential leakage on failure. Temp-file cleanup handles both label-file and wiki-dir resources. Label lookups use fixed-string comparison (awk) to handle names containing regex metacharacters. PowerShell wiki clone checks `$LASTEXITCODE` to fail fast when the wiki is not enabled. | `scripts/bootstrap_github.sh`, `scripts/BootstrapGitHub.ps1`, `docs/bootstrap/new-repository-checklist.md`, `README.md` | Human decisions are still required for final branch protection policy, project fields, and real epic labels. |
| Issue typing | Issues are expected to carry exactly one PLATE issue type label (`Bug`, `Feature`, `Epic`, `Research`, `Design`, `Question`, `Audit`, `Migration`). Feature/Epic issues require exactly one `Epic: short-name`; Question issues do not. | `.github/workflows/label-check.yml`, `.github/ISSUE_TEMPLATE/question.yml` | Requires labels to be applied in each new repository. |
| Question batching and answer sync | `/question-batch` comments provide batched open-question triage, and PRs that close Question issues must update `AGENTS.md` and `.agentic/skills.yml`. | `.github/workflows/question-handling.yml`, `scripts/question_batch.sh`, `scripts/QuestionBatch.ps1` | Depends on maintainers using question type labels consistently. |
| Upstream template sync behavior | Downstream repositories can import upstream process updates by syncing only `PLATES-CORE` sections instead of replacing heavily customized files. | `AGENTS.md §Upstream PLATE Template Synchronization`, `.agentic/skills.yml`, `README.md §Keeping Your Fork Current` | Requires downstream files to preserve marker structure when customizing. |
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
| GitHub Projects fields are still documented but not automatically provisioned by the template. | TBD | Teams must still create project fields manually to align planning state with PLATE guidance. |
