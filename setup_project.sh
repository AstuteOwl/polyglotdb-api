#!/bin/bash

[[ $_ != $0 ]] || printf "\n\t**Protip: Run script with $ source $0 for the virtualenv to persist\n\n"

#The purpose of this script is to setup virtualenv for the project.
#Check for pip
echo "Checking for pip installation..."
hash pip 2>/dev/null || { echo >&2 "pip is required to setup the virtualenv. Install pip and try again."; exit 1; }

#Check for virtualenv
echo "Checking for virtualen installation..."
if ! hash virtualenv 2>/dev/null; then
    echo "virtualenv not installed, installing it now..."
    pip install virtualenv
fi

#if the virtualenv director exists just run the install
echo "Virtual environment directory not found. Creating it now..."
if [ ! -d "apienv" ]; then
    virtualenv apienv
fi

#activate the local virtualenv
echo "Activating virtualenv for project now..."
source apienv/bin/activate

echo "Installing dependencies for project now..."
pip install -r requirements.txt
