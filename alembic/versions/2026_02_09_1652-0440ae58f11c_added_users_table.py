"""Added users table

Revision ID: 0440ae58f11c
Revises:
Create Date: 2026-02-09 16:52:19.224912

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "0440ae58f11c"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column("email", sa.Text(), nullable=False),
        sa.CheckConstraint(
            "length(email) <= 50",
            name=op.f("ck_users_email_length"),
        ),
        sa.CheckConstraint(
            "length(name) <= 50",
            name=op.f("ck_users_name_length"),
        ),
        sa.CheckConstraint(
            "length(username) <= 50",
            name=op.f("ck_users_username_length"),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_users")
        ),
        sa.UniqueConstraint(
            "email", name=op.f("uq_users_email")
        ),
        sa.UniqueConstraint(
            "username", name=op.f("uq_users_username")
        ),
    )



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
