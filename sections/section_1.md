# Hands-On Environment Setup

A WWT-built Docker Image provides a ready-to-use environment for the Git hands-on exercises. You don't need any Docker experience for these exercises. Just make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop "Docker Desktop Download") running on your Windows or macOS computer, and we will walk you through the development environment setup.

It's a two-step process (download and then run) to create the Docker Container we need from the WWT-built Docker Image, but we will accomplish both steps with a single command.

1. Open your terminal/shell program (iTerm, PowerShell, Bash, etc.) and type the following command:

```shell
docker container run -it --name git-foundations wwt01/alpine-network-dev
```

Expect the first run of this command to take a few minutes, while Docker Desktop downloads the Image from Docker Hub. Docker Desktop stores the Image on your computer, so subsequent runs of this command will only take a split second.

You will know your Docker Container environment is ready for the Git hands-on exercises when your terminal prompt reads **/development**:

![docker-container-run](../images/docker-container-run.png)

2. If you aren't sure whether you are at your computer's terminal prompt or the prompt within the Docker Container, you can use this command to double-check:

```shell
cat /etc/*-release
```

3. You are in the Docker Container environment if your output looks like this:

![container-release-info](../images/container-release-info.png)

4. Check the version of Git in the environment with the following command:

```shell
git --version
```

The result of that command should look something like this:

![git-version](../images/git-version.png)

**Here is a quick reference for some other Docker commands which will help you manage your Git hands-on environment:**

```shell
control + d (key sequence) # Stops your Container and returns you to your terminal prompt
docker container start git-foundations # Restarts your Container in the background
docker container attach git-foundations # Returns you to the Container prompt
docker container rm git-foundations # Destroys your container so you can start over
```

Your environment is set up and ready to use! Not to painful so far, right? Click the link below to get started with Git:

[Next Section > Setup GitHub Authentication](section_2.md "Setup GitHub Authentication")
