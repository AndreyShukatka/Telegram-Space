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
        '--seconds_delay',
        help='укажите количество секунд, которое '
             'необходимо для задержки отправления фото',
        default='10',
        type=int
    )
    parser.add_argument(
        '--image_path',
        help='укажите название фото с расширением,'
             ' и путём, которое опубликовать',
    )
    args = parser.parse_args()
    return args


def add_photo_paths():
    paths = list()
    for root, directory, filenames in os.walk('images'):
        for picture in filenames:
            paths.append(os.path.join(root, picture))
    return paths


def publish_image_to_channel(path, token):
    bot = telegram.Bot(token=token)
    seconds = 20
    with open(path, 'rb') as pictures:
        try:
            bot.send_photo(channel_id, pictures)
        except telegram.error.NetworkError:
            print('Неудачная попытка соединения,'
                    ' reconnect через 20 секунд')
            time.sleep(seconds)


def publish_endlessly_random_photos(paths, token, seconds_delay):
    while True:
        random.shuffle(paths)
        for path in paths:
            publish_image_to_channel(path, token)
            time.sleep(seconds_delay)


if __name__ == '__main__':
    load_dotenv()
    channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    token = os.environ['TELEGRAM_TOKEN']
    args = input_parsing_command_line()
    path = args.image_path
    paths = add_photo_paths()
    seconds_delay = args.seconds_delay
    if args.image_path:
        publish_image_to_channel(path, token)
    else:
        publish_endlessly_random_photos(paths, token, seconds_delay)
