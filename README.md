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

Create a new repository from this template, then complete the bootstrap checklist below. The first bootstrap pass should create labels, replace placeholders, configure repository settings, enable GitHub Projects for planning state, and initialize the wiki only if wiki synchronization will be used.

For a faster and more repeatable setup, run the bootstrap helper from the generated repository root. Choose the script for your operating system:

**macOS / Linux / WSL (bash):**
```bash
bash scripts/bootstrap_github.sh --repo OWNER/REPO --local-repo . --owner-handle @your-handle --remove-default-labels --set-delete-branch-on-merge --protect-branch main
# Add --init-wiki only if you plan to enable wiki sync.
```

**Windows (PowerShell):**
```powershell
.\scripts\BootstrapGitHub.ps1 -Repo OWNER/REPO -LocalRepo . -OwnerHandle @your-handle -RemoveDefaultLabels -SetDeleteBranchOnMerge -ProtectBranch main
# Add -InitWiki only if you plan to enable wiki sync.
```

Both scripts apply the canonical PLATE labels, remove conflicting default GitHub labels, update `.github/CODEOWNERS`, optionally initialize the wiki from `docs/wiki/Home.md`, enable delete-branch-on-merge, and can apply a conservative baseline branch protection rule. They require only `gh` (GitHub CLI) and `git`.

| Step | Action |
|---|---|
| 1 | Run `scripts/bootstrap_github.sh` (macOS/Linux/WSL) or `scripts\BootstrapGitHub.ps1` (Windows), or complete the same actions manually. |
| 2 | Replace `@PLATE_REPO_OWNER` in `.github/CODEOWNERS` with your GitHub username or team if you did not use the helper. |
| 3 | Replace placeholder project language in `SPEC.md`, `CURRENT.md`, and public-facing docs. |
| 4 | Review `AGENTS.md` and adjust allowed commands, escalation rules, and project-specific safety constraints. |
| 5 | Configure GitHub Projects fields for mutable planning state such as status, priority, owner, iteration, target date, and release target. |
| 6 | Confirm that issue forms apply exactly one issue type label and that Feature and Epic issues receive an `Epic: short-name` label. |
| 7 | Enable the workflows in `.github/workflows/`, then tune CI, audit, release, and pages jobs for the project stack. |
| 8 | Review branch protection and decide whether the baseline rule should also require approvals, code-owner review, status checks, or linear history. |
| 9 | If using wiki sync, set repository variable `PLATE_WIKI_SYNC_ENABLED=true`, create a `WIKI_TOKEN` secret with the narrowest practical permissions, and review the safety model before enabling writes. |
| 10 | Add the first real Epic issue and corresponding `Epic: short-name` label, then create a running project example that can be reused across documentation, tests, and wiki pages. |

The generated repository also includes `docs/bootstrap/new-repository-checklist.md`, which separates automatable bootstrap tasks from human-only decisions.

## Label Taxonomy Principle

Labels are not decoration. In PLATE, labels are stable machine-readable process metadata. A label should exist only if it changes routing, enforcement, auditing, reporting, review burden, or agent behavior. If a state changes frequently during planning, use a GitHub Projects field instead of a label.

The canonical label categories are **type**, **epic**, **area**, **risk**, and **need**. The `need:` prefix is singular by convention. This template intentionally does **not** include default `priority:*` labels because those categories create duplicate sources of truth when GitHub Projects fields are available. The `status:blocked` and `status:ready-to-work` labels are the explicit exception used by PLATES native trigger workflows (see §Autonomous Workflow).

## Required Label Rules

Every issue must have exactly one PLATE issue type label from `Bug`, `Feature`, `Epic`, `Research`, `Design`, `Question`, `Audit`, or `Migration`. Every pull request must have exactly one PLATE PR type label from `Bug`, `Feature`, or `Documentation`.

Every Epic issue must define and carry a matching `Epic: short-name` label. Every Feature issue must carry exactly one corresponding `Epic: short-name` label. Question issues are intentionally not tied to epic labels. Every Feature pull request must modify `CURRENT.md` and pass the **PR Documentation Check** workflow.

## Autonomous Workflow

PLATES provides three GitHub-native workflow triggers that automate the issue lifecycle for agentic task processing. These workflows use issue events, labels, and native GitHub dependencies to chain automation without external services.

### Triggers

| Workflow | File | Trigger | Purpose |
|---|---|---|---|
| Usage Report on Issue Closed | `plates-on-issue-closed.yml` | `Feature` or `Question` issue closed | Parses a structured `=== USAGE REPORT ===` block from the closing comment, appends a row to `.agentic/COSTS.md`, and optionally updates a dashboard issue. |
| Unblock Features | `plates-unblock-features.yml` | Issue closed or labeled | Checks dependent Feature issues via GitHub native issue dependencies. If all blockers are closed, removes `status:blocked` and adds `status:ready-to-work`, then inlines the kickoff logic. |
| Start Feature | `plates-start-feature.yml` | `status:ready-to-work` label applied | Dispatches the orchestrator workflow (if `PLATE_MAIN_ORCHESTRATOR_WORKFLOW` is set) or posts a kickoff comment trigger. |

### Labels

| Label | Purpose |
|---|---|
| `status:blocked` | Applied to Feature issues that have one or more open native GitHub blockers. |
| `status:ready-to-work` | Applied to Feature issues whose blockers are all resolved and that can be started by PLATES triggers. |

### Using Native Dependencies

GitHub supports native issue dependencies via the "blocked by" relationship. To declare that a Feature issue is blocked by another issue:

1. Open the Feature issue.
2. In the sidebar, add a "blocked by" dependency pointing to the blocker issue.
3. Apply the `status:blocked` label to the Feature issue.

When the blocker issue is closed, `plates-unblock-features.yml` automatically checks whether the Feature has remaining open blockers. If none remain, it promotes the Feature to `status:ready-to-work` and triggers the kickoff flow.

### Repository Variables

| Variable | Purpose |
|---|---|
| `PLATE_MAIN_ORCHESTRATOR_WORKFLOW` | Workflow filename to dispatch when a Feature is ready. If unset, a kickoff comment is posted instead. |
| `PLATE_COST_DASHBOARD_ISSUE` | Issue number where usage report summaries are posted as comments. |

## Wiki Synchronization

PLATE expects documentation to move with the product, but automated wiki writes should be explicit rather than accidental. The **Sync to Wiki on Merge** workflow is disabled by default. When enabled, it runs only for merged Feature pull requests, captures provenance, copies only scoped source directories, and commits with an auditable message. Projects should refine the wiki-sync safety model before allowing broad automated rewrites.

## Human Merge Rule

Agents may prepare work, write tests, update documentation, and propose pull requests. They must not silently redefine product intent, bypass required checks, weaken quality gates, or merge their own work. A human remains responsible for judgment and merge authority.
