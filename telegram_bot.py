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

def send_photo(chat_id, token, delay_time, pictures_path):
    bot = telegram.Bot(token=token)
    while True:
        if len(pictures_path) >= 1:
            with open (random.choice(pictures_path), 'rb') as pictures:
                bot.send_photo(chat_id, pictures)
            pictures_path.remove(pictures.name)
            time.sleep(delay_time)
        elif len(pictures_path) < 1:
            pictures_path = files.copy()
            random.shuffle(name_pictures)


if __name__ == '__main__':
    load_dotenv()
    chat_id = create_parser().id
    token = os.environ['TELEGRAM_TOKEN']
    delay_time = create_parser().t
    send_message_bot(chat_id, token, delay_time)

