import argparse
import os
import random
import time
from dotenv import load_dotenv
import telegram


def input_parsing_command_line(channel_id):
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографии'
                    ' в Телеграмм канал с заданной интенсивностью'
    )
    parser.add_argument(
        '-t',
        '--seconds_delay',
        help='укажите количество секунд, которое '
             'необходимо для задержки отправления фото',
        default='10',
        type=int
    )
    parser.add_argument(
        '-id',
        '--channel_id',
        help='Указать id, на который необходимо посылать фотографии',
        default=channel_id
    )
    parser.add_argument(
        '-im',
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


def sending_file(pictures, token):
    bot = telegram.Bot(token=token)
    seconds = 20
    try:
        bot.send_photo(args.id, pictures)
    except telegram.error.NetworkError:
        print('Неудачная попытка соединения,'
              ' reconnect через 20 секунд')
        time.sleep(seconds)


def publish_endlessly_random_photos(args, paths):
    while True:
        random.shuffle(paths)
        for path in paths:
            with open(path, 'rb') as pictures:
                sending_file(pictures, token)
            time.sleep(args.t)


def publish_image_to_channel(args):
    with open(args.im, 'rb') as pictures:
        sending_file(pictures, token)


if __name__ == '__main__':
    load_dotenv()
    channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    token = os.environ['TELEGRAM_TOKEN']
    args = input_parsing_command_line(channel_id)
    paths = add_photo_paths()
    if args.im:
        publish_image_to_channel(args)
    else:
        publish_endlessly_random_photos(args, paths)
