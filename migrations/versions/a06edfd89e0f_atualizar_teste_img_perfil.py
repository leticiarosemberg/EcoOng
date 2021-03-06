"""atualizar teste img_perfil

Revision ID: a06edfd89e0f
Revises: 6465433f0e59
Create Date: 2021-11-19 13:29:27.575874

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a06edfd89e0f'
down_revision = '6465433f0e59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_perfil', sa.String(length=100), nullable=True))
        batch_op.drop_column('perfil')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('perfil', mysql.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('img_perfil')

    # ### end Alembic commands ###
