from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import homework_04.models.config as config

# Создается асинхронный движок базы данных с заданными параметрами подключения
async_engine = create_async_engine(
    url=config.SQLA_DB_URL_ASYNC,  # URL подключения к базе данных
    echo=config.SQLA_DB_ECHO,  # Включает вывод логов SQL-команд
)

# Конструктор асинхронных сессий для взаимодействия с базой данных
ASYNC_Session = async_sessionmaker(
    bind=async_engine,  # Привязываем созданный ранее асинхронный движок
    expire_on_commit=False,  # Отключаем автоматическое обновление объектов после коммита транзакций
)
