#!/bin/bash

if [ -z "$1" ]; then
    # If no argument, use default
    echo "No argument provided. Using default value."
    version=""
else
    version="$1"
fi


echo "Installing python requirements"
pip${version} install -r assets/requirements.txt

echo "\nInstalling fswebcam module"
sudo apt-get install fswebcam

echo "\nCreating executable"
chmod +x run.sh

echo "\nRunning setup.py script"
python${version} setup/setup.py

exit 0