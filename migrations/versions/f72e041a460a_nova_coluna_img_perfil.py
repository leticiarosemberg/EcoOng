"""nova coluna img_perfil

Revision ID: f72e041a460a
Revises: 8e0e19569864
Create Date: 2021-11-04 19:40:25.225060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f72e041a460a'
down_revision = '8e0e19569864'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_perfil', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('membro', schema=None) as batch_op:
        batch_op.drop_column('img_perfil')

    # ### end Alembic commands ###