import requests
import sys


def get_latest_discord_message(channel_id: str, token: str):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1"

    headers = {
        "Authorization": f"Bot {token}"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data:
                latest_message = data[0]
                return latest_message["content"]
            else:
                print("No messages found.")
        else:
            print(f"Unexpected status code: {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error getting data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:  <channelid> <token>")
        exit(0)
    print(get_latest_discord_message(sys.argv[1], sys.argv[2]))
