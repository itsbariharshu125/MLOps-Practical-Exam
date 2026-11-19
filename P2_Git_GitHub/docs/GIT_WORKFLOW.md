# Practical 2: Git and GitHub Workflow

Run these commands from the repository root. Replace the example branch name
with a short name that describes your task.

## Configure Git

Set your commit identity globally (for all repositories on this computer), or
omit `--global` to configure only this repository:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Check a setting with `git config --global --get user.name` (replace the key as
needed). Do not use another person's identity.

## Stage and commit changes

```sh
git status
git add path/to/changed-file
git status
git commit -m "Describe the change"
```

Use `git add -A` to stage all intentional changes in the repository. Review
`git status` before committing so generated files or unrelated changes are not
included.

## Create and switch branches

Start from an up-to-date `main` and create a feature branch:

```sh
git switch main
git pull --ff-only origin main
git switch -c practical2/git-workflow
```

Switch to an existing branch with `git switch branch-name`. Keep task changes
on the feature branch rather than committing directly to `main`.

## Merge changes

After review, merge the feature branch into `main`. For a local merge:

```sh
git switch main
git pull --ff-only origin main
git merge practical2/git-workflow
```

For team work, use a GitHub Pull Request (below) as the normal way to merge.
Do not merge until conflicts are resolved and required checks pass.

## Push and pull with GitHub

Push a new branch and set its upstream:

```sh
git push -u origin practical2/git-workflow
```

Fetch and integrate the latest `main` without creating a merge commit when a
fast-forward is possible:

```sh
git switch main
git pull --ff-only origin main
```

`git pull` fetches remote changes and integrates them into the current branch.
Check the current branch with `git branch --show-current` before pulling.

## Open a Pull Request

1. Push your feature branch to `origin`.
2. On GitHub, create a Pull Request with the feature branch as the compare
   branch and `main` as the base branch.
3. Summarize the change, review the diff, and respond to review feedback.
4. Wait for required checks and approval, then merge using the repository's
   permitted merge option.

## Resolve merge conflicts

When a merge or pull reports conflicts, inspect the affected files and status:

```sh
git status
```

Open each conflicted file. Edit the content to keep the intended result, and
remove all conflict-marker lines (`<<<<<<<`, `=======`, and `>>>>>>>`). Then
stage the resolved files and complete the merge:

```sh
git add path/to/resolved-file
git status
git commit
```

Review the final diff before staging. If the correct resolution is unclear,
stop and coordinate with the contributor rather than discarding their work.
