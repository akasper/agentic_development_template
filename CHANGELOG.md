# Changelog

All notable changes to this project should be recorded here. Each release entry should link issues, pull requests, tests, documentation updates, wiki pages, migration notes, and audit findings where applicable.

## Unreleased

| Type | Change | Issue | PR | Evidence |
|---|---|---|---|---|
| Process | Establish PLATE template artifact baseline. | — | #2 | Repository files, labels, templates, and workflow scaffolds. |
| Process | Add GitHub bootstrap guidance and automation based on recent repository setup lessons, including atomic PR labeling guidance for agents. | — | Pending merge | `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `.github/copilot-instructions.md`, `docs/bootstrap/new-repository-checklist.md`, `scripts/bootstrap_github.sh`, `scripts/BootstrapGitHub.ps1`. |
| Feature | Add autonomous mode: `AGENTS.md §Autonomous Mode`, `auto-merge` label, `auto-merge.yml` workflow with marker-file gate, updated `copilot-instructions.md` and `CURRENT.md`. Mode is off by default; toggle via `.github/AUTONOMOUS_MODE`. | — | Pending merge | `AGENTS.md`, `.github/labels.yml`, `.github/workflows/auto-merge.yml`, `.github/copilot-instructions.md`, `CURRENT.md`. |
| Feature | Add PLATE Principles v2: autopilot doctrine, issue artifact rules, Design issue type, PR issue-link check workflow, `no-issue` label, `docs/research/` and `docs/design/` scaffolds, `SPEC.md §External Integrations`, updated `AGENTS.md`, `PULL_REQUEST_TEMPLATE.md`, `copilot-instructions.md`, `label-check.yml`, and `research.yml` issue template. | — | Pending merge | `AGENTS.md`, `.github/workflows/pr-issue-link-check.yml`, `.github/ISSUE_TEMPLATE/design.yml`, `docs/research/README.md`, `docs/design/README.md`. |
