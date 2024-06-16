# TODO: add config for when to reboot and sleep time

import os
import time
from datetime import datetime

time.sleep(60)

def reboot():
    os.system('sudo reboot')

def should_reboot():
    current_time = datetime.now().time()
    return current_time.hour == 4 and current_time.minute == 0

while True:
    if should_reboot():
        reboot()
    time.sleep(10)
