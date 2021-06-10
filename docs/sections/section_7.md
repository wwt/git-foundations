# Manage Local Git Branches

Our Git environment is ready for us to start work on our repository. Typically, especially on a project with many contributors, Git branches allow each contributor to have as many non-overlapping copies of the repository as they need, to make and manage their changes. We will do some basic work with branches, so we can, later, contribute our changes to the **main** branch of the GitHub repository.

---

## View, Create, Switch To, & Remove Branches

1. From the Docker Container prompt, list your _local_ Git branches with the following command:

    ```shell
    # Display all local git branches
    git branch
    ```

    [![git-branch-1](../images/git-branch-1.png "Display local git branches")](/git-foundations/images/git-branch-1.png){target=_blank}

2. Notice that only the **main** branch cloned to your local Git repository from GitHub.

    - This is normal/expected behavior; only the **main** branch clones from GitHub because other branches (like the **branch1** branch we created in GitHub) are likely other peoples' work in-progress and any work we do should originate from the **main** branch of the GitHub repository.
    - The asterisk to the left of **"main"** indicates that **main** is our current, working branch.

    ---

3. List all Git repository branches, local _and_ remote, with the following command:

    ```shell
    # Display all local and remote repository git branches
    git branch -a
    ```

    [![git-branch-a-1](../images/git-branch-a-1.png "Display all local and remote git repository branches")](/git-foundations/images/git-branch-a-1.png){target=_blank}

4. Notice how we see:
    - A **main** branch.
        - This is our local copy of the **main** branch.
    - An **origin/main** branch alias (for **remotes/origin/HEAD**).
        - This is the copy of the **main** branch in Github.
    - And an **origin/remotes/branch1** branch.
        - This is the copy of the **branch1** branch in Github.

    !!! info
        **Origin** is how our local repository refers to GitHub so **origin/main** represents the **main** branch on GitHub.

    ---

5. Create a new, local branch named **branch2**, with the following command:

    ```shell
    # Create a new local git branch named 'branch2'
    git branch branch2
    ```

    [![git-branch-branch2](../images/git-branch-branch2.png "Create a new local branch named 'branch2'")](/git-foundations/images/git-branch-branch2.png){target=_blank}

    ---

6. List your local branches again with the following command:

    ```shell
    # Display all local git branches
    git branch
    ```

    [![git-branch-2](../images/git-branch-2.png "Display all local git branches")](/git-foundations/images/git-branch-2.png){target=_blank}

7. Notice your new branch, **branch2** and also that the asterisk next to **main** tells us that, even though we just created **branch2**, our working branch is still **main**.

    ---

8. Again, list all branches, local and remote, with the following command:

    ```shell
    # Display all local and remote repository git branches
    git branch -a
    ```

    [![git-branch-a-2](../images/git-branch-a-2.png "Display all local and remote git repository branches")](/git-foundations/images/git-branch-a-2.png){target=_blank}

9. Notice that **branch2** does not exist as a remote branch in GitHub. This is normal behavior and something we will work with later on.

    ---

10. Switch your working branch to **branch2** with the following command:

    ```shell
    # Switch the working branch from 'main' to 'branch2'
    git checkout branch2
    ```

    [![git-checkout-branch2](../images/git-checkout-branch2.png "Switch to branch 'branch2'")](/git-foundations/images/git-checkout-branch2.png){target=_blank}

    ---

11. Verify your current, working branch with the following command:

    ```shell
    # Display all local git branches
    git branch
    ```

    [![git-branch-3](../images/git-branch-3.png "Display local git branches")](/git-foundations/images/git-branch-3.png){target=_blank}

12. Notice the asterisk next to **branch2** which indicates that **branch2** is our current, working branch.

    ---

13. Create and simultaneously switch to a new branch with the following command:

    ```shell
    # Create and switch the working branch to a new local git branch named 'branch3'
    git checkout -b branch3
    ```

    [![git-checkout-b-branch3](../images/git-checkout-b-branch3.png "Create and switch to a new branch named 'branch3'")](/git-foundations/images/git-checkout-b-branch3.png){target=_blank}

14. The `git checkout` command allows you to switch between branches.
    - The `git checkout` command with the `-b` flag creates a new branch _and_ switches to the new branch.

    !!! tip
        The `git checkout -b branch_name` command is just a shortcut for the `git branch branch_name` command followed by `git checkout branch_name` command.

    ---

15. List your local branches again with the following command:

    ```shell
    # Display all local git branches
    git branch
    ```

    [![git-branch-4](../images/git-branch-4.png "Display local git branches")](/git-foundations/images/git-branch-4.png){target=_blank}

16. Notice the asterisk next to **branch3** which indicates that **branch3** is our current, working branch.

    ---

17. For our purpose, we only need one branch, in addition to the **main** branch, so we can remove one of our new branches with the following command:

    ```shell
    # Delete the local branch named 'branch2'
    git branch -d branch2
    ```

    !!! tip
        Git will not allow you to delete your current, working branch.

    [![git-branch-d-branch2](../images/git-branch-d-branch2.png "Delete branch 'branch2'")](/git-foundations/images/git-branch-d-branch2.png){target=_blank}

    ---

18. Review your local branches with the following command:

    ```shell
    # Display all local git branches
    git branch
    ```

    [![git-branch-5](../images/git-branch-5.png "Display local git branches")](/git-foundations/images/git-branch-5.png){target=_blank}

19. Notice that **branch2** is no longer available.

---

We can make some changes to our repository within **branch3** without impacting the **main** branch. Click the link below to continue:

[Next Section > Make Local Git Repository Changes](section_8.md "Make Local Git Repository Changes")
