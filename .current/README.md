# Per-ticket current-state entries

Use this directory to record **feature-local implemented state** without forcing every parallel Feature PR to edit `CURRENT.md`.

## Naming

Create one markdown file per issue or ticket:

- `.current/issue-123.md`
- `.current/feature-154-mcp-tools-qanda.md`

## Minimum contents

Each entry should include:

1. Linked issue or ticket reference
2. What changed (implemented behavior only)
3. Verification evidence (tests, artifacts, or workflow links)
4. Any docs/wiki links updated

## Roll-up rule

`CURRENT.md` remains the durable top-level index. Feature PRs may satisfy PLATE documentation requirements by updating either:

- `CURRENT.md`, **or**
- at least one `.current/*.md` entry

During periodic audits or release prep, roll finalized `.current/*.md` details into the relevant `CURRENT.md` rows.
