import os
import pathlib

import requests


def download_image (url, file_name):
    img = requests.get(url)
    img.raise_for_status()
    folder_name = 'images/{}'.format(file_name)
    pathlib.Path('images').mkdir(parents=True,
                                 exist_ok=True)
    with open(folder_name, 'wb') as file:
        file.write(img.content)


def extract_file_extension (url):
    link, extension = os.path.splitext(url)
    return extension