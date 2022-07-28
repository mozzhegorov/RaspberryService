import datetime
import os
import sys
import traceback
from time import sleep
import RPi.GPIO as GPIO
import environ
from requesting import send_telegram
from services import get_temp, Temperature, msg
from db import create_tables

TF_DICT = {
    True: "Включен",
    False: "Отключен",
}

env = environ.Env()
environ.Env.read_env()
CONTROL_PIN = env.get_value("CONTROL_PIN")

rasp_temp = Temperature()

if __name__ == "__main__":
    create_tables()
    print("Script run")
    send_telegram("\ура ")

    try:
        temp_on = rasp_temp.high_temp
        control_pin = int(CONTROL_PIN)
        pinState = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(control_pin, GPIO.OUT, initial=0)
        temperature = get_temp()
        if temperature > temp_on and not pinState or temperature < temp_on - 10 and pinState:
            pinState = not pinState
            GPIO.output(control_pin, pinState)
            if pinState:
                send_telegram("Вентилятор включен, температура " + str(temperature))
                msg('', '')
            else:
                send_telegram("Вентилятор выключен, температура " + str(temperature))
                msg('', '')
        sleep(10)
    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")
    except ImportError as e:
        print("Other Exception")
        print("--- Start Exception Data:")
        traceback.print_exc(limit=2, file=sys.stdout)
        print("--- End Exception Data:")
    finally:
        print("CleanUp")
        GPIO.cleanup()
        print("End of program")
