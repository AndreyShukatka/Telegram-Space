import telegram
import os
from dotenv import load_dotenv

load_dotenv()
chat_id = '@SpacePhotobyShukatka'
token = os.environ['TELEGRAM_TOKEN']
bot = telegram.Bot(token=token)
updates = bot.get_updates()
bot.send_document(chat_id = chat_id, document = open('images/epic_Nasa_2022_06_30_00_03.png', 'rb'))
