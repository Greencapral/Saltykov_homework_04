from sqlalchemy import create_engine
import homework_04.models.config as config

engine = create_engine(
    url=config.SQLA_DB_URL,
    echo=config.SQLA_DB_ECHO,
)
