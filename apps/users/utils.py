import requests
import os

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')

def send_tg_message(message):
    url = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage'
    payload = {'chat_id': TG_CHAT_ID, 'text': message}
    try:
        resp = requests.post(url, data=payload)
    except Exception as e:
        print(e)