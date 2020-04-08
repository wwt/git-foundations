# Review The Pull Request Impact to Your Local Git Repository



From your terminal, pull the latest changes from GitHub to your local repository
Use the following command:



```shell
git pull
```



Notice the message indicating your local branch, 'Branch3' doe not exist in GitHub

Use the following command to list your local branches:



```shell
git branch
```

Notice 'Branch3' remains in your local repository

Use the following command to change to the 'master' branch:



```shell
git checkout master
```

Notice the message:
The local copy of the 'master' branch is behind the remote 'master' branch
The local copy of 'master' branch 'can be fast-forwarded'

Use the following command to catch your local 'master' branch up with GitHub



```shell
git pull
```

Notice the output which indicates file changes and insertions

Use the following command to delete 'Branch3' from the local repository



```shell
git branch -d Branch3
```

Use the following command to list your local branches:



```shell
git branch
```

Notice the only branch in your local repository is 'master'



[Next Section > Clone Another Repository, Make Changes, and Create a New Pull Request](section_13.md "Clone Another Repository, Make Changes, and Create a New Pull Request")

