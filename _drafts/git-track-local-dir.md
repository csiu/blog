clone repo

rsync .git to dir of interest

[Git ignore locally deleted folder](http://stackoverflow.com/questions/4589333/git-ignore-locally-deleted-folder)
git ls-files --deleted -z | git update-index --assume-unchanged -z --stdin

Add .gitignore file

[How to pull specific directory with git](http://stackoverflow.com/questions/2425059/how-to-pull-specific-directory-with-git)
git fetch
git checkout HEAD path/to/your/dir/or/file

make changes on new branch
git checkout -b make

Rebase
http://stackoverflow.com/questions/11563319/git-rebase-basics
https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog
https://git-scm.com/docs/git-rebase

on branch "make" and rebase to move new-feature to the tip of master:
git checkout make
git rebase master

Standard fast-forward merge from master:
git checkout master
git merge new-feature
