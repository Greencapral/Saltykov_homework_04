from typing import TYPE_CHECKING

from sqlalchemy import Text, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from homework_04.models.base import Base

if TYPE_CHECKING:
    from homework_04.models.user import User


class Post(Base):
    """Модель для хранения постов в базе данных."""

    #: Максимально допустимая длина заголовка поста
    max_title_len = 70

    #: Максимально допустимая длина тела поста
    max_body_len = 200

    #: Идентификатор поста (первичный ключ)
    id: Mapped[int] = mapped_column(primary_key=True)

    #: Внешний ключ, ссылающийся на таблицу users (автор поста)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    #: Заголовок поста (строка длиной до max_title_len символов)
    title: Mapped[str] = mapped_column(Text, server_default="", doc="Заголовок поста")

    #: Тело поста (строка длиной до max_body_len символов)
    body: Mapped[str] = mapped_column(Text, server_default="", doc="Содержание поста")

    #: Пользователь, создавший этот пост (связано с таблицей Users)
    user: Mapped["User"] = relationship(
        back_populates="posts", doc="Пользователь, написавший пост"
    )

    __table_args__ = (
        CheckConstraint(func.length(title) <= max_title_len, "title_length"),
        CheckConstraint(func.length(body) <= max_body_len, "body_length"),
    )

    def __str__(self) -> str:
        """
        Человечески понятное представление экземпляра класса.

        :return: Строка, содержащая информацию о посте.
        """

        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", title={self.title!r}"
            f", body={self.body!r}"
            f", user_id={self.user_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        """
        Представление экземпляра класса для вывода в консоли.

        :return: Строка, представляющая объект Post.
        """

        return str(self)
