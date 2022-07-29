import sys
import traceback
from time import sleep
import RPi.GPIO as GPIO
from sqlalchemy.engine.url import URL

from services.models import DB_CONFIG
from services.requesting import send_telegram
from services.services import get_rasp_temp, msg, get_high_temp, db_init
from services.settings import CONTROL_PIN

TF_DICT = {
    True: "Включен",
    False: "Отключен",
}

if __name__ == "__main__":
    db_init()
    print(URL(**DB_CONFIG), **DB_CONFIG)
    control_pin = int(CONTROL_PIN)

    try:
        temp_on = get_high_temp()
        pinState = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(control_pin, GPIO.OUT, initial=0)
        temperature = get_rasp_temp()
        if temperature > temp_on and not pinState or temperature < temp_on - 10 and pinState:
            pinState = not pinState
            GPIO.output(control_pin, pinState)
            if pinState:
                send_telegram("Вентилятор включен, температура " + str(temperature))
                msg('', '')
            else:
                send_telegram("Вентилятор выключен, температура " + str(temperature))
                msg('', '')
        sleep(30)
    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")
    except ImportError as e:
        print("Other Exception")
        print("--- Start Exception Data:")
        traceback.print_exc(limit=2, file=sys.stdout)
        print("--- End Exception Data:")
    finally:
        print("CleanUp")
        if GPIO.input(control_pin):
            temperature = get_rasp_temp()
            send_telegram("Вентилятор выключен, температура " + str(temperature))
        GPIO.cleanup()
        print("End of program")
