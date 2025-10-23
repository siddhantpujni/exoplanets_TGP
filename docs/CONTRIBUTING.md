# Team Contribution Guide

Please read and follow these guidelines for all contributions.

## The Golden Rule

> The `main` branch is our source of truth. It must **always** be stable and deployable. No one ever pushes directly to `main`. All work is done on separate branches.

---

## The Core Workflow: Step-by-Step

All work, from a major new feature to a tiny bug fix, follows this same process.

### Step 1: Sync Your Local `main` Branch

Before starting any new work, ensure you have the most up-to-date version of the code.

```bash
# Switch to your local main branch
git checkout main

# Pull the latest changes from the remote repository on GitHub
git pull origin main 
```

### Step 2: Create a New Branch
Create a new branch off of main for your task. Please follow branch naming conventions to keep things clear and use a prefix followed by a short, descriptive, hyphenated name. Keep things descriptive.

```bash
# This creates a new branch and switches to it automatically. (e.g. feature/more_particles, bug/file_path_error)
git checkout -b prefix/descriptive-name
```
### Step 3: Do whatever you need to
Make occasional commits to just save your work but this is completely safe and won't have any impacts. Following is the process to properly commit changes after a few edits.

```bash
# This stages the commits
git add .

# The following commits them
git commit -m "Descriptive commit message" 
```
### Step 4: Open a pull request
Once finished making changes push your branch with the following and follow the steps after:

1. Use the source control page (Ctrl + Shift + G) to push your changes
2. Go to the repository on GitHub. You will see a prompt to "Compare & pull request". Click it.
3. Fill out the Pull Request template:
    Title: A clear, concise title for your changes.
    Description: Explain what the PR does and why the change was made. If it fixes a specific issue, link to it.
    Reviewers: On the right sidebar, request reviews from at least one or two other team members.

### Step 5: Clean up your workspace stuff with some following commands
```bash
# Switch back to the main branch
git checkout main

# Update it with the code you just merged
git pull origin main

# Delete the local feature branch, as it's no longer needed
git branch -d prefix/descriptive-name
```