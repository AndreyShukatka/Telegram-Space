import argparse
import os
from dotenv import load_dotenv
import requests
from downloads_images import extract_file_extension, download_image


def input_parsing_command_line():
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии космоса Nasa'
    )
    parser.add_argument(
        '-c',
        help='Количество фото',
        default='5'
    )
    args = parser.parse_args()
    return args


def nasa_download_image(nasa_token, count):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    photo_information = response.json()
    for number, data in enumerate(photo_information):
        url = data['url']
        file_name = 'nasa_appod_{}{}'.format(
            number,
            extract_file_extension(url)
        )
        download_image(
            url,
            file_name,
            params
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    count = input_parsing_command_line().c
    nasa_download_image(nasa_token, count)
