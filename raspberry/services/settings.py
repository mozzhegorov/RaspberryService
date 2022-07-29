import configparser

config = configparser.ConfigParser()
config.read('/home/.env')

general_env = config["General"]

BOT_TOKEN = general_env['BOT_TOKEN']
CHANEL_ID = general_env['CHANEL_ID']
DB_NAME = general_env['DB_NAME']
DB_USER = general_env['DB_USER']
DB_PASSWORD = general_env['DB_PASSWORD']
DB_HOST = general_env['DB_HOST']
DB_PORT = general_env['DB_PORT']
