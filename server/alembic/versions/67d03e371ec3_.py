"""empty message

Revision ID: 67d03e371ec3
Revises: f4fa87ac1ac8
Create Date: 2024-07-19 21:41:55.052349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67d03e371ec3'
down_revision: Union[str, None] = 'f4fa87ac1ac8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('name', sa.String(length=60), nullable=True))
    op.drop_column('customer', 'first_name')
    op.drop_column('customer', 'last_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.drop_column('customer', 'name')
    # ### end Alembic commands ###
