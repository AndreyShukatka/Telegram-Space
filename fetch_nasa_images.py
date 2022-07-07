import argparse
import os
from dotenv import load_dotenv

import requests

from downloads_images import extract_file_extension, download_image


def parsing_input_command_line():
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии космоса Nasa')
    parser.add_argument('-c', help='Количество фото', default='5')
    args =parser.parse_args()
    return args


def download_nasa_image(nasa_token, count):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key':nasa_token, 'count':count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    url = response.json()
    for url_number, data in enumerate(url):
        url = data['url']
        file_name = 'nasa_appod_{}{}'.format(url_number,
                                             extract_file_extension (url))
        download_image(url,
                       file_name)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    count = parsing_input_command_line().c
    download_nasa_image(nasa_token, count)
