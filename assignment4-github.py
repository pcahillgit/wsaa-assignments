# This program reads a file from a repository, replaces all instances of "Andrew" with "Paul"
# and then commits those changes and pushes the file back to the repository. 
# Author: Paul Cahill

from github import Github
from config import config as cfg

apikey = cfg["githubkey"] # the config file with my github key is hidden by the gitignore.

g = Github(apikey)
repo = g.get_repo("pcahillgit/wsaa-assignments") # accessing the repo

file_path = "sampletext.txt" # text to be edited
fileInfo = repo.get_contents(file_path)
file_content = fileInfo.decoded_content.decode("utf-8")  # Reading the file contents
updated_content = file_content.replace("Andrew", "Paul") # Replacing Andrew with Paul in the text

# Committing if there are changes
if file_content != updated_content:
    repo.update_file(
        path=file_path,
        message="Ran assignment 4, updated sampletext.txt and replaced 'Andrew' with 'Paul'",
        content=updated_content,
        sha=fileInfo.sha,
    )
    print("Done!")
else:
    print("No changes needed.")

# References:
# Andrew Beatty: Web Services and Applications Lab 5.03 Using Packages.
# Github Guide for Personal Access Tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens