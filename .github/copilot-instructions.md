# Copilot Instructions

## Build, test, and lint

This template does not define a local build, lint, or test toolchain yet. `tests\README.md` is a placeholder, and `.github\workflows\ci.yml` currently contains a scaffold step that only echoes `"Tests would run here"`.

When a downstream project adds a runtime or package manager, prefer the real project commands over inventing new ones, and update this file with:

- the full test command
- the single-test command for that stack
- any build and lint commands that CI actually uses

## High-level architecture

This repository is a **PLATE template**, not an application codebase. The important architecture is the process wiring between durable project artifacts, machine-readable rules, and GitHub enforcement:

- `SPEC.md` defines the intended goal state.
- `CURRENT.md` records the implemented state and verification evidence.
- `AGENTS.md` defines local agent operating rules and escalation boundaries.
- `.agentic\process.yml` mirrors the same process in machine-readable form for automation and audits.
- `.github\labels.yml`, `.github\ISSUE_TEMPLATE\`, and `.github\PULL_REQUEST_TEMPLATE.md` define the work intake and review metadata.
- `.github\workflows\label-check.yml` enforces required issue and PR type labels.
- `.github\workflows\pr-documentation-check.yml` enforces that `Feature` PRs update `CURRENT.md`.
- `.github\workflows\sync-wiki-on-merge.yml` runs only for merged `Feature` PRs on `main`, then copies scoped documentation sources into the GitHub wiki.

Read those pieces together when making process changes. A change in one of them usually implies matching updates in the others.

## Key conventions

- Treat repository artifacts as the source of durable truth. If behavior, process, or evidence changes, update the relevant artifact instead of relying on chat history.
- If `AGENTS.md`, `.agentic\process.yml`, and the template files disagree, preserve the PLATE intent and keep them aligned.
- Labels are stable process metadata, not casual tags. Use type labels (`Bug`, `Feature`, `Epic`, `Documentation`, `Research`, `Audit`, `Migration`) and prefixed labels (`Epic:`, `area:`, `risk:`, `need:`, `priority:`, `status:`) according to the existing taxonomy.
- `Feature` issues must carry both the `Feature` label and a matching `Epic: short-name` label. Their issue template expects acceptance criteria, test expectations, and documentation impact.
- `Bug` work should include a reproduction path or explicitly signal the gap with `need:reproduction`, plus a regression test plan.
- Every PR must carry a type label. `Feature` PRs must update `CURRENT.md`; documentation-only changes should use the `Documentation` label instead of pretending to be product behavior changes.
- Prefer small, scoped documentation and wiki updates. The wiki sync workflow is intentionally conservative and currently treats `CURRENT.md`, `docs\wiki`, and `docs\features` as the sync inputs.
- Do not weaken tests, documentation gates, or workflow checks to make a change pass. Human review and merge authority remain outside agent authority.
