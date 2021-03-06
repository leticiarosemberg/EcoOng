"""atualizacao coluna img_perfil da tabela membro

Revision ID: f2202f87b0bb
Revises: 4518d798854a
Create Date: 2021-11-19 12:31:41.760199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f2202f87b0bb'
down_revision = '4518d798854a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.drop_column('img_capa')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_capa', mysql.VARCHAR(length=100), nullable=True))

    # ### end Alembic commands ###
