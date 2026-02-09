import os
from pathlib import Path
from sqlalchemy import URL

BASE_DIR = Path(__file__).resolve().parent

SQLA_DB_URL_ASYNC = URL.create(
    drivername="postgresql+asyncpg",
    username="adm",
    password="password",
    host="localhost",
    port=5432,
    database="hm4_blog",
)
SQLA_DB_ECHO = False

if os.getenv("SQLA_DB_ECHO"):
    SQLA_DB_ECHO = True
