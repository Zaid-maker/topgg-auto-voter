"""
This script fetches the latest version of the script from GitHub and votes for the bot on top.gg.
It is designed to be run on a server or a local machine to automate the voting process.
"""
import time
import requests
import os

# Replace with your GitHub repository details
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/Zaid-maker/topgg-auto-voter/main/vote.py'
BOT_ID = '1329035516779167764'
TOP_GG_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEzMjkwMzU1MTY3NzkxNjc3NjQiLCJib3QiOnRydWUsImlhdCI6MTczNzc5MjY4MH0.9Fs6oCVPluSiim2u-FSbZGUyKkfaMYUAxksiDvc6PAo'
SLEEP_DURATION = 12 * 60 * 60  # 12 hours in seconds

def fetch_script():
    """Fetch the latest version of the script from GitHub."""
    try:
        response = requests.get(GITHUB_RAW_URL)
        if response.status_code == 200:
            with open('vote.py', 'w') as file:
                file.write(response.text)
            print("Script updated successfully!")
        else:
            print(f"Failed to fetch script. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching script: {e}")

def vote():
    """Vote for the bot on top.gg."""
    url = f'https://top.gg/api/bots/{BOT_ID}/vote'
    headers = {
        'Authorization': TOP_GG_TOKEN
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Voted successfully!")
    else:
        print(f"Failed to vote. Status code: {response.status_code}")

if __name__ == "__main__":
    while True:
        fetch_script()  # Fetch the latest version of the script
        vote()  # Vote once
        print(f"Waiting for {SLEEP_DURATION / 3600} hours before voting again...")
        time.sleep(SLEEP_DURATION)  # Sleep for 12 hours
