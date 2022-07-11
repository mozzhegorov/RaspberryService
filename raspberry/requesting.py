import requests
import environ

env = environ.Env()
environ.Env.read_env()
BOT_TOKEN = env.get_value('BOT_TOKEN')
CHANEL_ID = env.get_value('CHANEL_ID')


def send_telegram(text):
    token = BOT_TOKEN
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


if __name__ == '__main__':
    print(BOT_TOKEN, CHANEL_ID)
    send_telegram('test')
