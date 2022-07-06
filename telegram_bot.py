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

def send_message_bot(chat_id, token, delay_time):
    bot = telegram.Bot(token=token)
    filesindir = os.walk('images')
    for root, dirs, files in filesindir:
        name_pictures = files.copy()
        while True:
            if len(name_pictures) >= 1:
                picture_download = open(f'images/{random.choice(name_pictures)}', 'rb')
                bot.send_photo(chat_id=chat_id, photo=picture_download)
                picture_download.close()
                name_pictures.remove(picture_download.name.split('/')[1])
                time.sleep(delay_time)
            elif len(name_pictures) < 1:
                name_pictures = files.copy()
                random.shuffle(name_pictures)


if __name__ == '__main__':
    load_dotenv()
    chat_id = chat_id = create_parser().id
    token = os.environ['TELEGRAM_TOKEN']
    delay_time = create_parser().t
    send_message_bot(chat_id, token, delay_time)

