#!/bin/bash

if [ -z "$1" ]; then
    # If no argument, use default
    echo "No argument provided. Using default value."
    python_version="python3"
else
    python_version="$1"
fi

# Function to handle cleanup
cleanup() {
    echo "Stopping GarageCamera."

    # Kill the background processes
    kill $PID1 $PID2

    echo "Stopped GarageCamera."
    exit 1
}

# Trap the SIGINT signal (Ctrl+C) to call the cleanup function
trap cleanup SIGINT

echo "Starting Discord Bot"
$arg1 discordBot.py &
PID1=$!

echo "Starting Server!"
$arg1 server.py &
$PID2=$!


file_path="assets/ascii_name.txt"

# Print out logo
cat "$file_path"

# Wait for both background processes to finish
wait $PID1
wait $PID2

echo "Started GarageCamera!"
