# PLATE Template Repository

This repository is the installable baseline for a **Process Lifecycle Agentic Task Engine (PLATE)** project. PLATE is a methodology for agent-assisted software delivery in which **humans keep judgment, agents do the toil, and GitHub preserves truth**.

The template is an artifact of the PLATE book. If the book and this repository disagree, the book is the source of truth. Repository changes should first be described in the book or its appendix artifacts, then ported here.

## What This Template Provides

A PLATE repository gives a human project owner and an agent a shared operating environment. It defines the canonical files that preserve project memory, the labels that route work, the issue forms that shape intent, the pull request template that captures evidence, and workflow scaffolds that enforce the most important rules.

| Artifact | Purpose |
|---|---|
| `SPEC.md` | Describes product intent, user outcomes, constraints, non-goals, and major decisions. |
| `CURRENT.md` | Records what the software currently does and how that behavior is verified. |
| `AGENTS.md` | Defines local operating rules for agents working in this repository. |
| `.agentic/process.yml` | Encodes PLATE process rules in machine-readable form. |
| `.github/labels.yml` | Defines the canonical label taxonomy for bootstrapping or reconciliation. |
| `.github/ISSUE_TEMPLATE/` | Provides structured entry points for epics, features, bugs, research, and audit findings. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Captures implementation evidence, documentation updates, and human review context. |
| `.github/workflows/` | Provides enforcement scaffolds for CI, labels, documentation checks, audits, releases, pages, and wiki sync. |

## Quick Start

Create a new repository from this template, then complete the bootstrap checklist below. The first bootstrap pass should create labels, enable GitHub Actions, configure repository permissions, enable the wiki if wiki sync will be used, and decide whether GitHub Projects will carry planning state such as priority and workflow status.

| Step | Action |
|---|---|
| 1 | Replace placeholder project language in `SPEC.md` and `CURRENT.md`. |
| 2 | Review `AGENTS.md` and adjust allowed commands, escalation rules, and project-specific safety constraints. |
| 3 | Apply `.github/labels.yml` using a label-sync tool or by creating labels manually. |
| 4 | Confirm that issue forms apply the correct type labels and that Feature issues receive an `Epic: short-name` label. |
| 5 | Enable the workflows in `.github/workflows/`, then tune them for the project stack. |
| 6 | If using wiki sync, create a `WIKI_TOKEN` secret with the narrowest practical permissions and review the safety model before enabling writes. |
| 7 | Add the first Epic issue and create a running project example that can be reused across documentation, tests, and wiki pages. |

## Label Taxonomy Principle

Labels are not decoration. In PLATE, labels are stable machine-readable process metadata. A label should exist only if it changes routing, enforcement, auditing, reporting, review burden, or agent behavior. If a state changes frequently during planning, prefer a GitHub Projects field instead of a label.

The canonical label categories are **type**, **epic**, **area**, **risk**, **need**, **priority**, and limited **status**. The `need:` prefix is singular by convention.

## Required Label Rules

Every ordinary issue must have at least one of `Bug`, `Feature`, or `Epic`. Supporting process issues may use `Research`, `Audit`, or `Migration` when the work is intentionally outside ordinary feature delivery.

Every Epic issue must define and carry a matching `Epic: short-name` label. Every Feature issue must carry its corresponding epic label. Every pull request must have at least one of `Bug`, `Feature`, or `Documentation`. Every Feature pull request must modify `CURRENT.md` and pass the **PR Documentation Check** workflow.

## Wiki Synchronization

PLATE expects documentation to move with the product. When a Feature pull request is merged, the repository may run **Sync to Wiki on Merge** to update relevant wiki pages. The workflow in this template is intentionally conservative. It validates token presence, captures PR context, writes only from scoped documentation sources, and commits with explicit provenance. Projects should refine the wiki-sync safety model before allowing broad automated rewrites.

## Human Merge Rule

Agents may prepare work, write tests, update documentation, and propose pull requests. They must not silently redefine product intent, bypass required checks, weaken quality gates, or merge their own work. A human remains responsible for judgment and merge authority.
