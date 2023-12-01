import os

def file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

