# PLATE Template Repository

This repository is the installable baseline for a **Process Lifecycle Agentic Task Engine (PLATE)** project. PLATE is a GitHub-first methodology for agent-assisted software delivery in which **humans keep judgment, agents do the toil, and GitHub preserves truth**.

This repository should be treated as the **artifact source of truth for the template package**. The PLATE book should explain doctrine, operating principles, and the reasons behind the process; this repository should carry the fast-changing files, templates, workflow scaffolds, and machine-readable policy that agents and humans actually install. If the book and repository drift, open a corrective issue or pull request rather than duplicating large artifact appendices in the book.

## What This Template Provides

A PLATE repository gives a human project owner and an agent a shared operating environment. It defines the canonical files that preserve project memory, the labels that route work, the issue forms that shape intent, the pull request template that captures evidence, and workflow scaffolds that enforce the most important rules.

| Artifact | Purpose |
|---|---|
| `SPEC.md` | Describes product intent, user outcomes, constraints, non-goals, and major decisions. |
| `CURRENT.md` | Records what the software currently does and how that behavior is verified. |
| `AGENTS.md` | Defines local operating rules for agents working in this repository. |
| `.agentic/process.yml` | Encodes PLATE process rules in machine-readable form. |
| `.agentic/skills.yml` | Describes controlled agent capability profiles and evidence obligations. |
| `.agentic/extensions.yml` | Records optional process extensions and their compatibility requirements. |
| `.agentic/audit.yml` | Defines drift checks, severities, output paths, and escalation behavior. |
| `.agentic/traceability.yml` | Defines the evidence chain from intent to release. |
| `.agentic/marketing.yml` | Keeps public claims tied to implemented product truth. |
| `.github/labels.yml` | Defines the canonical stable label taxonomy for bootstrapping or reconciliation. |
| `.github/ISSUE_TEMPLATE/` | Provides structured entry points for epics, features, bugs, research, audits, and migrations. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Captures implementation evidence, documentation updates, and human review context. |
| `.github/workflows/` | Provides enforcement scaffolds for CI, labels, documentation checks, audits, releases, pages, and wiki sync. |

## Quick Start

Create a new repository from this template, then complete the bootstrap checklist below. The first bootstrap pass should create labels, enable GitHub Actions, configure repository permissions, enable GitHub Projects for planning state, and enable the wiki only if wiki synchronization will be used.

| Step | Action |
|---|---|
| 1 | Replace placeholder project language in `SPEC.md` and `CURRENT.md`. |
| 2 | Review `AGENTS.md` and adjust allowed commands, escalation rules, and project-specific safety constraints. |
| 3 | Apply `.github/labels.yml` using a label-sync tool or by creating labels manually. |
| 4 | Configure GitHub Projects fields for mutable planning state such as status, priority, owner, iteration, target date, and release target. |
| 5 | Confirm that issue forms apply exactly one issue type label and that Feature and Epic issues receive an `Epic: short-name` label. |
| 6 | Enable the workflows in `.github/workflows/`, then tune CI, audit, release, and pages jobs for the project stack. |
| 7 | If using wiki sync, set repository variable `PLATE_WIKI_SYNC_ENABLED=true`, create a `WIKI_TOKEN` secret with the narrowest practical permissions, and review the safety model before enabling writes. |
| 8 | Add the first Epic issue and create a running project example that can be reused across documentation, tests, and wiki pages. |

## Label Taxonomy Principle

Labels are not decoration. In PLATE, labels are stable machine-readable process metadata. A label should exist only if it changes routing, enforcement, auditing, reporting, review burden, or agent behavior. If a state changes frequently during planning, use a GitHub Projects field instead of a label.

The canonical label categories are **type**, **epic**, **area**, **risk**, and **need**. The `need:` prefix is singular by convention. This template intentionally does **not** include default `status:*` or `priority:*` labels because those categories create duplicate sources of truth when GitHub Projects fields are available.

## Required Label Rules

Every issue must have exactly one PLATE issue type label from `Bug`, `Feature`, `Epic`, `Research`, `Audit`, or `Migration`. Every pull request must have exactly one PLATE PR type label from `Bug`, `Feature`, or `Documentation`.

Every Epic issue must define and carry a matching `Epic: short-name` label. Every Feature issue must carry exactly one corresponding `Epic: short-name` label. Every Feature pull request must modify `CURRENT.md` and pass the **PR Documentation Check** workflow.

## Wiki Synchronization

PLATE expects documentation to move with the product, but automated wiki writes should be explicit rather than accidental. The **Sync to Wiki on Merge** workflow is disabled by default. When enabled, it runs only for merged Feature pull requests, captures provenance, copies only scoped source directories, and commits with an auditable message. Projects should refine the wiki-sync safety model before allowing broad automated rewrites.

## Human Merge Rule

Agents may prepare work, write tests, update documentation, and propose pull requests. They must not silently redefine product intent, bypass required checks, weaken quality gates, or merge their own work. A human remains responsible for judgment and merge authority.
