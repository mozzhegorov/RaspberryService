import environ

env = environ.Env()
environ.Env.read_env()

BOT_TOKEN = env.get_value('BOT_TOKEN')
CHANEL_ID = env.get_value('CHANEL_ID')
DB_NAME = env.get_value('DB_NAME'),
DB_USER = env.get_value('DB_USER'),
DB_PASSWORD = env.get_value('DB_PASSWORD'),
DB_HOST = env.get_value('DB_HOST'),
DB_PORT = env.get_value('DB_PORT'),
