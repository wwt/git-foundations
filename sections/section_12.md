# Review The Pull Request Impact to Your Local Git Repository

The GitHub repository has a new version of the **main** branch, but our local repository isn't aware of the change yet. Before we make new changes to our local repository, let's get it back in sync with GitHub and clean up the branch (**branch3**) which is no longer in GitHub.

## **Pull Changes from GitHub**

1. From your terminal, pull the latest changes from GitHub to your local repository with the following command:

```shell
# Download and merge changes from the remote repository to the local repository
git pull
```

![git-pull-branch3](../images/git-pull-branch3.png)

2. Notice the last two lines of the output which indicate Git attempted to pull changes from GitHub and merge those changes with **branch3** in the local repository.

   - However, Git was unable to locate **branch3** in GitHub because, of course, we deleted **branch3** in GitHub after merging our **pull request**.

---

3. List your local branches with the following command:

```shell
# Display all local git branches
git branch
```

![git-branch-5](../images/git-branch-5.png)

4. Notice **branch3** remains in your local repository.

---

5. Change your working branch to **main** with the following command:

```shell
# Switch the working branch from 'branch3' to 'main'
git checkout main
```

![git-checkout-main](../images/git-checkout-main.png)

6. Notice the message which indicates the local branch **main** is behind the GitHub **main** branch (**origin/main**) by three commits and can be fast-forwarded.

---

7. Merge the GitHub **main** branch with your local repository **main** branch using the following command:

```shell
# Download and merge changes from the remote repository to the local repository
git pull
```

![git-pull-main](../images/git-pull-main.png)

8. Notice the output which indicates the file changes and insertions.

---

9. Since our local **main** branch now in sync with the latest copy of the GitHub repository, we no longer need our local copy of **branch3**. Remove **branch3** from the local repository with the following command:

```shell
# Delete the local branch named 'branch3'
git branch -d branch3
```

![git-branch-d-branch3](../images/git-branch-d-branch3.png)

---

10. Confirm **branch3** no longer exists with the following command:

```shell
# Display all local git branches
git branch
```

![git-branch-7](../images/git-branch-7.png)

11. Notice that **main** is now the only branch in your local repository.

:star: You did it! You:

:white_check_mark: Set up a new GitHub repository.
:white_check_mark: Set up a local Git environment in a Docker Container.
:white_check_mark: Managed local Git branches.
:white_check_mark: Staged and committed local repository changes.
:white_check_mark: Pushed branches and changes from your local Git environment to GitHub.
:white_check_mark: Merged changes in GitHub with a pull request.
:white_check_mark: Synchronized merged GitHub changes to your local Git environment.

Click the link below to go to the last section and finish things up:

[Next Section > Clone Another Repository, Make Changes, and Create a New Pull Request](section_13.md "Clone Another Repository, Make Changes, and Create a New Pull Request")
