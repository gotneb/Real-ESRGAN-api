import os
from datetime import datetime

# Used by render
TMP_DIR = '/tmp'

def save_image(img, filename: str): 
    path = f'{TMP_DIR}/{filename}.jpg'
    with open(path, 'wb') as f:
        f.write(img.read())
        print("Temp file sucessfully saved!")
    return path


def get_timestamp() -> str:
    return datetime.now().strftime('%Y%m%d_%H%M%S%f')

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} successfully deleted.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied: Unable to delete {file_path}.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

def list_tmp_files():
    tmp_dir = "/tmp"
    files = os.listdir(tmp_dir)
    return files