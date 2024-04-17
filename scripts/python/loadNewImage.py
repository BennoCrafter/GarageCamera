import requests
from utils.getIp import get_ip_address

flask_server_url = f"http://{get_ip_address()}:5032/update_image"


def loadNewImage(image_url):
    response = requests.post(flask_server_url, data={"image_url": image_url})

    return response.text
