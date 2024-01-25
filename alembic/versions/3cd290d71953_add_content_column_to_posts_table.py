"""add content column to posts table

Revision ID: 3cd290d71953
Revises: a499d2545d0e
Create Date: 2024-01-25 13:19:26.832495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cd290d71953'
down_revision: Union[str, None] = 'a499d2545d0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
