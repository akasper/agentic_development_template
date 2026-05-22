# PLATE Pull Request

## Summary

Describe the change in plain language. Explain what changed, why it changed, and what a reviewer should focus on.

## Required PR Type Label

Apply at least one required PR type label before review.

| Label | Use When |
|---|---|
| `Bug` | The PR fixes incorrect behavior or a regression. |
| `Feature` | The PR adds or changes product behavior. |
| `Documentation` | The PR changes only documentation, examples, process artifacts, or public explanation. |

- [ ] This PR has a required type label: `Bug`, `Feature`, or `Documentation`.
- [ ] If this is a `Feature` PR, it modifies `CURRENT.md`.
- [ ] If this is a `Feature` PR, it includes or identifies the relevant `Epic: short-name` label or linked epic.

## Linked Work

Closes or relates to:

- 

## Tests and Evidence

| Verification | Result | Notes |
|---|---|---|
| Unit tests | Not run |  |
| Integration tests | Not run |  |
| End-to-end tests | Not run |  |
| Manual verification | Not run |  |
| Regression coverage | Not applicable |  |

Describe any failing tests that were added before implementation, any tests that could not be run, and any evidence a reviewer should inspect.

## Documentation and Traceability

| Artifact | Updated? | Notes |
|---|---|---|
| `SPEC.md` | No |  |
| `CURRENT.md` | No | Required for Feature PRs. |
| Wiki source / wiki context | No |  |
| Release notes / changelog | No |  |
| Public claims / marketing | No |  |

## Risk and Rollback

| Question | Answer |
|---|---|
| Risk label | `risk:low` / `risk:medium` / `risk:high` / `risk:critical` |
| Main risk |  |
| Rollback plan |  |
| Human decision needed? | No |

## Agent Self-Review

- [ ] I followed `AGENTS.md` and `.agentic/process.yml`.
- [ ] I did not weaken tests, checks, or documentation gates to make the PR pass.
- [ ] I updated durable project memory rather than relying on chat history.
- [ ] I identified missing information with `need:*` labels or reviewer notes.
- [ ] I left enough evidence for a human to judge the change.
