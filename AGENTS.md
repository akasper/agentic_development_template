# PLATE Agent Operating Rules

This repository follows the **Process Lifecycle Agentic Task Engine (PLATE)** methodology. The local operating doctrine is simple: **humans keep judgment, agents do the toil, and GitHub preserves truth**.

Agents working here should treat repository artifacts as durable project memory, not as optional narrative. Issues, labels, tests, pull requests, `CURRENT.md`, wiki pages, release notes, audit outputs, and traceability records are the inspectable record of the project.

## Authority Model

The PLATE book explains doctrine and the reasons behind the method. This repository is the source of truth for the **installable template artifacts** because those files must evolve faster than a long-form book can safely absorb. When a repository artifact and book prose disagree, do not preserve both versions indefinitely. Open a corrective issue or pull request that reconciles the doctrine, the template artifact, and any migration note required for existing users.

| Area | Agent May Do | Human Must Decide |
|---|---|---|
| Product intent | Draft proposals, clarify ambiguities, identify conflicts, and map work to issues. | Final scope, priority, product tradeoffs, public commitments, and roadmap direction. |
| Implementation | Modify code, tests, docs, and configuration inside an approved task. | Acceptance of risk, merge approval, release approval, and irreversible operational changes. |
| Process | Follow PLATE rules, detect drift, and suggest process improvements. | Changing required gates, weakening checks, changing merge policy, or adopting new required automation. |
| Documentation | Update `CURRENT.md`, wiki source pages, release notes, audit notes, and traceability records. | Approving claims that affect customers, pricing, legal posture, security posture, or roadmap promises. |

## Required Work Loop

For a normal Feature task, follow this loop.

| Step | Required Behavior |
|---|---|
| 1 | Confirm the issue is labeled `Feature` and has exactly one relevant `Epic: short-name` label. |
| 2 | Identify acceptance criteria, expected tests, documentation impact, and risk. |
| 3 | Add or update tests before or alongside implementation. |
| 4 | Implement the smallest coherent change that satisfies the issue. |
| 5 | Update `CURRENT.md` to describe the implemented behavior and verification evidence. |
| 6 | Open a pull request labeled `Feature` and complete the PR template. |
| 7 | Leave wiki-sync context, release-note context, and audit evidence for the human reviewer and post-merge workflows. |

For a Bug task, reproduce the failure or document why reproduction is not yet possible, add regression coverage, and label missing information with `need:reproduction`, `need:tests`, or `need:human-review` as appropriate.

## Autonomous Mode

Autonomous mode is an opt-in operating posture for unattended sessions (overnight runs, long-running autopilot, `/delegate` tasks) where no human reviewer is available interactively. It selectively lifts the self-merge prohibition for lightweight, low-risk PRs.

**Toggle:** Create `.github/AUTONOMOUS_MODE` on the default branch to enable. Delete it to return to normal human-in-the-loop operation. The file content is ignored; its presence is the signal.

**When autonomous mode is active:**

| Rule | Normal Mode | Autonomous Mode |
|---|---|---|
| Agent may merge own PRs | Never | Permitted for eligible `risk:low` PRs only |
| Must wait for human merge | Always | May call `gh pr merge --auto --squash` on eligible PRs |
| May add `auto-merge` label | No | Yes, for eligible PRs |

**Eligibility criteria — all must be true for a PR to qualify:**

- Labeled `risk:low`
- Does not modify `AGENTS.md`, `SPEC.md`, `.github/CODEOWNERS`, or any workflow file
- Does not add, remove, or alter credential handling, payment logic, authentication, or security controls
- Does not carry `need:human-review` or `need:security-review`
- Does not change public-facing claims in `README.md` or marketing documentation

**How to auto-merge an eligible PR in autonomous mode:**

```bash
gh pr create --label "risk:low" --label "auto-merge" [other required labels] ...
gh pr merge --auto --squash <PR_NUMBER>
```

The `.github/workflows/auto-merge.yml` workflow also triggers on the `auto-merge` label and verifies the marker file before proceeding — providing a second gate.

**GitHub settings required** (one-time per repository):

```bash
# Allow the repo to use auto-merge
gh api -X PATCH repos/OWNER/REPO -f allow_auto_merge=true

# Allow Actions to write PRs and contents (needed by the workflow)
gh api -X PUT repos/OWNER/REPO/actions/permissions/workflow \
  -f default_workflow_permissions=write \
  -F can_approve_pull_request_reviews=false
```

**Security posture:** Autonomous mode intentionally cannot self-escalate. An agent operating in autonomous mode may not create, modify, or delete `.github/AUTONOMOUS_MODE` itself, and may not relax branch protection rules or modify the eligibility criteria in this file.

## Label Rules

Use labels as stable process metadata. Do not create ad hoc labels unless they change routing, enforcement, reporting, auditing, review burden, or agent behavior. Use GitHub Projects fields for frequently changing planning state such as status, priority, owner, rank, iteration, target date, or release target.

| Label Family | Usage |
|---|---|
| `Bug`, `Feature`, `Epic`, `Research`, `Audit`, `Migration` | Exactly one required issue type label. |
| `Bug`, `Feature`, `Documentation` | Exactly one required pull request type label. |
| `Epic: short-name` | Epic identity and feature grouping. Required on Epic and Feature issues. |
| `area:*` | Stable subsystem or ownership area. |
| `risk:*` | Review burden and release caution. |
| `need:*` | Missing input or required follow-up. |

## Documentation Rules

Every Feature pull request must modify `CURRENT.md`. Documentation pull requests should explain whether they update process artifacts, product documentation, wiki source material, or public-facing claims. If a change affects feature behavior, update both implementation evidence and documentation evidence.

## Wiki Sync Rules

The **Sync to Wiki on Merge** workflow is opt-in. Agents should not enable broad wiki writes without human approval. Prefer scoped page updates, provenance comments, auditable commits, and reversible changes. If wiki synchronization is requested but not configured, add `need:wiki-sync` and escalate.

## Escalation Rules

Escalate to a human when product intent is ambiguous, acceptance criteria conflict, a required label is missing and cannot be inferred, a workflow would need to be weakened, a secret or permission is required, a public claim might change, or the agent cannot produce the required evidence.

## Prohibited Actions

Agents must not merge their own pull requests **unless autonomous mode is active (`.github/AUTONOMOUS_MODE` present on the default branch) and the PR meets all eligibility criteria in §Autonomous Mode above**. Agents must not bypass required checks, remove documentation gates, weaken tests to pass CI, fabricate test results, silently rewrite product intent, expose secrets, enable write automation without approval, create or delete `.github/AUTONOMOUS_MODE` themselves, or treat chat history as more authoritative than repository artifacts.
