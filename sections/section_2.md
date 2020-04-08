# View & Configure Local Git Settings



From your terminal, view your systemwide Git settings with the following command:

```shell
cat /usr/local/etc/gitconfig
```



Git global settings are user-specific and take precedence over over systemwide settings
View your global Git settings with the following command:



```shell
cat ~/.gitconfig
```



Configure your global Git username and email address with the following commands



```shell
git config --global user.name "Kris Smith"
git config --global user.email "kris.smith@wwt.com"
```



git config --global user.name "Kris Smith"
git config --global user.email "kris.smith@wwt.com"



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





[Next Section > Setup a GitHub Repository](section_3.md "Setup a GitHub Repository")