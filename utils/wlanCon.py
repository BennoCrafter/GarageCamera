import subprocess
import re

def get_wlan_info():
    try:
        # Run iwconfig command and capture output
        result = subprocess.check_output(["iwconfig"], stderr=subprocess.STDOUT).decode('utf-8')
        
        # Extract relevant info using regex
        ssid_match = re.search(r'ESSID:"(.*?)"', result)
        quality_match = re.search(r'Quality=(\d+/\d+)', result)
        return result
               
        if ssid_match and quality_match:
            ssid = ssid_match.group(1)
            quality = quality_match.group(1)
            
            # Convert quality to percentage
            quality_percent = int((int(quality.split('/')[0]) / int(quality.split('/')[1])) * 100)
            
            return {
                'SSID': ssid,
                'Quality': f'{quality_percent}%'
            }
        else:
            return {'Error': 'Could not retrieve WLAN info'}
        
    except subprocess.CalledProcessError as e:
        return {'Error': f'Command execution failed: {e.output.decode("utf-8")}'}

