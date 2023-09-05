#!/bin/bash

# OVERVIEW
# This script sets username and email address in Git config and installs nbstripout as default as a pre-commit hook for all repos.
# This file should be copied to a non-version controlled location and the PARAMETERS updated. 
# Its ownership should be changed using chmod 777 <filename.sh> (This allows it to be run)
# It can then be run using ./<filename.sh> and should be done on every startup.
# A longer term solution is being sought.

# PARAMETERS
YOUR_USER_NAME="Firstname Lastname"
YOUR_DHSC_EMAIL_ADDRESS="YOUR_EMAIL@XX.co.uk"

# Stops execution of this script if there are errors
set -e

sudo -u ec2-user -i <<EOF
git config --global user.name "$YOUR_USER_NAME"
git config --global user.email "$YOUR_DHSC_EMAIL_ADDRESS"

# Creates a directory to store git settings
mkdir -p ~/.config/git  # This folder may not exist

# Installs nbstripout
pip install nbstripout pre-commit black

# Enforces nbstripout for all repos on this VM/instance
nbstripout --install --global --attributes=~/.config/git/attributes

# Install pre-commit into this repo
cd SageMaker/cookiecutter-repo_name
pre-commit install

# Check variables set
echo "The next three lines are a check that this has been implement correctly and should have your name, email and a reference to nbstripout"
git config user.name
git config user.email
git config filter.nbstripout.clean
EOF
