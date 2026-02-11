import os
from pathlib import Path
from sqlalchemy import URL

# Определяем путь к основному каталогу приложения относительно текущего файла
BASE_DIR = Path(__file__).resolve().parent

# Формируем строку подключения к PostgreSQL используя драйвер asyncpg
SQLA_DB_URL_ASYNC = URL.create(
    drivername="postgresql+asyncpg",  # Драйвер асинхронного соединения с PostgreSQL
    username="adm",  # Имя пользователя базы данных
    password="password",  # Пароль пользователя базы данных
    host="localhost",  # Адрес хоста базы данных
    port=5432,  # Порт базы данных
    database="hm4_blog",  # Название базы данных
)

# По умолчанию отключаем эхо-вывод SQL-запросов
SQLA_DB_ECHO = False

# Перезаписываем настройку, если переменная окружения SQLA_DB_ECHO установлена
if os.getenv("SQLA_DB_ECHO"):
    SQLA_DB_ECHO = True
