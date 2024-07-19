"""file_path 추가

Revision ID: d8415f57140e
Revises: b21be87d33d4
Create Date: 2024-07-18 12:06:22.165632

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8415f57140e'
down_revision = 'b21be87d33d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_path', sa.String(length=256), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=150),
               type_=sa.String(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(length=150),
               existing_nullable=False)

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('file_path')

    # ### end Alembic commands ###
