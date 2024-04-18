from config.config import Config
import requests

config_data = Config("config/config.yaml")

url= None
headers = None

# Set up your HomeAssistant URL and API key
def setupHomeAssistant():
    global url, headers
    url = f"{config_data.get_value('homeAssistant', 'host')}/api/services/script/{config_data.get_value('scriptName')}"
    headers = {
        "Authorization": f"Bearer {config_data.get_value('homeAssistant','homeAssistantToken')}",
        "Content-Type": "application/json",
    }


def sendImageToHomeAssistant():
    response = requests.post(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Script executed successfully!")
    else:
        print("Failed to execute the script:", response.text)

setupHomeAssistant()
