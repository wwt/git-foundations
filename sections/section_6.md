# View & Configure Local Git Settings

Git requires very little information before we can start to make local repository changes and then push those changes to GitHub.  We just need to tell Git the **name** and **email address** of the person contributing changes, as a way to help all repository viewers and contributors understand who contributes what.  We provide Git our **name** and **email address** in one or more configuration files.

Git has several tiers of configuration files and we will explore the three most common:

- **System-wide** - ***/etc/gitconfig***
  - Applies to all repositories for *all* users on a system.
- **Global** - ***~/.gitconfig***
  - Applies to all repositories for a *single* user on a system.
  - Supersedes any overlapping **system-wide** settings.
- **Local repository** - ***repository_folder/.git/config***
  - Applies to a single repository.
  - Supercedes any overlapping **global** and **system-wide** settings.



**Edit System-Wide Git Configuration**

1. Configure a **system-wide** Git **username** and **email address** with the following commands:


```shell
git config --system user.name "Your Name - System"
git config --system user.email "system@your_domain.com"
```



2. Review the **system-wide** configuration file with the following command:

```shell
cat /etc/gitconfig
```





Notice the two configuration settings you just applied.



3. Configure a **Global** Git **username** and **email address** with the following commands:

```shell
git config --global user.name "Your Name - Global"
git config --global user.email "your.email@your_domain.com"
```



2. Review the **global** configuration file with the following command:

```shell
cat ~/.gitconfig
```



View the contents of the repository 'config' file in your .git directory
Use the following command:

```shell
cat .git/config
```



Notice the URL in the '[remote "origin"]' section
This is one way to check the your central repository target



In this section we will explore the various local Git configuration settings and some 



From your terminal, view your systemwide Git settings with the following command:

```shell
cat /usr/local/etc/gitconfig
```



Git global settings are user-specific and take precedence over over systemwide settings
View your global Git settings with the following command:

```shell
cat ~/.gitconfig
```



Configure your global Git username and email address with the following commands:

```shell
git config --global user.name "Kris Smith"
git config --global user.email "kris.smith@wwt.com"
```



Review the updated global Git configuration settings

```shell
cat ~/.gitconfig
```



Every Git repository on your computer has its own configuration settings
To view repository-specific settings use the following command:



```shell
cat .git/config
```



Within any Git repository on your computer, you may configure specific settings
Repository-specific settings take precedence over global and systemwide settings
From the Git repository directory, you can use commands like these:



```shell
git config user.name "Kris Smith"
git config user.email "kris.smith@wwt.com"
```



[Next Section > Manage Local Git Branches](section_7.md "Manage Local Git Branches")