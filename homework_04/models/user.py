from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from homework_04.models.base import Base

if TYPE_CHECKING:
    from homework_04.models.post import Post


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, server_default="")
    username: Mapped[str] = mapped_column(Text, unique=True)
    email: Mapped[str] = mapped_column(Text, unique=True)

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    __table_args__=(
        CheckConstraint(func.length(name) <= 50,"name_length"),
        CheckConstraint(func.length(username) <= 50, "username_length"),
        CheckConstraint(func.length(email) <= 50, "email_length"),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", name={self.name!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
