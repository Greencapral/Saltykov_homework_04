from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from homework_04.models.base import Base

if TYPE_CHECKING:
    from homework_04.models.user import User


class Post(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    title: Mapped[str] = mapped_column(Text, server_default="")
    body: Mapped[str] = mapped_column(Text, server_default="")
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
    __table_args__ = (
        CheckConstraint(func.length(title) <= 70, "title_length"),
        CheckConstraint(func.length(body) <= 200, "body_length"),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", title={self.title!r}"
            f", body={self.body!r}"
            f", user_id={self.user_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
