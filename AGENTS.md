# PLATE Agent Operating Rules

This repository follows the **Process Lifecycle Agentic Task Engine (PLATE)** methodology. The local operating doctrine is simple: **humans keep judgment, agents do the toil, and GitHub preserves truth**.

Agents working here should treat repository artifacts as durable project memory, not as optional narrative. Issues, labels, tests, pull requests, `CURRENT.md`, wiki pages, release notes, and audit outputs are the traceable record of the project.

## Authority Boundaries

| Area | Agent May Do | Human Must Decide |
|---|---|---|
| Product intent | Draft proposals, clarify ambiguities, identify conflicts. | Final scope, priority, product tradeoffs, public commitments. |
| Implementation | Modify code, tests, docs, and configuration inside an approved task. | Acceptance of risk, merge approval, release approval. |
| Process | Follow and suggest improvements to PLATE rules. | Changing required gates, weakening checks, changing merge policy. |
| Documentation | Update `CURRENT.md`, wiki source pages, release notes, and audit notes. | Approving claims that affect customers, pricing, legal posture, or roadmap. |

## Required Work Loop

For a normal Feature task, follow this loop.

| Step | Required Behavior |
|---|---|
| 1 | Confirm the issue is labeled `Feature` and has the relevant `Epic: short-name` label. |
| 2 | Identify acceptance criteria, expected tests, documentation impact, and risk. |
| 3 | Add or update tests before or alongside implementation. |
| 4 | Implement the smallest coherent change that satisfies the issue. |
| 5 | Update `CURRENT.md` to describe the implemented behavior and verification evidence. |
| 6 | Open a pull request labeled `Feature` and complete the PR template. |
| 7 | Leave wiki-sync context for the post-merge workflow or the human reviewer. |

For a Bug task, reproduce the failure or document why reproduction is not yet possible, add regression coverage, and label missing information with `need:reproduction`, `need:tests`, or `need:human-review` as appropriate.

## Label Rules

Use labels as stable process metadata. Do not create ad hoc labels unless they change routing, enforcement, reporting, auditing, review burden, or agent behavior. Use GitHub Projects fields for frequently changing planning state.

| Label Family | Usage |
|---|---|
| `Bug`, `Feature`, `Epic`, `Documentation`, `Research`, `Audit`, `Migration` | Work or PR type. |
| `Epic: short-name` | Epic identity and feature grouping. |
| `area:*` | Stable subsystem or ownership area. |
| `risk:*` | Review burden and release caution. |
| `need:*` | Missing input or required follow-up. |
| `priority:*` | Relative priority when a Project field is unavailable. |
| `status:*` | Lightweight status only when a Project field is unavailable. |

## Documentation Rules

Every Feature pull request must modify `CURRENT.md`. Documentation pull requests should explain whether they update book-derived process artifacts, product documentation, wiki source material, or public-facing claims. If the change affects feature behavior, update both implementation evidence and documentation evidence.

## Wiki Sync Rules

When a Feature pull request is merged, the **Sync to Wiki on Merge** workflow may update wiki pages. Until the project defines a stricter wiki-sync safety model, agents should avoid broad wiki rewrites. Prefer scoped page updates, provenance comments, and human-reviewable summaries.

## Escalation Rules

Escalate to a human when product intent is ambiguous, acceptance criteria conflict, a required label is missing and cannot be inferred, a workflow would need to be weakened, a secret or permission is required, a public claim might change, or the agent cannot produce the required evidence.

## Prohibited Actions

Agents must not merge their own pull requests, bypass required checks, remove documentation gates, weaken tests to pass CI, fabricate test results, silently rewrite product intent, expose secrets, or treat chat history as more authoritative than repository artifacts.
