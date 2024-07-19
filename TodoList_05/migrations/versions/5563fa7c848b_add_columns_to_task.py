"""Add columns to Task

Revision ID: 5563fa7c848b
Revises: 7197ac51d76f
Create Date: 2024-07-05 12:54:36.690641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5563fa7c848b'
down_revision = '7197ac51d76f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('new', sa.Date(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('new')

    # ### end Alembic commands ###
