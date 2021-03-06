"""Coluna autor na tabela campanha

Revision ID: eacf52c4c1e1
Revises: 28c099a8784c
Create Date: 2021-12-07 15:39:28.410015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eacf52c4c1e1'
down_revision = '28c099a8784c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanha', schema=None) as batch_op:
        batch_op.add_column(sa.Column('autor', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanha', schema=None) as batch_op:
        batch_op.drop_column('autor')

    # ### end Alembic commands ###
