import environ
import psycopg2 as dbdriver

env = environ.Env()
environ.Env.read_env()

DB_CONFIG = {
        'dbname': env.get_value('DB_NAME'),
        'user': env.get_value('DB_USER'),
        'password': env.get_value('DB_PASSWORD'),
        'host': env.get_value('DB_HOST'),
        'port': env.get_value('DB_PORT'),
}
# DB_CONFIG = env.get_value('DB_CONFIG')

SETTINGS_EXISTS = """
    SELECT * FROM information_schema.tables  
    WHERE table_name='settings';
"""

SETTINGS_EXISTS = """
    SELECT * FROM information_schema.tables  
    WHERE table_name='history';
"""
CREATE_SETTINGS_TABLE = """
    CREATE TABLE IF NOT EXISTS settings (
        id VARCHAR(50) PRIMARY KEY,
        value VARCHAR(50)
    );
"""
CREATE_SETTINGS_TABLE = """
    CREATE TABLE IF NOT EXISTS history (
        id SERIAL PRIMARY KEY,
        msg VARCHAR(100)
    );
"""
DROP_SETTINGS_TABLE = """
    DROP TABLE IF EXISTS settings;
"""
DROP_HISTORY_TABLE = """
    DROP TABLE IF EXISTS history;
"""

GET_HIGH_TEMP = """
    SELECT value FROM settings
    WHERE id=%s
"""

UPDATE_HIGH_TEMP = """
    UPDATE settings 
    SET value=%s
    WHERE id=%s;
"""


def create_tables():
    with dbdriver.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute(SETTINGS_EXISTS)
        table_exists = bool(cursor.fetchall())
        if not table_exists:
            cursor.execute(CREATE_SETTINGS_TABLE)


def data_base_action(script, inserted_data=None):
    with dbdriver.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        if inserted_data:
            cursor.execute(script, inserted_data)
        else:
            cursor.execute(script)


def data_base_fetch(script, inserted_data=None):
    with dbdriver.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute(script, inserted_data)
        return cursor.fetchall()


def data_base_fetchone(script, inserted_data=None):
    with dbdriver.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute(script, inserted_data)
        return cursor.fetchone()


if __name__ == '__main__':
    create_tables()
