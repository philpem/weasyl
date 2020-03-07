"""Remove dead ads table

Revision ID: f9226a83bbb6
Revises: 1307b62614a4
Create Date: 2020-02-27 23:14:41.314000

"""

# revision identifiers, used by Alembic.
revision = 'f9226a83bbb6'
down_revision = '1307b62614a4'

from alembic import op   # lgtm[py/unused-import]
import sqlalchemy as sa  # lgtm[py/unused-import]
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ind_ads_end', table_name='ads')
    op.drop_table('ads')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ads',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('owner', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('link_target', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('file', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('end', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['file'], [u'media.mediaid'], name=u'ads_file_fkey', onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id', name=u'ads_pkey')
    )
    op.create_index('ind_ads_end', 'ads', ['end'], unique=False)
    # ### end Alembic commands ###