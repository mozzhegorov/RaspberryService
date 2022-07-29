from raspberry.services import get_temp
from requesting import send_telegram

if __name__ == "__main__":
    send_telegram("RaspberryPi на связи")
    rasp_temp = get_temp()
    if rasp_temp > 75:
        send_telegram("Повышенная температура Raspberry")



