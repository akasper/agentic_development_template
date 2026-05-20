# AGENTS.md – Agent Constitution

This repository follows the GitHub Agentic Operating System (GHAOS). Agents may perform substantial work, but they must operate inside the authority boundaries and evidence requirements below.

## Repository Context

| Field | Value |
|---|---|
| Project | agentic_development_template |
| Process version | 0.4.0 |
| Human owner | akasper |
| Primary branch | main |
| Wiki | https://github.com/akasper/agentic_development_template/wiki |
| Project board | https://github.com/akasper/agentic_development_template/projects |

## Non-Negotiables

1. Never merge to `main`. Humans merge.
2. Begin behavior-changing work with failing tests.
3. Work from a GitHub issue unless the change is a trivial documentation correction.
4. Open a draft pull request early.
5. Keep changes small, reviewable, and tied to one issue whenever practical.
6. Update `CURRENT.md` when implemented behavior changes.
7. Update the Wiki when human-facing behavior, usage, or operations change.
8. Link tests, recordings, issues, pull requests, wiki pages, ADRs, and releases wherever applicable.
9. Escalate uncertainty, security concerns, destructive operations, credentials, user data, and product decisions to a human.

## Default Work Loop

When assigned a ready issue, create a branch, open a draft pull request, add failing tests, implement the change, run checks, update documentation, self-review, and request review. Respond to review feedback autonomously when the requested changes are within scope.

## Branch Naming

Use `feature/issue-N-short-description`, `bugfix/issue-N-short-description`, `docs/issue-N-short-description`, `audit/issue-N-short-description`, or `refactor/issue-N-short-description`.

## Testing Expectations

Behavior changes require tests. Bug fixes require a failing regression test before the fix. User-visible workflows require E2E coverage and recording where practical. If a test cannot be added, explain why in the pull request and request human approval.

## Documentation Expectations

Update `CURRENT.md` for implemented behavior. Update the Wiki for human-facing behavior, operations, examples, screenshots, recordings, and feature explanations. Update ADRs when decisions are made or superseded.

## Allowed Actions

Agents may create branches, open draft pull requests, edit code, add tests, update documentation, draft issues, draft ADRs, run local checks, review their own work, and respond to review feedback.

## Restricted Actions

Agents must request human approval before changing process configuration, modifying CI gates, changing dependencies with high risk, performing data migrations, changing security-sensitive code, altering deployment infrastructure, or deleting durable evidence.

## Prohibited Actions

Agents must not merge to `main`, disable required checks, alter branch protection, change secrets, approve security exceptions, delete audit evidence, or make major product decisions without human approval.

## Escalation Triggers

Escalate when requirements are unclear, acceptance criteria conflict, tests cannot be made reliable, security or privacy risk is discovered, user data may be affected, destructive operations are required, costs may materially increase, or a decision changes the project direction.

## Project-Specific Overrides

| Rule | Override | Approver | Scope | Review Date | ADR |
|---|---|---|---|---|---|
| RULE | OVERRIDE | HUMAN | SCOPE | YYYY-MM-DD | ADR_LINK |