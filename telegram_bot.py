import argparse
import os
import random
import time
from dotenv import load_dotenv

import telegram


def input_parsing_command_line():
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографии'
                    ' в Телеграмм канал с заданной интенсивностью'
    )
    parser.add_argument(
        '-t',
        help='укажите количество секунд, которое '
             'необходимо для задержки отправления фото',
        default='14400',
        type=int
    )
    parser.add_argument(
        '-id',
        help='Указать id, на который необходимо посылать фотографии',
        default='@SpacePhotobyShukatka'
    )
    args = parser.parse_args()
    return args


def add_photo_paths():
    paths_to_pictures = list()
    for root, directory, photo_filenames in os.walk('images'):
        for picture_name in photo_filenames:
            paths_to_pictures.append(os.path.join(root, picture_name))
    return paths_to_pictures


def publish_images_to_channel(args, token, pictures_paths):
    bot = telegram.Bot(token=token)
    while True:
        random.shuffle(pictures_paths)
        for picture_path in pictures_paths:
            with open(picture_path, 'rb') as pictures:
                bot.send_photo(args.id, pictures)
            time.sleep(args.t)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    args = input_parsing_command_line()
    pictures_paths = add_photo_paths()
    publish_images_to_channel(args, token, pictures_paths)
