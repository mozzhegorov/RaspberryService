from services.services import get_rasp_temp
from services.requesting import send_telegram

if __name__ == "__main__":
    rasp_temp = get_rasp_temp()
    send_telegram(f"Проверка температуры {rasp_temp}")
    if rasp_temp > 75:
        send_telegram("Повышенная температура Raspberry")
