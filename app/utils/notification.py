import requests
from config import Telegram

def telegram_notif(message):
   response = requests.post(
         url=f'https://api.telegram.org/bot{Telegram.TOKEN}/sendMessage',
         data={'chat_id': Telegram.CHAT_ID, 'text': str(message)}
      ).json()
   
   return response