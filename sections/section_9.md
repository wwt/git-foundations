# Stage, Commit, &, Push Changes to GitHub



From your terminal, Add your '.gitcommit' file to the staging area with the following command:



```shell
git add .gitignore
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice the '.gitignore' file in the section, 'Changes to be committed'

De-commit the stage of the '.gitignore' file with the following command:



```shell
git restore --staged .gitignore
```

This command is useful to upstage a commit

Use the following command to view the status of your local repository:



```shell
git status
```

Re-add your '.gitcommit' file to the staging area with the following command:



```shell
git add .gitignore
```

Commit your '.gitignore' file to your local repository with the following command:



```shell
git commit -m "Added '.DS_Store' to exclude macOS Spotlight Index"
```

The '-m' indicates a comment follows; Git requires a comment with every commit

Use the following command to view the status of your local repository:



```shell
git status
```

Notice your working branch and that you have no changes to commit
Optionally, you may edit commit comments with the 'git commit --amend' command
This command will open your configured Git file editor, VIM is the default
After you view the file, press '<esc>' and type ':q!' to quit without saving changes



```shell
git commit --amend
```

Attempt to push your changes to GitHub with the following command:



```shell
git push
```

Notice the error message
This error occurs because the local branch does not yet exist in GitHub

Push your local branch and committed changes to GitHub with the following command:



```shell
git push --set-upstream origin Branch3
```

Notice the output indicating a new branch on GitHub:
'To github.wwt.com:hullt/ex1.git'
 '* [new branch]      Branch3 -> Branch3'

Log on to https://github.wwt.com (ATC VPN required)
Open your Git repository
From the home screen, your repository list is on the left
Click the 'Branch:' button and choose your new branch
Notice the comment and timestamp for the '.gitignore' file within the new branch



[Next Section > Make Local Git Repository Changes with Atomic Commits](section_9.md "Make Local Git Repository Changes with Atomic Commits")

