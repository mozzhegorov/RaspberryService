from re import findall
from subprocess import check_output
from sqlalchemy.orm import sessionmaker
import services.models as models


def open_session():
    Session = sessionmaker(bind=models.engine)
    session = Session()
    return session


def msg(text, args):
    pass


def get_rasp_temp():
    temp_raw = check_output(["/usr/bin/vcgencmd", "measure_temp"]).decode()
    temperature_now = float(findall('\d+\.\d+', temp_raw)[0])
    return temperature_now


def get_high_temp():
    session = open_session()
    high_temp = session.query(models.Setting).\
        where(models.Setting.name == "high temp").nor_or_none()
    if high_temp:
        return int(high_temp)
    else:
        return None


def update_high_temp(new_high_temp: str):
    session = open_session()
    temperature = session.query(models.Setting).where(models.Setting.name == "high temp").one()
    temperature.value = int(new_high_temp)
    return int(new_high_temp)


def init_high_temp():
    session = open_session()
    high_temp = get_high_temp()
    if high_temp:
        return high_temp
    else:
        new_setting: models.Setting = models.Setting(
            name="high temp",
            value="70",
        )
        session.add(new_setting)
        session.commit()
        return 70


def db_init():
    models.DeclarativeBase.metadata.create_all(models.engine)
    init_high_temp()
