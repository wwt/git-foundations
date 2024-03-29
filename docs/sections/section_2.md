# Setup GitHub Authentication

## GitHub Version Control Overview

Git is a distributed Version Control System (VCS) which means any copy of any Git repository can function independently of any other copies of the same Git repository. A Git repository can reside on any single computer, Container, etc. and there are also hosted or managed Git solutions which provide a central location to aggregate changes to version-controlled files.

[GitHub](https://github.com "GitHub.com"){target=_blank} is one example of a hosted or managed Git solution.  These hosted/managed solutions allow many people to run local instances of Git software on their computers and keep their version-controlled files, source code, documentation, etc. in sync with one another.

The remainder of this walkthrough will show you how to:

1. Create a centralized Git repository on GitHub.
2. Synchronize the GitHub repository with our local Git environment (the 'git-foundations' Docker Container).
3. Make changes to the local Git repository.
4. Merge local Git repository changes to GitHub.

---

## GitHub Authentication Overview

Before we setup a GitHub repository, it's a good idea to consider how our local Git environment (the **git-foundations** Container) will authenticate to GitHub during repository synchronization events (clone, pull, push, etc). GitHub supports two types of secure transport, each with their own authentication mechanism(s):

1. HTTPS with basic authentication (username and password) or API key.
2. SSH with public/private key authentication.

    Either choice is just as good as the other. In this environment, we use SSH because it allows us to secure communication without having to manage credentials or API keys. We will first set up SSH authentication before we create a GitHub repository.

    ---

## Generate an SSH Key Pair

1. From the Docker Container prompt, generate an SSH key pair with the following command:

    ```shell
    # Generate a new public/private SSH key pair
    ssh-keygen
    ```

2. After you enter this command and press your ++enter++ or ++"Return"++ key, you may press your ++enter++ or ++"Return"++ key **three more times**, to accept the default storage location for the key and to accept and confirm the default, blank passphrase. Your terminal output will look something like this:

    [![container-ssh-keygen](../images/container-ssh-keygen.png "ssh-keygen")](/git-foundations/images/container-ssh-keygen.png){target=_blank}

    ---

3. Display the new SSH public key file in the terminal with this command:

    ```shell
    # Displays the contents of the new SSH public key file
    cat ~/.ssh/id_rsa.pub
    ```

    !!! caution
        Treat your SSH keys as if they were any other form of credentials and do not share them with anyone.

    [![container-ssh-key](../images/container-ssh-key.png "cat ~/.ssh/id_rsa.pub")](/git-foundations/images/container-ssh-key.png){target=_blank}

4. Copy the full contents of the SSH public key output to your clipboard, including the **ssh-rsa** at the beginning of the file and the **root@_container_id_** at the end of the file. We will share the text from this file with GitHub to establish mutual trust between our Container and GitHub.

---

## Setup GitHub SSH Key Authentication

1. Navigate to [https://github.com/login](https://github.com/login "GitHub Login"){target=_blank}, log in, click the **Profile** icon in the upper-right corner of the window, and choose **Settings**.

    [![github-settings](../images/github-settings.png "GitHub settings access")](/git-foundations/images/github-settings.png){target=_blank}

    ---

2. Click on the **SSH and GPG keys** tab on the left side of the window.

    [![github-profile](../images/github-profile.png "GitHub profile")](/git-foundations/images/github-profile.png){target=_blank}

    ---

3. Click the green, **New SSH key** button

    [![github-ssh-keys](../images/github-ssh-keys.png "GitHub SSH keys")](/git-foundations/images/github-ssh-keys.png){target=_blank}

    ---

4. Provide a title for the SSH key (any title you like is just fine), paste the SSH key file text from your Container into the **Key** field, and click the green, **Add SSH key** button.

    [![github-add-ssh-key](../images/github-add-ssh-key.png "GitHub create SSH key")](/git-foundations/images/github-add-ssh-key.png){target=_blank}

    ---

5. Confirm that GitHub now has a copy of your container's SSH public key.

    [![github-new-ssh-key](../images/github-new-ssh-key.png "GitHub new SSH key")](/git-foundations/images/github-new-ssh-key.png){target=_blank}

---

SSH authentication setup is complete and we are ready to create a new GitHub repository. Click the link below to continue:

[Next Section > Create a GitHub Repository](section_3.md "Create a GitHub Repository")
