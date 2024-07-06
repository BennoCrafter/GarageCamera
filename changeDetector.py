import asyncio
from datetime import datetime

from interactions.models.discord import webhooks
from config.config import Config
from scripts.imageManagement.createNewImage import capture_image
from scripts.imageManagement.manageImageStorage import sortImages
from utils.list_files import list_files
from discordBot import send_image
from changeDetector_p.ImageComparator import ImageComparator
import requests
import json


configData = Config("config/config.yaml")

path = configData.get_value("general", "imagePath")
image_type = configData.data["general"]["image_data"]["type"]
image_data = configData.data["general"]["image_data"]
webhook = configData.data["discord"]["webhook"]

async def send_message_to_discord_channel(message: str, webhook_url: str):
    if not webhook_url.startswith("http"):
        print("Invalid webhook URL")
        return
    try:
        # Send POST request to the webhook URL
        response = requests.post(webhook_url, data=json.dumps({"content": message}), headers={"Content-Type": "application/json"})

        if response.status_code != 204:
            print(f"Unexpected status code: {response.status_code}")
        else:
            print("Message sent successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def minutes(sec):
    return sec * 60

async def run():
    while True:
        await asyncio.sleep(60)

        new_image_name = datetime.now().strftime("%Y%m%d_%H%M%S")
        prev_image_path = sortImages(list_files(path))[-1]
        capture_image(path, new_image_name, image_type, image_data)
        new_image_path = sortImages(list_files(path))[-1]

        app = ImageComparator()
        similarity = app.similarity(f"{path}/{prev_image_path}", f"{path}/{new_image_path}")
        changed = app.changed(f"{path}/{prev_image_path}", f"{path}/{new_image_path}")
        if changed:
            print("CHANGED!")
            await send_message_to_discord_channel("latest", webhook)

asyncio.run(run())
