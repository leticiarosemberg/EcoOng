"""ajuste

Revision ID: cf21ade20ae4
Revises: 123e52b41940
Create Date: 2021-10-22 17:37:18.124123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf21ade20ae4'
down_revision = '123e52b41940'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.alter_column('telefone',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.alter_column('telefone',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###
