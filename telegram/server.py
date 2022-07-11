import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode

from raspberry.db import create_tables
from raspberry.main import rasp_temp

from texts import *
import environ

env = environ.Env()
environ.Env.read_env()

API_TOKEN = env.get_value('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def new_calculation(message: types.Message):
    """Приветствие"""
    await message.answer(START_TEXT, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: message.text.startswith('/newhightemp'))
async def new_calculation(message: types.Message):
    """Обновление температуры"""
    new_high_temp = int(message.text[12:])
    rasp_temp.update_high_temp(new_high_temp)
    await message.answer(UPDATE_TEMP_TEXT.format(new_high_temp), parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    create_tables()
    executor.start_polling(dp, skip_updates=True)
