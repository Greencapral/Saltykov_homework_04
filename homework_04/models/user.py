from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from homework_04.models.base import Base

if TYPE_CHECKING:
    from homework_04.models.post import Post


class User(Base):
    """Модель пользователя в БД."""

    #: Уникальный идентификатор пользователя (первичный ключ таблицы)
    id: Mapped[int] = mapped_column(primary_key=True)

    #: Имя пользователя (строка длиной до 50 символов)
    name: Mapped[str] = mapped_column(Text, server_default="", doc="Имя пользователя")

    #: Логин пользователя (строка длиной до 50 символов)
    username: Mapped[str] = mapped_column(Text, unique=True, doc="Логин пользователя")

    #: Электронная почта пользователя (строка длиной до 50 символов)
    email: Mapped[str] = mapped_column(
        Text, unique=True, doc="Электронная почта пользователя"
    )

    #: Связанные посты пользователя (связано с моделью Post через внешний ключ)
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user", doc="Связанные посты пользователя"
    )

    __table_args__ = (
        CheckConstraint(func.length(name) <= 50, "name_length"),
        CheckConstraint(func.length(username) <= 50, "username_length"),
        CheckConstraint(func.length(email) <= 50, "email_length"),
    )

    def __str__(self) -> str:
        """
        Человечески понятное представление экземпляра класса.

        :return: Строка, представляющая экземпляр класса User.
        """

        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", name={self.name!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            ")"
        )

    def __repr__(self) -> str:
        """
        Представление экземпляра класса для вывода в консоли.

        :return: Строка, представляющая экземпляр класса User.
        """

        return str(self)
