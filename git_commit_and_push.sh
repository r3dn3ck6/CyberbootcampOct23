#!/bin/bash

# Add all changes to staging area
git add .

# Prompt for commit message
read -p "Enter commit message: " commit_message

# Commit changes with the provided message
git commit -m "$commit_message"

# Push changes to the remote repository
git push

# This script performs the following steps:

# Adds all changes to the staging area using git add . (this assumes you want to add all changes; you can modify it to add specific files if needed).
# Prompts the user to enter a commit message.
# Commits the changes with the provided commit message using git commit -m "$commit_message".
# Pushes the committed changes to the remote repository using git push.
# Remember to make the script executable using the following command:

chmod +x git_commit_and_push.sh

# To execute the script,run:

./git_commit_and_push.sh
files

# Ensure that you are in the correct Git repository directory when executing this script, and use it responsibly after reviewing the changes being committed.