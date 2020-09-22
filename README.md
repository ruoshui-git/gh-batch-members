# Batch invite users to your GitHub Org

1. get a [personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) from github (make sure to grant admin:org scope)

2. make sure you have an .env file with GH_TOKEN (your token) and GH_ORG (the name of the org you want to invite people to) set

3. make sure you have the PyGithub library installed (or use requirements.txt)

4. run the program, argument is the file_name of the emails