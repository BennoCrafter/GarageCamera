import asyncio
from datetime import datetime
from config.config import Config
from scripts.imageManagement.createNewImage import capture_image
from scripts.imageManagement.manageImageStorage import sortImages
from utils.list_files import list_files
from discordBot import send_image
from changeDetector_p.ImageComparator import ImageComparator


configData = Config("config/config.yaml")

path = configData.get_value("general", "imagePath")
image_type = configData.data["general"]["image_data"]["type"]
image_data = configData.data["general"]["image_data"]

def minutes(sec):
    return sec * 60

async def run():
    while True:
        await asyncio.sleep(minutes(2))  # Use asyncio.sleep instead of time.sleep

        new_image_name = datetime.now().strftime("%Y%m%d_%H%M%S")
        prev_image_path = sortImages(list_files(path))[-1]
        capture_image(path, new_image_name, image_type, image_data)
        new_image_path = sortImages(list_files(path))[-1]

        app = ImageComparator()
        similarity = app.similarity(prev_image_path, new_image_path)
        changed = app.changed(prev_image_path, new_image_path)
        if changed:
            await send_image(new_image_path, "AutoDetector")  # Assuming send_image is an asynchronous function

asyncio.run(run())
