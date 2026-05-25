# PLATE Template Synchronization

Use this skill to import upstream PLATE template changes into a downstream repository **without erasing local customization**.

## Inputs

- Source template repository: `https://github.com/akasper/plate_template`
- Sync state file: `.plate/upstream-ref`
- Target branch: downstream default branch or an explicit sync branch

## Required Process

1. Read `.plate/upstream-ref` and capture `last_synced_commit`.
2. Fetch upstream and identify `latest_upstream_commit`.
3. Build the candidate change set for core PLATE files:
   - `AGENTS.md`
   - `SPEC.md`
   - `.agentic/*.yml`
   - `.github/workflows/*.yml`
   - `.github/labels.yml`
   - templates and process docs as needed
4. For each file, pick a merge strategy and record it in migration notes:
   - **Managed-block update** for content between markers such as `<!-- PLATE-CORE-START:* -->` and `<!-- PLATE-CORE-END:* -->`
   - **Targeted hunk merge** for files without markers
   - **No change** when local policy intentionally diverges
5. Never replace an entire customized file unless a human explicitly approves.
6. Validate affected checks/tests and confirm no policy regressions.
7. Update `.plate/upstream-ref` only after sync edits are complete and validated.
8. Open a **Documentation PR** with migration notes and evidence.

## Safety Rules

- Preserve downstream behavior by default.
- Escalate with `need:human-review` when upstream and local policy conflict.
- Keep PRs small and atomic (split by area when needed).
- Use exactly one required PR type label at creation time (`Documentation` for docs/process-only changes, `Feature` when executable behavior changes).

## Suggested Commands

```bash
# one-time in downstream repo
if ! git remote get-url plate-upstream >/dev/null 2>&1; then
  git remote add plate-upstream https://github.com/akasper/plate_template.git
fi

git fetch plate-upstream main

# inspect sync state
cat .plate/upstream-ref

# inspect upstream changes since last sync
# replace OLD with the tracked last_synced_commit
# and NEW with plate-upstream/main
OLD=<last_synced_commit>
NEW=plate-upstream/main

git diff --name-status "$OLD" "$NEW" -- \
  AGENTS.md SPEC.md .agentic .github/workflows .github/labels.yml
```

## Required Migration Notes Template

Commit `docs/migration/plate-template-sync-<yyyy-mm-dd>.md` with:

- Upstream source URL
- Previous synced commit
- New upstream commit
- File-by-file merge strategy
- Before/after snippets for non-trivial edits
- Explicit list of intentionally preserved local customizations
- Follow-up actions and risks
