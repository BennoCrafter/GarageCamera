#!/bin/bash

if [ -z "$1" ]; then
    # If no argument, use default
    echo "No argument provided. Using default value."
    python_version="python"
else
    echo "Using: $1"
    python_version="$1"
fi

# Function to handle cleanup
cleanup() {
    echo "Stopping GarageCamera."

    # Kill the background processes
    kill $PID1 $PID2 $PID3

    echo "Stopped GarageCamera."
    exit 1
}

# Trap the SIGINT signal (Ctrl+C) to call the cleanup function
trap cleanup SIGINT

echo "Starting Discord Bot"
sh run_discordBot.sh $python_version &
PID1=$!

echo "Starting Server!"
$python_version server.py &
$PID2=$!

echo "Starting Auto restart!"
$python_version scripts/auto_restart.py
$PID3=$!

echo "Starting Auto change detector!"
$python_version changeDetector/changeDetector.py
$PID3=$!

file_path="assets/ascii_name.txt"

# Print out logo
cat "$file_path"

# Wait for both background processes to finish
wait $PID1
wait $PID2
wait $PID3

echo "Started GarageCamera!"
