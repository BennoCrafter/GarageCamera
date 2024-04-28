import subprocess
import re

def get_signal_level(wanted_wlan="wlan0"):
    try:
        # Run iwconfig command and capture the output
        result = subprocess.check_output(["iwconfig", wanted_wlan]).decode("utf-8")
        
        # Use regular expression to find signal level
        match = re.search(r"Signal level=(-\d+)", result)
        
        if match:
            signal_level = int(match.group(1))
            return signal_level
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

