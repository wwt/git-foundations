# Clone a GitHub Repository to Your Computer



Log on to https://github.wwt.com (ATC VPN required)
Open your Git repository
From the home screen, your repository list is on the left
Click the green 'Clone or download' button
From the expanded menu choose either SSH or HTTPS
Click the 'Copy to clipboard' button to the right of the URL

From your terminal, navigate to the directory in which you want to download your repository
Use the following sample command to choose a directory:



```shell
cd ~/Documents/projects/code
```



Type the command 'git clone' and then paste your repository URL as follows:



```shell
git clone git@github.wwt.com:smithk/myRepo1.git
```



List your directory contents to confirm your repository folder downloaded
Use the following command:



```shell
ls -l
```



In the output, look for a directory name which matches that of your repository

Change to your repository with the following sample command:



```shell
cd myRepo1
```



Look at the contents of your repository directory, including hidden files
Use the following command:



```shell
ls -la
```



View the contents of your 'README.md' file with the following command:



```shell
cat README.md
```



View the contents of the .git directory with the following command:



```shell
ls -l .git
```



View the contents of the repository 'config' file in your .git directory
Use the following command:



```shell
cat .git/config
```



Notice the URL in the '[remote "origin"]' section
This is a good way to check the your central repository target



[Next Section > Manage Local Git Branches](section_6.md "Manage Local Git Branches")

