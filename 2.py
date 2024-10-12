# prompt: vscode sleep day script

import subprocess
import time
import datetime

def get_current_time():
  """Gets the current time in HH:MM format."""
  now = datetime.datetime.now()
  return now.strftime("%H:%M")

def is_weekday():
  """Checks if it's a weekday."""
  return datetime.datetime.today().weekday() < 5  # Monday is 0, Sunday is 6

def run_vscode_command(command):
  """Runs a command in VS Code using the Code command."""
  try:
    subprocess.run(["code", command], check=True)
  except subprocess.CalledProcessError as e:
    print(f"Error running VS Code command: {e}")

def sleep_vscode_day():
  """Sleeps VS Code on weekdays during the specified time range."""
  while True:
    current_time = get_current_time()

    if is_weekday():
      if "18:00" <= current_time <= "08:00":  # Sleep between 6 PM and 8 AM
          run_vscode_command("--wait")  # Closes VS Code if open
          print(f"VS Code is sleeping. Current time: {current_time}")
          time.sleep(60 * 60)  # Sleep for one hour
      else:
          print(f"VS Code is active. Current time: {current_time}")
          time.sleep(60 * 30)  # Check every 30 minutes
    else:
      print("It's the weekend! VS Code is active.")
      time.sleep(60 * 60)  # Check every hour

if name == "main":
  sleep_vscode_day()
