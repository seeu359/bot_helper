import os
from pathlib import Path
from typing import NamedTuple

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
TG_TOKEN = os.getenv('TG_TOKEN')


class DBCreds(NamedTuple):
    user: str
    password: str
    host: str
    port: str
    db_name: str


def get_database_url():
    prefix = 'postgresql+psycopg2://'
    creds = get_db_credentials()
    return f'{prefix}{creds.user}:{creds.password}@' \
           f'{creds.host}:{creds.port}/{creds.db_name}'


def get_db_credentials() -> DBCreds:
    return DBCreds(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        db_name=os.getenv('POSTGRES_DB')
    )


def get_logs_path():
    return os.path.join(BASE_DIR, '../logs.log')


LOGGER = logger.add(
    sink=get_logs_path(),
    level='INFO',
    format='{time:YYYY.MM.DD - HH:mm:ss} - {level} - {message}',
)
