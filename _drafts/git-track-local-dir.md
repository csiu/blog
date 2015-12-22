clone repo

rsync .git to dir of interest

[Git ignore locally deleted folder](http://stackoverflow.com/questions/4589333/git-ignore-locally-deleted-folder)
git ls-files --deleted -z | git update-index --assume-unchanged -z --stdin

Add .gitignore file

[How to pull specific directory with git](http://stackoverflow.com/questions/2425059/how-to-pull-specific-directory-with-git)
git fetch
git checkout HEAD path/to/your/dir/or/file
