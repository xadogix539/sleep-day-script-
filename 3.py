# prompt: vscode website sleep day script

import time
import pyautogui

# Set the time interval for the script to run (in seconds)
interval = 3600  # 1 hour

while True:
    # Move the mouse slightly to prevent the screen from locking
    pyautogui.moveRel(10, 0, duration=0.25)
    pyautogui.moveRel(-10, 0, duration=0.25)

    # Wait for the specified interval
    time.sleep(interval)
