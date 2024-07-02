#!/bin/bash


if [ -z "$1" ]; then
    # If no argument, use default
    echo "No argument provided. Using default value."
    python_version="python"
else
    python_version="$1"
fi

restart_time=10

call_script() {
    $python_version discordBot.py
    echo "Fatal Error! Couldn't handle error in the code. Discord bot exited! Restarting in $restart_time seconds..."
}

while true
do
    call_script
    sleep $restart_time
done
