import argparse
import os
import random
import time
from dotenv import load_dotenv

import telegram


def create_parser():
    parser = argparse.ArgumentParser(description='Программа отправляет фотографии в Телеграмм канал с заданной интенсивностью')
    parser.add_argument('-t', help='укажите количество секунд, которое необходимо для задержки отправления фото', default='14400', type = int)
    parser.add_argument('-id', help='Указать id, на который необходимо посылать фотографии', default='@SpacePhotobyShukatka')
    args = parser.parse_args()
    return args

def create_list_pictures():
    pictures_path = list()
    for root, dir, file in os.walk('images'):
        for picture_name in file:
            pictures_path.append(os.path.join(root, picture_name))
    return pictures_path

def send_photo(chat_id, token, delay_time, pictures_paths):
    bot = telegram.Bot(token=token)
    while True:
        random.shuffle(pictures_paths)
        for picture_path in pictures_paths:
            with open(picture_path, 'rb') as pictures:
                bot.send_photo(chat_id, pictures)
            time.sleep(delay_time)


if __name__ == '__main__':
    load_dotenv()
    pictures_paths = create_list_pictures()
    chat_id = create_parser().id
    token = os.environ['TELEGRAM_TOKEN']
    delay_time = create_parser().t
    send_photo(chat_id, token, delay_time, pictures_paths)

