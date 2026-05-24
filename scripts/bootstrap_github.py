#!/usr/bin/env python3

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_LABELS_TO_REMOVE = [
    "bug",
    "documentation",
    "duplicate",
    "enhancement",
    "good first issue",
    "help wanted",
    "invalid",
    "question",
    "wontfix",
]


def run(command, cwd=None, capture_output=True):
    result = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=capture_output,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Command failed: {' '.join(command)}\n{detail}")
    return result.stdout.strip() if capture_output else ""


def parse_labels(path):
    labels = []
    current = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            if current:
                labels.append(current)
            current = {}
            key, value = line[2:].split(":", 1)
            current[key.strip()] = value.strip().strip('"')
            continue
        if current and ":" in line:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
    if current:
        labels.append(current)
    return labels


def gh_json(args, cwd=None):
    return json.loads(run(["gh", *args], cwd=cwd))


def replace_codeowners(local_repo, owner_handle):
    codeowners = local_repo / ".github" / "CODEOWNERS"
    content = codeowners.read_text(encoding="utf-8")
    updated = content.replace("@PLATE_REPO_OWNER", owner_handle)
    if updated != content:
        codeowners.write_text(updated, encoding="utf-8")
        return True
    return False


def sync_labels(repo, labels):
    existing = {
        label["name"].lower(): label
        for label in gh_json(["label", "list", "--repo", repo, "--limit", "200", "--json", "name,color,description"])
    }
    for label in labels:
        args = [
            "--repo",
            repo,
            "--name",
            label["name"],
            "--color",
            label["color"],
            "--description",
            label["description"],
        ]
        current = existing.get(label["name"].lower())
        if current:
            run(["gh", "label", "edit", current["name"], *args], capture_output=False)
        else:
            run(["gh", "label", "create", label["name"], *args], capture_output=False)


def remove_default_labels(repo, canonical_names):
    existing = gh_json(["label", "list", "--repo", repo, "--limit", "200", "--json", "name"])
    existing_names = {label["name"].lower() for label in existing}
    canonical_lower = {name.lower() for name in canonical_names}
    for label_name in DEFAULT_LABELS_TO_REMOVE:
        if label_name in canonical_lower or label_name not in existing_names:
            continue
        run(["gh", "label", "delete", label_name, "--repo", repo, "--yes"], capture_output=False)


def set_delete_branch_on_merge(repo):
    run(["gh", "repo", "edit", repo, "--delete-branch-on-merge"], capture_output=False)


def protect_branch(repo, branch):
    payload = {
        "required_status_checks": None,
        "enforce_admins": False,
        "required_pull_request_reviews": None,
        "restrictions": None,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "block_creations": False,
        "required_conversation_resolution": True,
        "lock_branch": False,
        "allow_fork_syncing": True,
    }
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
        json.dump(payload, handle)
        temp_path = handle.name
    try:
        run(
            [
                "gh",
                "api",
                "--method",
                "PUT",
                "-H",
                "Accept: application/vnd.github+json",
                f"repos/{repo}/branches/{branch}/protection",
                "--input",
                temp_path,
            ],
            capture_output=False,
        )
    finally:
        Path(temp_path).unlink(missing_ok=True)


def initialize_wiki(repo, local_repo):
    home = local_repo / "docs" / "wiki" / "Home.md"
    if not home.exists():
        raise RuntimeError(f"Wiki source file not found: {home}")

    user = gh_json(["api", "user"])
    author_name = user.get("name") or user["login"]
    author_email = user.get("email") or f"{user['login']}@users.noreply.github.com"
    token = run(["gh", "auth", "token"])

    temp_dir = Path(tempfile.mkdtemp(prefix="plate-wiki-"))
    try:
        clone_url = f"https://x-access-token:{token}@github.com/{repo}.wiki.git"
        run(["git", "clone", clone_url, str(temp_dir)], capture_output=False)
        shutil.copyfile(home, temp_dir / "Home.md")
        if not run(["git", "status", "--short"], cwd=temp_dir):
            return False
        run(["git", "config", "user.name", author_name], cwd=temp_dir, capture_output=False)
        run(["git", "config", "user.email", author_email], cwd=temp_dir, capture_output=False)
        run(["git", "add", "Home.md"], cwd=temp_dir, capture_output=False)
        run(["git", "commit", "-m", "docs: initialize wiki home page"], cwd=temp_dir, capture_output=False)
        run(["git", "push", "origin", "master"], cwd=temp_dir, capture_output=False)
        return True
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def print_manual_steps():
    print("\nManual follow-up still required:")
    print("1. Replace placeholder product language in SPEC.md, CURRENT.md, and public-facing docs.")
    print("2. Decide whether branch protection should also require approvals, code-owner review, status checks, or linear history.")
    print("3. Configure GitHub Projects fields for planning state such as status, priority, owner, iteration, target date, and release target.")
    print("4. Create real Epic: short-name labels and the first Epic issue.")
    print("5. Tune CI, release, pages, and audit workflows for the project stack.")
    print("6. Decide whether to enable wiki sync and, if so, create PLATE_WIKI_SYNC_ENABLED and WIKI_TOKEN.")


def parse_args():
    parser = argparse.ArgumentParser(description="Bootstrap standard GitHub settings for a new PLATE repository.")
    parser.add_argument("--repo", required=True, help="GitHub repository in OWNER/REPO format.")
    parser.add_argument("--local-repo", default=".", help="Path to the local repository checkout.")
    parser.add_argument("--owner-handle", help="GitHub username or team handle for CODEOWNERS, for example @your-username.")
    parser.add_argument("--remove-default-labels", action="store_true", help="Delete conflicting default GitHub labels.")
    parser.add_argument("--set-delete-branch-on-merge", action="store_true", help="Enable delete-branch-on-merge.")
    parser.add_argument("--protect-branch", metavar="BRANCH", help="Apply conservative baseline protection to the named branch.")
    parser.add_argument("--init-wiki", action="store_true", help="Initialize the wiki with docs/wiki/Home.md.")
    return parser.parse_args()


def main():
    args = parse_args()
    local_repo = Path(args.local_repo).resolve()
    labels_path = local_repo / ".github" / "labels.yml"
    if not labels_path.exists():
        raise RuntimeError(f"Label registry not found: {labels_path}")

    run(["gh", "auth", "status"])

    labels = parse_labels(labels_path)
    sync_labels(args.repo, labels)
    print(f"Synced {len(labels)} canonical labels.")

    if args.remove_default_labels:
        remove_default_labels(args.repo, [label["name"] for label in labels])
        print("Removed conflicting default GitHub labels.")

    if args.owner_handle:
        changed = replace_codeowners(local_repo, args.owner_handle)
        if changed:
            print("Updated .github/CODEOWNERS with the provided owner handle.")
        else:
            print(".github/CODEOWNERS already used the requested owner handle.")

    if args.set_delete_branch_on_merge:
        set_delete_branch_on_merge(args.repo)
        print("Enabled delete-branch-on-merge.")

    if args.protect_branch:
        protect_branch(args.repo, args.protect_branch)
        print(f"Applied baseline protection to {args.protect_branch}.")

    if args.init_wiki:
        changed = initialize_wiki(args.repo, local_repo)
        if changed:
            print("Initialized the wiki homepage from docs/wiki/Home.md.")
        else:
            print("Wiki homepage was already up to date.")

    print_manual_steps()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
