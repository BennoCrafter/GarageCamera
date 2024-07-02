#!/bin/bash

# Function to handle cleanup
cleanup() {
    echo "Stopping GarageCamera."

    # Kill the background processes
    kill $PID1 $PID2 $PID3

    echo "Scripts stopped."
    exit 1
}

# Trap the SIGINT signal (Ctrl+C) to call the cleanup function
trap cleanup SIGINT

echo "Starting Discord Bot"
sh run_discordBot.sh my-venv/bin/python3.11&
PID1=$!

echo "Starting Server!"
my-venv/bin/python3.11 server.py &
$PID2=$!

echo "Starting Auto restart!"
my-venv/bin/python3.11 scripts/python/auto_restart.py
$PID3=$!

file_path="assets/ascii_name.txt"

# Print out logo
cat "$file_path"

# Wait for both background processes to finish
wait $PID1
wait $PID2
wait $PID3
