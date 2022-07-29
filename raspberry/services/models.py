from sqlalchemy import Column, Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from services.settings import (
    DB_NAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_USER,
)

DB_CONFIG = {
    "drivername": "postgresql+psycopg2",
    "host": DB_HOST,
    "port": DB_PORT,
    "username": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME,
}
# DB_CONFIG = env.get_value('DB_CONFIG')

engine = create_engine(URL(**DB_CONFIG), echo=True)
# engine = create_engine("sqlite:///test.db")

DeclarativeBase = declarative_base()


class Setting(DeclarativeBase):
    __tablename__ = "setting"

    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String(64),
        nullable=False,
    )
    value = Column(
        String(64),
        nullable=False,
    )

    def __repr__(self):
        return f"Person(id={self.id!r})"