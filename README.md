# downloads_images
В файле собраны все общие функции, которые используются в проект

# fetch_epic_nasa
Файл содержит скрипт для скачивание фотографий земли, с видом из космоса с сайта Nasa 

### Для запуска необходимо:
- Скачать файл `fetch_epic_nasa.py`
- По [данной ссылке](https://api.nasa.gov/#apod) получить для себя токен для доступа к скачиванию фотографий с сайта
- создать файл `.env`, В нём прописать полученный токен следующим образом: 
```
'NASA_TOKEN'='ВАШ ТОКЕН'
```
- В командной строке прописать: 
``` 
python fetch_epic_nasa.py -с "указать количество скачиваемых фотографий" 
```
Все фотографии скачиваются в папку `images`

# fetch_apod_nasa
Файл содержит скрипт для скачивание фотографий космоса, с сайта Nasa 
### Для запуска необходимо:
- Скачать файл `fetch_apod_nasa`
- По [данной ссылке](https://api.nasa.gov/#apod) получить для себя токен для доступа к скачиванию фотографий с сайта
- создать файл `.env`, В нём прописать полученный токен следующим образом: 
```
'NASA_TOKEN'='ВАШ ТОКЕН'
```
- В командной строке прописать: 
```
python fetch_apod_nasa.py -с "указать количество скачиваемых фотографий"
```

Все фотографии скачиваются в папку `images`

# fetch_spacex_images
Файл содержит скрипт для скачивание фотографий запуска шатлов SpaceX
### Для запуска необходимо:
- Скачать файл `fetch_spacex_images.py`
- В командной строке прописать: 
```
python fetch_spacex_images.py -id "Указать номер запуска, с которого хотите получить фото"
```
По умолчанию скачивается фото последнего запуска, если они есть в базе. Пример id `5eb87d47ffd86e000604b38a`

Все фотографии скачиваются в папку `images`

# telegram_bot
Файл содержит скрипт для запуска телеграмм бота, который будет с заданным интервалом времени отправлять на заданный канал фотографии из директории `images`
### Для запуска необходимо:
- Скачать файл `telegram_bot.py`
- Создать канал в телеграме и бота и получить токен, инструкция по ссылке: [Кликни тут](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/).
- создать файл `.env` и добавить туда токен следующей записью: 
```
'TELEGRAM_TOKEN'='ВАШ ТОКЕН'
``` 
и 
```
'CHANEL_ID'='ВАШ ID'
```
- Сделать бота администратором канала (Что бы он мог отправлять в нём фотографии)
- В командной строке прописать: 
```
telegram_bot.py -id "Указать id канала, в который посылать фотографии" -t "указать задержку отправлений фотографий в секундах"
```
