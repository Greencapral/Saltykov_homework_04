from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Базовая декларативная база для моделей SQLAlchemy."""

    #: Набор метаданных с соглашением именования таблиц
    metadata = MetaData(naming_convention=convention)

    @declared_attr.directive
    def __tablename__(self) -> str:
        """
        Автоматическое формирование названия таблицы исходя из имени класса.

        Название таблицы получается путем преобразования имени класса в нижний регистр и добавления суффикса "s".

        :return: Название таблицы в формате "<имя_класса>s".
        """

        return f"{self.__name__.lower()}s"
