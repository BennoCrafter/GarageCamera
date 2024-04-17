from flask import Flask, send_file, request, redirect, render_template
import os
from utils.getIp import get_ip_address
from scripts.python.update import update
from config.config import Config
from utils.autoUpdateProject import update_project_from_git
from waitress import serve

app = Flask(__name__)

ip_address = get_ip_address()
IMAGE_URL = "assets/startup.jpeg"
configData = Config("config.json")


@app.route('/')
def index():
    return redirect("/home")

@app.route('/home')
def home():
    return "Home"

@app.route('/raw_image')
def get_raw_image():
    return send_file(IMAGE_URL, mimetype='image/jpeg')


@app.route('/update_image', methods=['POST'])
def change_image():
    new_image_url = request.form.get('image_url')
    if new_image_url:
        global IMAGE_URL
        IMAGE_URL = new_image_url
        return "Picture changed successfully!"
    else:
        return "No image URL provided."


@app.route('/refresh')
def refresh_image():
    update()
    if configData.get_value("siteForwarding"):
        return redirect("/home")
    else:
        return "Refresh triggerd sucessfully."
    
@app.route('/update_project')
def update_project():
    lel = update_project_from_git()
    if lel == None:
        return "Sucessss"
    return lel

if __name__ == '__main__':
    # print(f"\n\nIP Address:\n\n {ip_address}\n")

    serve(app, host='0.0.0.0', port="5032")