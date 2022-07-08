import requests
import argparse
from downloads_images import extract_file_extension, download_image


def input_parsing_command_line():
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии запуска SpaceX'
    )
    parser.add_argument('-id', help='Введите id запуска', default='latest')
    args = parser.parse_args()
    return args


def fetch_spacex_last_launch(space_id):
    spacex_url = 'https://api.spacexdata.com/v3/launches/'
    params = {'flight_number': space_id}
    response = requests.get(spacex_url, params=params)
    response.raise_for_status()
    response_data = response.json()[0]['links']['flickr_images']
    flight_number = response.json()[0]['flight_number']
    for url_number, url in enumerate(response_data):
        file_name = 'spacex{}_{}{}'.format(
            flight_number,
            url_number,
            extract_file_extension(url)
        )
        download_image(url,
                       file_name,
                       params)


if __name__ == '__main__':
    space_id = input_parsing_command_line().id
    fetch_spacex_last_launch(space_id)
