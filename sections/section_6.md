# Manage Local Git Branches



From your terminal, use the following command to list your local branches:

```shell
git branch
```



Notice that only the 'master' branch cloned to your local repository
This is the correct behavior; other branches do not clone to local repositories

Use the following command to list all branches, local and remote:

```shell
git branch -a
```



Notice your local 'master' branch plus the remote branches

Create a new, local branch:



```shell
git branch BranchX
```



Use the following command to, again, list your local branches:



```shell
git branch
```



Notice your new branch
Notice the highlight of and asterisk next to the 'master' branch
The highlight and asterisk indicate your current, working branch

Use the following command to, again, list all branches, local and remote:



```shell
git branch -a
```



Notice the new local branch does not exist as a remote branch

Switch to your new branch with the following command:



```shell
git checkout Branch2
```



Use the following command to, again, list your local branches:



```shell
git branch
```



Notice the highlight of and asterisk your new branch

Use the following command to simultaneously create and switch to a new branch



```shell
git checkout -b Branch3
```



Use the following command to, again, list your local branches:



```shell
git branch
```



Notice the highlight of and asterisk your new branch

Use the following command to delete one of your branches:



```shell
git branch -d BranchX
```



Use the following command to, again, list your local branches:



```shell
git branch
```



Notice the removal of your branch



[Next Section > Make Local Git Repository Changes](section_7.md "Make Local Git Repository Changes")

