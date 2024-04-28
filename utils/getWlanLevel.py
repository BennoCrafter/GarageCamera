import subprocess
import re

def get_signal_level():
    try:
        # Run iwconfig command and capture the output
        result = subprocess.check_output(["iwconfig", "wlan0"]).decode("utf-8")
        
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

def visualize_signal_level(signal_level):
    if signal_level is None:
        return "Signal level not available"
    
    if signal_level >= -50:
        return "🟢🟢🟢🟢🟢"
    elif signal_level >= -60:
        return "🟢🟢🟢🟢"
    elif signal_level >= -70:
        return "🟢🟢🟢"
    elif signal_level >= -80:
        return "🟢🟢"
    elif signal_level >= -90:
        return "🟢"
    else:
        return "🔴"

# Get signal level
signal_level = get_signal_level()
print(visualize_signal_level(signal_level))
