#Git

Git manages versions of projects.
Each version of a project is called a commit. Each commit is a snapshot of the entire project. The collection of commits contain the history of the project.
All commits belong to a branch (an independent line of development of the project). By default, there is a master branch. The independence of branches allows simultaneous stability and development. After the merge, the master branch contains the new feature. Pull request are requests to merge your branch into another branch. Pull requests can include team review and testing, improving product quality.

Git is a distributed version control system. Version control includes complete history tracked and available at any point of time, supports many workflows (collaboration, reviews), manages small changes and easily test fix and undo changes. A git repository is a series of commits.

Basic git syntax: git [command] [--flags] [arguments]
Full help for a command: git help [command]
Config for your computer using git config

Working Tree is the location on your computer that contains files of a single commit. Staging area contains a list of files that are planned to be included in the next commit that you make. Local repository contains all of the commit.

View status using git status, stage content to staging area using git add, commit content to local repository using git commit, View the commit history using git log. If no local repo, clone the remote else add remote. git push to add content from local to remote repo.

Git models the relationship of commits (nodes) with a directed acyclic graph. Arrow points at a commit's parents. A branch occurs if a commit has more than one child. A merge occurs when a commit has more than one parent.

Git objects contains a Commit Object (commit message, reference to parent and root tree), Annotated Tag (A reference to a specific commit), Tree (Directories and filenames in the project), Blob (Content of a file in the project). A Git ID (SHA-1) is a name of a Git Object. git log --oneline shortens the git id.

Reference is a user-friendly name that points to a commit SHA-1 hash. A branch label points to the most recent commit in the branch and they are labeled as references. HEAD is a reference to a current commit (can view in git repo or by git log). To refer to a prior commit use ~ (eg. HEAD~). Using ^ refers to a parent in a merge commit (^ : first parent of the commit). A tag is a reference attached to a specific commit. Tags can be used instead of branch labels or sha-1 values.

Git branches enable experimentation by isolating the work, supports multiple project versions.Creating branch using git branch <name>, git checkout updates the HEAD reference, updates the working tree with the commit's files. Detached HEAD reference points directly to a commit, fix a detached HEAD by creating a branch.

Merging. There are 4 types of merge: Fast Forward Merge, Merge commit, Squash merge, Rebase. In a FF merge, git merge moves the base branch label to the tip of the topic branch (only possible if no other commits on base branch). In a merge commit, it combines the commits at the tips of the merged branches and places the result in the merge commit. While combining branches there may be some merge conflicts (if two branches changes same chunk in one file). For resolving merge conflicts while merging in master, Fix and stage the file causing the conflict.

A tracking branch is a local branch that represents a remote branch named as <remote>/<branch> (eg. origin/master). Tracking branches can be out of sync after commiting some changes and can be updated with network commands like clone, fetch, pull, push. Clone copies a remote repository, Fetch retrieves new objects and references from the remote repository, tracking branches are updated. Pull fetches and merges commits locally. Push adds new objects and references to remote repository. Rebase moves commit to a new parent (base). Git can calculate the difference between commits using DIFFS. Rebasing is kind of a merge so it can lead to merge conflicts. git rebase <upstream> <branch> checks out branch and changes its parent to upstream.

Amending a commit. you can change the most recent commit using git commit --amend. Interactive rebase lets you edit commits using git rebase -i <after-this-commit>, this opens several options such as reword (edit commit message), squash (use commit and meld into previous commit), drop (remove commit).

Pull request is used to merge a branch into the project. Forking is copying a remote repository to your own account. The upstream repository is the source repository. A centralized workflow involves working on a single branch, In a feature branch workflow, work is done on feature branch and then merged into longer running branches. In a forking workflow, work is added upstream using PRs. 
