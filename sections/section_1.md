# Hands-On Environment Setup

A WWT-built Docker Image provides a ready-to-use environment for the Git hands-on excercises.  You don't need any Docker experience for these exercises.  Just make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop "Docker Desktop Download") running on your Windows or macOS computer and we will walk you through the environment setup.

It's a two step process (download and then run) to create the Docker Container we need from the WWT-built Docker Image but we will accomplish both steps with a single command.

**Open your favorite terminal/shell program (iTerm, PowerShell, Bash, etc.) and type the following command:**

```shell
docker container run -it --name git-foundations wwt01/alpine-network-dev
```



Expect the first run of this command to take a few minutes, while Docker Desktop downloads the Image from Docker Hub.  Docker Desktop stores the Image on your computer so subsequent runs of this command will only take a split second.

You will know your Docker Container environment is ready for the Git hands-on exercises when your terminal prompt looks like this:

// Insert screenshot



**Check the version of Git in the environment with the following command:**

```shell
git --version
```



The result of that command should look something like this:

// Insert screenshot



**Here is a quick reference for some other Docker commands which will help you manage your Git hands-on environment:**

```shell
control + d (key sequence) # Stops your Container and returns you to your terminal prompt
docker container start git-foundations # Restarts your Container in the background
docker container attach git-foundations # Returns you to the Container prompt
docker container rm git-foundations # Destroys your container so you can start over
```



Your environment is setup and ready to use!  Not to painful so far, right?  Click the link below to get started with Git:

[Next Section > View & Configure Local Git Settings](section_2.md "View & Configure Local Git Settings")

