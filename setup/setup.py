import os
import argparse

class Setup:
    def __init__(self):
        pass
    
    def check_and_create_file(self, target_file, template_file):
        # Check if the target file already exists
        if os.path.exists(target_file):
            print(f"{target_file} already exists.\n")
        else:
            # Read the content from the template file
            with open(template_file, 'r') as f:
                template_content = f.read()

            # Write the template content to the target file
            with open(target_file, 'w') as f:
                f.write(template_content)

            print(f"{target_file} file has been created sucessfully.")

    def delete_folder(self, target_folder):
        # Check if the target file exists
        if os.path.exists(target_folder):
            # Delete the target file
            os.removedirs(target_folder)
            print(f"{target_folder} has been deleted.")
        else:
            print(f"{target_folder} does not exist.")

    def delete_file(self, target_file):
        # Check if the target file exists
        if os.path.exists(target_file):
            # Delete the target file
            os.remove(target_file)
            print(f"{target_file} has been deleted.")
        else:
            print(f"{target_file} does not exist.")

    def create_image_directory(self, image_dir_name):
        if not os.path.exists(image_dir_name):
            os.mkdir(image_dir_name)
            print("Created image directory!")
        else:
            print(f"{image_dir_name} already exists.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Checks and creates the config file from a template.")
    parser.add_argument("--reset", choices=["FORCE"], help="Resets all set up files and folders!")
    
    setup = Setup()

    target_file = "config/config.yaml"       
    template_file = "config/defaultConfig.yaml" 
    image_dir_name = "SavedImages"

    args = parser.parse_args()
    if args.reset == "FORCE":
        print("Resetting everything!")
        setup.delete_folder(image_dir_name)
        setup.delete_file(target_file)
    elif args.reset:
        print("You need to use FORCE to use --reset.")
    else:
        setup.check_and_create_file(target_file, template_file)
        
        setup.create_image_directory(image_dir_name)

    if setup.smth_exists_already:
        print("Some files are already existing!")