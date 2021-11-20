"""relacionamento membro e campanha

Revision ID: 540950a902e3
Revises: a06edfd89e0f
Create Date: 2021-11-19 19:18:28.144194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540950a902e3'
down_revision = 'a06edfd89e0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanha', schema=None) as batch_op:
        batch_op.add_column(sa.Column('membro_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_campanha_membro_id_membro'), 'membro', ['membro_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanha', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_campanha_membro_id_membro'), type_='foreignkey')
        batch_op.drop_column('membro_id')

    # ### end Alembic commands ###