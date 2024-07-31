"""empty message

Revision ID: eea9258ef38b
Revises: f3bb9eb1ed78
Create Date: 2024-07-10 10:05:03.699324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eea9258ef38b'
down_revision: Union[str, None] = 'f3bb9eb1ed78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.Column('import_price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['size_id'], ['size.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice_details')
    op.drop_table('inventory')
    # ### end Alembic commands ###
