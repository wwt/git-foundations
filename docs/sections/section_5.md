# Clone a GitHub Repository to Your Computer

Now it's time for us to work with the files in our GitHub repository, and we start by copying or **cloning** the repository to our local Docker Container environment.

---

## Copy The Repository SSH URL

We mentioned GitHub supports two transports, HTTPS and SSH. GitHub defaults to HTTPS transport, which adds an extra step (entering your username and password) to the cloning process.  The SSH keys we setup in [Section 2](section_2.md "Setup GitHub Authentication") allow our Docker Container and GitHub to communicate with each other without repeatedly prompting for credentials.

1. Click the green **Clone** button and notice that GitHub displays an HTTPS URL. Click the **SSH** link to change the display to an SSH URL.

    [![github-clone-https](../images/github-clone-https.png "Clone repository button default transport")](/git-foundations/images/github-clone-https.png){target=_blank}

    ---

2. Click the **Copy** icon, just to the right of the SSH URL, to store the URL on your clipboard.

    [![github-clone-ssh](../images/github-clone-ssh.png "Copy repository SSH URL")](/git-foundations/images/github-clone-ssh.png){target=_blank}

---

## Clone & Review The Repository

1. Return to your Docker Container prompt, type the command `git clone`, paste **_your repository URL_**, as shown in the example below (your repository URL will be different than the example in the in the following code block), and press your ++enter++ or ++"Return"++ key:

    ```shell
    # Download a new copy of a GitHub repository to a local system (our Container, in this case)
    git clone git@github.com:your-repository-url/git-repo-1.git
    ```

    !!! attention
        You will likely see a prompt which asks you to confirm the authenticity of GitHub's SSH RSA fingerprint. You may safely type `yes` and press ++enter++ or ++"Return"++ to continue.

    The result of the `git clone` command should look something like this:

    [![git-clone](../images/git-clone.png "Clone GitHub repository")](/git-foundations/images/git-clone.png){target=_blank}

    ---

2. List your directory contents to view your repository folder, **git-repo-1**, with the following command:

    ```shell
    # List the contents of the current directory in long format
    ls -l
    ```

    [![container-root-ls](../images/container-root-ls.png "List directory contents")](/git-foundations/images/container-root-ls.png){target=_blank}

    ---

3. Change to your repository directory and display your current working directory with the following commands:

    ```shell
    # Change the current working directory from development to /development/git-repo-1
    cd git-repo-1
    ```

    ```shell
    # Display the current working directory
    pwd
    ```

    [![container-cd-repo](../images/container-cd-repo.png "Change to the respository directory")](/git-foundations/images/container-cd-repo.png){target=_blank}

    ---

4. Let's take a quick look at the contents of your repository directory, including the hidden files, with the following command.

    ```shell
    # List the contents of the current directory, including hidden files, in long format
    ls -la
    ```

    [![container-repo-ls](../images/container-repo-ls.png "List all repository files")](/git-foundations/images/container-repo-ls.png){target=_blank}

5. Notice that both of the files in your GitHub repository (**.gitignore** and **README.md**) are now in our Docker Container.

    ---

6. View the contents of the **README.md** file with the following command:

    ```shell
    # Display the contents of the file 'README.md'
    cat README.md
    ```

    [![container-cat-readme](../images/container-cat-readme.png "Display the README.md file contents")](/git-foundations/images/container-cat-readme.png){target=_blank}

    ---

7. There is one item in our repository directory which isn't in our GitHub repository, the **.git** directory. This directory contains all of the details about your local repository and you should rarely, if ever, have to interact with these files. Just to see what the contents of this folder look like, use the following command:

    ```shell
    # List the contents of the .git directory in long format
    ls -l .git
    ```

    [![container-ls-git](../images/container-ls-git.png "List the contents of the .git directory")](/git-foundations/images/container-ls-git.png){target=_blank}

---

We now have a copy of our GitHub repository in our Docker environment. Before we make changes to our local copy of the Git repository, we need to configure a few local Git settings. Click the link below to continue:

[Next Section > View & Configure Local Git Settings on Your Computer](section_6.md "View & Configure Local Git Settings on Your Computer")
