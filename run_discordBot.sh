#!/bin/bash

get_signal_level() {
    local wanted_wlan=$1
    local result

    # Run iwconfig command and capture the output
    result=$(iwconfig "$wanted_wlan" 2>/dev/null)

    if [[ $? -ne 0 ]]; then
        echo "Error: Unable to get information for $wanted_wlan"
        return 1
    fi

    # Use grep and awk to find signal level
    signal_level=$(echo "$result" | grep -oP 'Signal level=\K[-0-9]+')

    if [[ -n $signal_level ]]; then
        echo "$signal_level"
    else
        echo "No signal level found"
    fi
}

if [ -z "$1" ]; then
    # If no argument, use default
    echo "No argument provided. Using default value."
    python_version="python"
else
    python_version="$1"
fi


reached_wlan_level=false
min_signal_level=15
restart_time=10  # time in seconds to wait before retrying
wanted_wlan="wlan1"

call_script() {
    $python_version discordBot.py
    echo "Error! Discord bot exited!"
}

while true
do
    while [[ $reached_wlan_level == false ]]; do
        signal_level=$(get_signal_level "$wanted_wlan")

        if [[ $? -ne 0 ]]; then
            echo "Failed to get signal level. Trying in $restart_time seconds again."
            sleep $restart_time
            continue
        fi

        if [[ $signal_level -ge $min_signal_level ]]; then
            reached_wlan_level=true
            echo "Reached desired signal level: $signal_level"
            call_script
            reached_wlan_level=false
            break
        else
            echo "Failed to connect to wlan. Trying in $restart_time seconds again."
            sleep $restart_time
        fi
    done
done
