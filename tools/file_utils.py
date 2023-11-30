import os

def file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False
