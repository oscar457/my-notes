#Git

Git manages versions of projects.
Each version of a project is called a commit. Each commit is a snapshot of the entire project. The collection of commits contain the history of the project.
All commits belong to a branch (an independent line of development of the project). By default, there is a master branch. The independence of branches allows simultaneous stability and development. After the merge, the master branch contains the new feature. Pull request are requests to merge your branch into another branch. Pull requests can include team review and testing, improving product quality.

Git is a distributed version control system. Version control includes complete history tracked and available at any point of time, supports many workflows (collaboration, reviews), manages small changes and easily test fix and undo changes. A git repository is a series of commits.

Basic git syntax: git [command] [--flags] [arguments]
Full help for a command: git help [command]
Config for your computer using git config

Working Tree is the location on your computer that contains files of a single commit. Staging area contains a list of files that are planned to be included in the next commit that you make. Local repository contains all of the commit.

View status using git status, stage content to staging area using git add, commit content to local repository using git commit, View the commit history using git log. 
