"""Added posts table

Revision ID: 3158884dceb3
Revises: 0440ae58f11c
Create Date: 2026-02-09 16:53:50.801390

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "3158884dceb3"
down_revision: Union[str, Sequence[str], None] = (
    "0440ae58f11c"
)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "title",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "body",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(body) <= 200",
            name=op.f("ck_posts_body_length"),
        ),
        sa.CheckConstraint(
            "length(title) <= 70",
            name=op.f("ck_posts_title_length"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_posts_user_id_users"),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_posts")
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
