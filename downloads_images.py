import os
import pathlib
import urllib
import requests


def download_image(url, file_name, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    folder_name = 'images/{}'.format(file_name)
    pathlib.Path('images').mkdir(parents=True,
                                 exist_ok=True)
    with open(folder_name, 'wb') as file:
        file.write(response.content)


def extract_file_extension(url):
    link, extension = os.path.splitext(url)
    file_extension = urllib.parse.urlsplit(extension).path
    return file_extension
