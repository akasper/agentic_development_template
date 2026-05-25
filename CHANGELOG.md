# Changelog

All notable changes to this project should be recorded here. Each release entry should link issues, pull requests, tests, documentation updates, wiki pages, migration notes, and audit findings where applicable.

## Unreleased

| Type | Change | Issue | PR | Evidence |
|---|---|---|---|---|
| Process | Establish PLATE template artifact baseline. | — | #2 | Repository files, labels, templates, and workflow scaffolds. |
| Process | Add GitHub bootstrap guidance and automation based on recent repository setup lessons, including atomic PR labeling guidance for agents. | — | Pending merge | `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `.github/copilot-instructions.md`, `docs/bootstrap/new-repository-checklist.md`, `scripts/bootstrap_github.sh`, `scripts/BootstrapGitHub.ps1`. |
| Feature | Add autonomous mode: `AGENTS.md §Autonomous Mode`, `auto-merge` label, `auto-merge.yml` workflow with marker-file gate, updated `copilot-instructions.md` and `CURRENT.md`. Mode is off by default; toggle via `.github/AUTONOMOUS_MODE`. | — | Pending merge | `AGENTS.md`, `.github/labels.yml`, `.github/workflows/auto-merge.yml`, `.github/copilot-instructions.md`, `CURRENT.md`. |
| Feature | Add PLATE Principles v2: autopilot doctrine, issue artifact rules, Design issue type, PR issue-link check workflow, `no-issue` label, `docs/research/` and `docs/design/` scaffolds, `SPEC.md §External Integrations`, updated `AGENTS.md`, `PULL_REQUEST_TEMPLATE.md`, `copilot-instructions.md`, `label-check.yml`, and `research.yml` issue template. | — | Pending merge | `AGENTS.md`, `.github/workflows/pr-issue-link-check.yml`, `.github/ISSUE_TEMPLATE/design.yml`, `docs/research/README.md`, `docs/design/README.md`. |
| Feature | Add Question issue handling: new `Question` type label and issue form, `question-handling.yml` slash-command and answer-sync workflow, and batched GitHub CLI scripts for open-question interaction. | #12 | Pending merge | `.github/labels.yml`, `.github/ISSUE_TEMPLATE/question.yml`, `.github/workflows/question-handling.yml`, `scripts/question_batch.sh`, `scripts/QuestionBatch.ps1`, `AGENTS.md`, `CURRENT.md`. |
| Bug | Fix PR label enforcement: `label-check.yml` now posts an actionable repair comment on the PR when the type label is missing; PR template now has an agent-facing HTML note clarifying that checkboxes do not apply labels; `copilot-instructions.md` now covers both CLI (`--label` at create) and web/API paths (`gh pr edit` immediately after); `AGENTS.md §Documentation Rules` updated accordingly. | #20 | Pending | `.github/workflows/label-check.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/copilot-instructions.md`, `AGENTS.md`. |
