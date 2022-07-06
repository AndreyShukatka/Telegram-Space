import datetime
import requests
import argparse
import os
from dotenv import load_dotenv
from downloads_images import download_image

def create_parser():
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии земли из космоса Nasa')
    parser.add_argument('-a', help='Количество фото', default='5', type=int)
    args =parser.parse_args()
    return args

def nasa_epic_photo(nasa_token, epic_photos_amount):
    nasa_url = 'https://api.nasa.gov/EPIC/api/natural/'
    epic_base_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    params = {'api_key': nasa_token}
    response = requests.get(nasa_url,
                            params=params)
    reply = response.json()
    for day in range(epic_photos_amount):
        epic_date = datetime.datetime.fromisoformat(reply[day]['date'])
        url = '{}{}/png/{}.png?api_key={}'.format(epic_base_url,
                                                  epic_date.strftime('%Y/%m/%d'),
                                                  reply[day]['image'],
                                                  nasa_token)
        file_name = 'epic_Nasa_{}.png'.format(datetime.datetime.fromisoformat(reply[day]['date']).strftime('%Y_%m_%d_%H_%M'))
        download_image(url, file_name)

if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    epic_photos_amount = create_parser().a
    nasa_epic_photo(nasa_token, epic_photos_amount)