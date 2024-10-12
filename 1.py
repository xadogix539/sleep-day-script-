# prompt: vscode sleep day script

import time
import subprocess

def sleep_vscode():
  """
  This function puts VS Code to sleep for a day by closing it and scheduling
  it to reopen after 24 hours.
  """

  # Close VS Code (adapt this command to your OS and how you launch VS Code)
  try:
    subprocess.run(["pkill", "code"], check=True)  # Linux/macOS: Kill the 'code' process
    print("VS Code closed successfully.")
  except subprocess.CalledProcessError:
    print("Error closing VS Code. Make sure it's running and the command is correct.")

  # Schedule VS Code to reopen after 24 hours
  # (This uses the 'sleep' command, which might not be ideal on all systems)
  try:
    subprocess.Popen(["sleep", "86400"]) # Sleep for 86400 seconds (24 hours)
    print("VS Code will reopen in 24 hours.")
  except subprocess.CalledProcessError:
    print("Error scheduling VS Code to reopen.")


if name == "main":
  sleep_vscode()
