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
        default='10',
        type=int
    )
    parser.add_argument(
        '-id',
        help='Указать id, на который необходимо посылать фотографии',
        default=chanel_id
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
                    try:
                        bot.send_photo(args.id, pictures)
                    except:
                        print('Ошибка подключения, повторное подключение через 20 секунд')
                        time.sleep(20)
                time.sleep(args.t)




if __name__ == '__main__':
    load_dotenv()
    chanel_id = os.environ['CHANEL_ID']
    token = os.environ['TELEGRAM_TOKEN']
    args = input_parsing_command_line()
    pictures_paths = add_photo_paths()
    publish_images_to_channel(args, token, pictures_paths)
