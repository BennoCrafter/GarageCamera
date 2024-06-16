from scripts.imageManagement.manageImageStorage import sortImages, list_files

def get_latest_images(path, count):
    return sortImages(list_files(path))[len(ex_lis)-count:]
