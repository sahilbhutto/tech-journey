"""add country column

Revision ID: e8df7f74bf87
Revises: 7354613d25ed
Create Date: 2026-11-03 14:03:39.839753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8df7f74bf87'
down_revision: Union[str, Sequence[str], None] = '7354613d25ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('country', sa.String(length=50), nullable=False))


def downgrade() -> None:
    op.drop_column('users', 'country')
