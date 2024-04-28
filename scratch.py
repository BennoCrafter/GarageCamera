def convert_to_dots(signal_level):
    # Calculate number of dots
    num_dots = min(4, max(1, int(signal_level) // 25))
    # Generate dots representation
    dots = '●' * num_dots + '○' * (4 - num_dots)
    return dots

def extract_signal_level(text, wanted_wlan):
    in_right_wlan_shelf = False
    lines = text.split('\n')
    for line in lines:
        if wanted_wlan in line:
            in_right_wlan_shelf = True
        if in_right_wlan_shelf and "Signal level=" in line:
            signal_level_info = line.split('Signal level=')[1].split('/')[0]
            return int(signal_level_info)
    return None

# Corrected sample text
text = """
lo no wireless extensions.

eth0 no wireless extensions.

wlan0 IEEE 802.11 ESSID:off/any
Mode:Managed Access Point: Not-Associated
Retry short limit:7 RTS thr:off Fragment thr:off
Power Management:on

wlan1 IEEE 802.11bgn ESSID:"BobsWifi" Nickname:"
Mode:Managed Frequency:2.437 GHz Access Point: DC:39:6F:26:7D:58
Bit Rate:87 Mb/s Sensitivity:0/0
Retry:off RTS thr:off Fragment thr:off
Power Management:off
Link Quality=58/100 Signal level=10/100 Noise level=0/100
Rx invalid nwid:0 Rx invalid crypt:0 Rx invalid frag:0
Tx excessive retries:0 Invalid misc:0 Missed beacon:0
"""

signal_level = extract_signal_level(text, "wlan1")

if signal_level is not None:
    print(signal_level)
    print(convert_to_dots(signal_level))
else:
    print("Signal level not found.")