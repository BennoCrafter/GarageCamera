from datetime import datetime

from config.config import Config
from utils.manageImageStorage import manageImageStorage, sortImages
from utils.list_files import list_files
from scripts.python.createNewImage import capture_image
from scripts.python.loadNewImage import loadNewImage
from scripts.python.runHomeAssistantScript import sendImageToHomeAssistant

configData = Config("config/config.yaml")

path = configData.get_value("general", "imagePath")
image_name = datetime.now().strftime("%Y%m%d_%H%M%S")
image_type = configData.data["general"]["image_data"]["type"]
image_data = configData.data["general"]["image_data"]

def update():
    print(capture_image(path, image_name, image_type, image_data))
    file_names = list_files(path)
    print(manageImageStorage(file_names))
    loadNewImage(sortImages(file_names)[-1])
    if configData.get_value("homeAssistant", "useHomeAssistant"): 
        sendImageToHomeAssistant()
    
    return sortImages(list_files(path))[-1]

