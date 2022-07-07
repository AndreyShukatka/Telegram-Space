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
    path_pictures = list()
    for root, dir, file in os.walk('images'):
        for name_picture in file:
            path_pictures.append(os.path.join(root, name_picture))
    return path_pictures

def send_message_bot(chat_id, token, delay_time):
    bot = telegram.Bot(token=token)
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
    chat_id = create_parser().id
    token = os.environ['TELEGRAM_TOKEN']
    delay_time = create_parser().t
    send_message_bot(chat_id, token, delay_time)

