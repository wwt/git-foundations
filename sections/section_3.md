# Setup a GitHub Repository



Setup SSH Key Authentication

Setup SSH key authentication with https://github.wwt.com

From your terminal, Check to see if you already have an SSH key with the following command:



```shell
cat ~/.ssh/id_rsa.pub
```



If id_rsa.pub does not exist, generate an ssh key pair with the following command:



```shell
ssh-keygen
```



Use the output of the following command to view the entire contents of your SSH key:



```shell
cat ~/.ssh/id_rsa.pub
```



Copy the entire contents to your clipboard
Log on to https://github.wwt.com (ATC VPN required)
Click on your profile icon in the upper-right corner of the screen
Choose 'Settings' and select the 'SSH and GPG keys' menu option
Click the 'New SSH key' button
Give your key a title and paste the key contents into the 'Key' input box
Click 'Add SSH key'



A best practice is to create/initialize all Git repositories from the central repository
This provides the benefit of automatically generating README and .gitignore files
In our case, that is https://github.wwt.com

Log on to https://github.wwt.com (ATC VPN required)
Click the, 'Start a project' button to create a new repository
Give your new repository a name and a description
The name and description values pre-populate the README file
Choose to make your repository public or private
Tick the box to 'Initialize this repository with a README'
Expand the 'Add a '.gitignore:' dropdown and type or choose 'Python'
Click the 'Create repository' button
Review the '.gitignore' and 'README.md' files in your repository



[Next Section > Create a New Branch in your GitHub Repository](section_4.md "Create a New Branch in your GitHub Repository")

