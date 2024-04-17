from config.config import Config
from utils.list_files import list_files
import os


dataConfig = Config("config/config.yaml")


def isImageStorageFull(images_list):
    return len(images_list) >= dataConfig.get_value("general", "maxImages")


def getOldestImage(images_list):
    return sortImages(images_list)[0]


def manageImageStorage(images_list):
    if isImageStorageFull(images_list):
        file_path = f"{dataConfig.get_value("general", "imagePath")}/{getOldestImage(images_list)}"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")

        return f"Deleted file name: {file_path}"


def sortImages(images_list):
    images_list.sort()
    return images_list

