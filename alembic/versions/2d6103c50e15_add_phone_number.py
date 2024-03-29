"""add phone number

Revision ID: 2d6103c50e15
Revises: de8fbd5c3a2c
Create Date: 2024-01-25 15:32:55.759760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d6103c50e15'
down_revision: Union[str, None] = 'de8fbd5c3a2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
