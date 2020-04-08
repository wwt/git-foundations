# Make Local Git Repository Changes



From your terminal, use the following command to view the status of your local repository:



```shell
git status
```



Notice your working branch and that you have no changes to commit

**The following requires a text editor and this guide uses VIM**
**You may, alternatively, use the text editor of your choice**

Open your .gitignore file in VIM to insert the name '.DS_Store'
Adding the name '.DS_Store' will keep the macOS Spotlight index from syncing to GitHub
Use the following command to open VIM:



```shell
vi .gitignore
```

Use the following VIM commands to insert the necessary text and save the changes:

i enters 'Insert' mode
macOS Spotlight Index

Press the 'Return' or 'Enter' key to move to a new line


```shell
.DS_Store
```

Press the 'Return' or 'Enter' key, to keep the file format/readability consistency

Press the 'esc' key



```shell
:wq
```

Press the 'Return' or 'Enter' key

Use the following command to view your changes:



```shell
git diff
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice the '.gitignore' file in the section, 'Changes not staged for commit'



[Next Section > Stage, Commit, & Push Changes to GitHub](section_9.md "Stage, Commit, & Push Changes to GitHub")

