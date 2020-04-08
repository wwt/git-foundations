# Clone a GitHub Repository to Your Computer



1. 

![github-clone-https](../images/github-clone-https.png)



2. 

![github-clone-ssh](../images/github-clone-ssh.png)







Log on to https://github.wwt.com (ATC VPN required)
Open your Git repository
From the home screen, your repository list is on the left
Click the green 'Clone or download' button
From the expanded menu choose either SSH or HTTPS
Click the 'Copy to clipboard' button to the right of the URL

1. From your terminal, type the command **git clone** and then paste your repository URL as follows:


```shell
git clone git@github.wwt.com:smithk/myRepo1.git
```



2. List your directory contents to confirm your repository folder downloaded
   Use the following command:

```shell
ls -l
```



3. In the output, look for a directory name which matches that of your repository.  Change to your repository with the following sample command:

```shell
cd myRepo1
```



4. Look at the contents of your repository directory, including hidden files
   Use the following command:

```shell
ls -la
```



5. View the contents of your 'README.md' file with the following command:

```shell
cat README.md
```



6. View the contents of the .git directory with the following command:

```shell
ls -l .git
```



7. View the contents of the repository 'config' file in your .git directory
   Use the following command:

```shell
cat .git/config
```



Notice the URL in the '[remote "origin"]' section
This is one way to check the your central repository target



[Next Section > View & Configure Local Git Settings](section_6.md "View & Configure Local Git Settings")

