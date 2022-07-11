from re import findall
from subprocess import check_output
import db


def msg(text, args):
    pass


def get_temp():
    temp_raw = check_output(["/usr/bin/vcgencmd", "measure_temp"]).decode()
    temperature_now = float(findall('\d+\.\d+', temp_raw)[0])
    return temperature_now


class Temperature:

    def __init__(self, *args, **kwargs):
        self.high_temp: float = self.init_high_temp()

    @staticmethod
    def init_high_temp():
        high_temp: str = db.data_base_fetchone(db.GET_HIGH_TEMP, ('high temp',))
        if high_temp.isdigit():
            return float(high_temp)
        else:
            db.data_base_fetchone(db.UPDATE_HIGH_TEMP, ('70', 'high temp', ))
            return 70

    def update_high_temp(self, new_value: str):
        if new_value.isdigit():
            self.high_temp = float(new_value)
            db.data_base_fetchone(db.UPDATE_HIGH_TEMP, (self.high_temp, 'high temp', ))
            return True
        return False
