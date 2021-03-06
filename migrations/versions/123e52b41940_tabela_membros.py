"""tabela Membros

Revision ID: 123e52b41940
Revises: d01364254436
Create Date: 2021-10-15 14:08:47.533648

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '123e52b41940'
down_revision = 'd01364254436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('membro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=100), nullable=False),
    sa.Column('telefone', sa.Integer(), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_membro'))
    )
    with op.batch_alter_table('example', schema=None) as batch_op:
        batch_op.drop_index('uq_example_field1')

    op.drop_table('example')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('field1', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('field2', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('example', schema=None) as batch_op:
        batch_op.create_index('uq_example_field1', ['field1'], unique=False)

    op.drop_table('membro')
    # ### end Alembic commands ###
