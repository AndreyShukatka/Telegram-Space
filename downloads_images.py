import os
import pathlib
import requests
from urllib.parse import urlsplit


def download_image(url, file_name, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    folder_name = os.path.join('images', file_name)
    pathlib.Path('images').mkdir(parents=True,
                                 exist_ok=True)
    with open(folder_name, 'wb') as file:
        file.write(response.content)


def extract_file_extension(url):
    path, filename_tail = os.path.split(urlsplit(url).path)
    return os.path.splitext(filename_tail)[-1]
