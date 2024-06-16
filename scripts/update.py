from datetime import datetime
from config.config import Config

from utils.list_files import list_files
from scripts.runHomeAssistantScript import sendImageToHomeAssistant

from scripts.imageManagement.manageImageStorage import manageImageStorage, sortImages
from scripts.imageManagement.createNewImage import capture_image
from scripts.imageManagement.loadNewImage import loadNewImage

configData = Config("config/config.yaml")

path = configData.get_value("general", "imagePath")
image_type = configData.data["general"]["image_data"]["type"]
image_data = configData.data["general"]["image_data"]

def update():
    # set image name to time
    image_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(capture_image(path, image_name, image_type, image_data))
    file_names = list_files(path)
    print(manageImageStorage(file_names))
    loadNewImage(sortImages(file_names)[-1])
    if configData.get_value("homeAssistant", "useHomeAssistant"):
        sendImageToHomeAssistant()

    return sortImages(list_files(path))[-1]
