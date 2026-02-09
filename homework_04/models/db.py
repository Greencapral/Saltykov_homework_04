from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import homework_04.models.config as config

async_engine = create_async_engine(
    url=config.SQLA_DB_URL_ASYNC,
    echo=config.SQLA_DB_ECHO,
)

ASYNC_Session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
