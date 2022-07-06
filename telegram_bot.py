import telegram
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ['TELEGRAM_TOKEN']
bot = telegram.Bot(token=token)
updates = bot.get_updates()
bot.send_message(chat_id='@SpacePhotobyShukatka', text='Привет')
