import os


def list_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    files = os.listdir(directory)

    return files
