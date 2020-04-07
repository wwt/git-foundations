# Make Local Git Repository Changes with Atomic Commits



From your terminal, create a simple python script within your local repository
Use the the following command:



```shell
touch myScript.py
```

Confirm your python script file, 'myScript.py' exists with the following command:



```shell
ls -l
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice the 'myScript.py' file in the section, 'Untracked files'

Add the 'myScript.py' file to the staging area with the following command:



```shell
git add myScript.py
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice the 'myScript.py' file in the section, 'Changes to be committed'

Commit the 'myScript.py' file to your local repository with the following command:



```shell
git commit -m "Initial commit of 'myScript.py'"
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice your working branch and that you have no changes to commit

Check your commits which still require a push to GitHub with the following command:



```shell
git cherry -v
```

Notice the SHA1 hash and comment for the commit

**The following requires a text editor and this guide uses VIM**
**You may, alternatively, use the text editor of your choice**

Open the 'myScript.py' file in VIM to insert some python code
Use the following VIM commands to insert the necessary text and save the changes:



```shell
vi myScript.py
```

i enters 'Insert' mode



```python
! /usr/bin/env python
This script says hello and requires Python version 3.x

name = input('What is your name: ')
print(f'\nWell hello, {name}.  It is nice to meet you.\n')
```



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

Notice the 'myScript.py' file in the section, 'Changes not staged for commit'

Add the 'myScript.py' file to the staging area with the following command:



```shell
git add myScript.py
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice the 'myScript.py' file in the section, 'Changes to be committed'

Commit the 'myScript.py' file to your local repository with the following command:



```shell
git commit -m "Added 'input' and 'print' commands to 'myScript.py'"
```

Use the following command to view the status of your local repository:



```shell
git status
```

Notice your working branch and that you have no changes to commit

Check your commits which still require a push to GitHub with the following command:



```shell
git cherry -v
```

Notice the SHA1 hashes and comments for the commits



[Next Section > Stage, Commit, & Push Your New Changes to GitHub](section_10.md "Stage, Commit, & Push Your New Changes to GitHub")

