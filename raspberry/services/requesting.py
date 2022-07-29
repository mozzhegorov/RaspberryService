import requests
from services.settings import BOT_TOKEN, CHANEL_ID


def send_telegram(text):
    token = BOT_TOKEN
    print(BOT_TOKEN, CHANEL_ID)
    url = "https://api.telegram.org/bot"
    channel_id = CHANEL_ID
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        print(r)
        raise Exception("post_text error")
