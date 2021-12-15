"""atualizacao da tabela noticia

Revision ID: 24daba43c6f1
Revises: b2bfb0b97f34
Create Date: 2021-12-15 02:29:51.171458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24daba43c6f1'
down_revision = 'b2bfb0b97f34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('noticiatag', schema=None) as batch_op:
        batch_op.drop_constraint('fk_noticiatag_noticia_id_noticia', type_='foreignkey')
        batch_op.drop_constraint('fk_noticiatag_tag_id_tag', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_noticiatag_noticia_id_noticia'), 'noticia', ['noticia_id'], ['id'], ondelete='cascade')
        batch_op.create_foreign_key(batch_op.f('fk_noticiatag_tag_id_tag'), 'tag', ['tag_id'], ['id'], ondelete='cascade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('noticiatag', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_noticiatag_tag_id_tag'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_noticiatag_noticia_id_noticia'), type_='foreignkey')
        batch_op.create_foreign_key('fk_noticiatag_tag_id_tag', 'tag', ['tag_id'], ['id'])
        batch_op.create_foreign_key('fk_noticiatag_noticia_id_noticia', 'noticia', ['noticia_id'], ['id'])

    # ### end Alembic commands ###
