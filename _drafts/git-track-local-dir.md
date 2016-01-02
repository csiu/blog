## Work around to keep track of only certain files 

### Setup
1. git clone the repository of interest
2. rsync .git directory of the clone to the directory of interest
3. In the new directory, [git ignore locally deleted folder](http://stackoverflow.com/questions/4589333/git-ignore-locally-deleted-folder)

    ```
git ls-files --deleted -z | git update-index --assume-unchanged -z --stdin
```

4. Add .gitignore file to ignore everything else

### Making changes (on a new branch)
Create a new branch
```
git checkout -b make
```
and git add/commit changes there.

### Rebase
Be on branch "make" and rebase to move new-feature to the tip of master:
```
git checkout make
git rebase master
```

Do standard fast-forward merge from master:
```
git checkout master
git merge new-feature
```

Rebase Reference:

- http://stackoverflow.com/questions/11563319/git-rebase-basics
- https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog
- https://git-scm.com/docs/git-rebase

- [How to pull specific directory with git](http://stackoverflow.com/questions/2425059/how-to-pull-specific-directory-with-git)
    ```
git fetch
git checkout HEAD path/to/your/dir/or/file
```
