import time
from utils.checkOs import is_raspberry_pi
import os


# todo move var
valid_image_formats = ["jpeg", "png"]


def capture_image(image_path, image_name, image_type, img_data):
    if is_raspberry_pi():
        capture_image_pi(image_path, image_name, image_type, img_data)
    else:
        capture_image_cv(image_path, image_name, image_type)


def capture_image_cv(image_path, image_name, image_type):
    import cv2
    cap = cv2.VideoCapture(0)
    time.sleep(5)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Error: Failed to capture image")
        return

    filename = f"{image_path}/{image_name}"

    # Save the captured frame as an image with higher quality (compression=90)
    cv2.imwrite(filename, frame)
    return f"Image saved as {filename}"


def capture_image_pi(image_path, image_name, image_type, img_data):
    if image_type in valid_image_formats:
        command = f"fswebcam {image_path}/{image_name} --scale {str(img_data['width'])}x{str(img_data['height'])} --{image_type}"
    else:
        command = f"fswebcam {image_path}/{image_name} --scale {str(img_data['width'])}x{str(img_data['height'])} --jpeg"
        print(f"Capture image: Error: Wrong image type. '{image_type}' is not a valid format. Using jpeg instead.")

    # Execute the command using os.system()
    try:
        os.system(command)
        return f"Image saved as {image_name}"
    except Exception as e:
        return "Error capturing picture. You have installed fswebcam?"