import datetime
import os
import pathlib
from dotenv import load_dotenv

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


def fetch_spacex_last_launch():
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(spacex_url)
    response.raise_for_status()
    response_data=response.json()['links']['flickr']['original']
    for url_number, url in enumerate(response_data):
        file_name = 'spacex{}{}'.format(url_number,
                                        extract_file_extension (url))
        download_image(url,
                       file_name)

def nasa_download_image(nasa_token):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key':nasa_token, 'count':'20'}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    url = response.json()
    for url_number, data in enumerate(url):
        url = data['url']
        file_name = 'nasa_appod_{}{}'.format(url_number,
                                             extract_file_extension (url))
        download_image(url,
                       file_name)


def nasa_epic_photo(nasa_token):
    nasa_url = 'https://api.nasa.gov/EPIC/api/natural/'
    epic_base_url = 'https://api.nasa.gov/EPIC/archive/natural/'
    epic_photos_amount = 7
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

def main():
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    fetch_spacex_last_launch()
    nasa_download_image(nasa_token)
    nasa_epic_photo(nasa_token)


if __name__ == '__main__':
    main()
