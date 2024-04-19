import subprocess
import os 
from config.config import Config
from utils.checkOs import is_raspberry_pi


configData = Config("config/config.yaml")
def update_project_from_git():
    project_path = os.path.dirname(os.path.realpath(__file__))
    try:
        if is_raspberry_pi():
            os.chdir(project_path)
        else:
            subprocess.run(['cd', project_path], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Failed to change directory to {project_path}: {e}")
        return f"Failed to change directory to {project_path}: {e}"

    # Pull changes from the Git repository
    try:
        subprocess.run(['git', 'pull'], check=True)
        print("Project successfully updated from the Git repository!")
        if configData.get_value("general", "rebootAfterUpdate"):
            print("Rebooting now!")
            if is_raspberry_pi():
                subprocess.run(['reboot'], check=True)
            else:
                print("Failed rebooting!") 

    except subprocess.CalledProcessError as e:
        print(f"Failed to update project from Git repository: {e}")
