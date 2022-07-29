import configparser

config = configparser.ConfigParser()
config.read('.env')

BOT_TOKEN = config['BOT_TOKEN']
CHANEL_ID = config['CHANEL_ID']
DB_NAME = config['DB_NAME']
DB_USER = config['DB_USER'],
DB_PASSWORD = config['DB_PASSWORD']
DB_HOST = config['DB_HOST']
DB_PORT = config['DB_PORT']
