import datetime
import os
import sys
import traceback
from re import findall
from subprocess import check_output
from time import sleep
from requesting import send_telegram
import RPi.GPIO as GPIO

# DB_CONFIG = {
#     'provider': 'postgres',
#     'user': 'postgre',
#     'password': '4762',
#     'host': '127.0.0.1',
#     'database': 'bk_fucker',
# }

TF_DICT = {
    True: 'Включен',
    False: 'Отключен',
}


# db = Database()
# db.bind(**DB_CONFIG)

def get_temp():
    temp_raw = check_output(["/usr/bin/vcgencmd", "measure_temp"]).decode()
    temperature_now = float(findall('\d+\.\d+', temp_raw)[0])
    return temperature_now


try:
    temp_on = 73
    control_pin = 3
    pinState = False

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(control_pin, GPIO.OUT, initial=0)
    while True:
        # cmd = '/opt/vc/bin/vcgencmd measure_temp'
        # line = os.popen(cmd).readline().strip()[5::][:-2:]
        # _time = datetime.datetime.now()

        # write_in_db()

        # print(f'{_time.hour:02}:{_time.minute:02}:{_time.second:02} - {line}')
        # time.sleep(5)

        # temperature = get_temp()
        send_telegram('Я работаю')
        # if temperature > temp_on and not pinState or temperature < temp_on - 10 and pinState:
        #     pinState = not pinState
        #     GPIO.output(control_pin, pinState)
        #     if pinState:
        #         send_telegram('Вентилятор включен, температура ' + str(temperature))
        #     else:
        #         send_telegram('Вентилятор выключен, темпертура ' + str(temperature))
        sleep(1)
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
