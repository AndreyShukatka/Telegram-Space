from datetime import datetime
import requests
import argparse
import os
from dotenv import load_dotenv
from downloads_images import download_image


def input_parsing_command_line():
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии земли из космоса Nasa'
    )
    parser.add_argument('-с',
                        help='Количество фото',
                        default='5',
                        type=int
                        )
    args = parser.parse_args()
    return args


def download_epic_photo(token_nasa, epic_photos_amount):
    nasa_url = 'https://api.nasa.gov/EPIC/api/natural/'
    epic_base_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    params = {'api_key': token_nasa}
    response = requests.get(nasa_url,
                            params=params)
    response.raise_for_status()
    flight_information = response.json()
    for day in range(epic_photos_amount):
        epic_date = datetime.fromisoformat(flight_information[day]['date'])
        url = '{}{}/png/{}.png'.format(
            epic_base_url,
            epic_date.strftime('%Y/%m/%d'),
            flight_information[day]['image']
        )
        file_name = 'epic_Nasa_{}.png'.format(
            datetime.fromisoformat(
                flight_information[day]['date']
            ).strftime('%Y_%m_%d_%H_%M')
        )
        download_image(url, file_name, params)


if __name__ == '__main__':
    load_dotenv()
    token_nasa = os.environ['TOKEN_NASA']
    epic_photos_amount = input_parsing_command_line().с
    download_epic_photo(token_nasa, epic_photos_amount)
