"""Safen foreign keys

Revision ID: 79ee87f22571
Revises: eea0490be1f8
Create Date: 2023-01-03 01:35:21.948554

"""

# revision identifiers, used by Alembic.
revision = '79ee87f22571'
down_revision = 'eea0490be1f8'

from alembic import op


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('charcomment_hidden_by_fkey', 'charcomment', type_='foreignkey')
    op.create_foreign_key('charcomment_hidden_by_fkey', 'charcomment', 'login', ['hidden_by'], ['userid'], ondelete='SET NULL')
    op.drop_constraint('comments_hidden_by_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_parentid_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key('comments_hidden_by_fkey', 'comments', 'login', ['hidden_by'], ['userid'], ondelete='SET NULL')
    op.create_foreign_key('comments_parentid_fkey', 'comments', 'comments', ['parentid'], ['commentid'])
    op.drop_constraint('emailblacklist_userid_fkey', 'emailblacklist', type_='foreignkey')
    op.create_foreign_key('emailblacklist_userid_fkey', 'emailblacklist', 'login', ['added_by'], ['userid'])
    op.drop_constraint('journalcomment_hidden_by_fkey', 'journalcomment', type_='foreignkey')
    op.create_foreign_key('journalcomment_hidden_by_fkey', 'journalcomment', 'login', ['hidden_by'], ['userid'], ondelete='SET NULL')
    op.drop_constraint('report_closerid_fkey', 'report', type_='foreignkey')
    op.create_foreign_key('report_closerid_fkey', 'report', 'login', ['closerid'], ['userid'], ondelete='SET NULL')
    op.drop_constraint('reportcomment_userid_fkey', 'reportcomment', type_='foreignkey')
    op.create_foreign_key('reportcomment_userid_fkey', 'reportcomment', 'login', ['userid'], ['userid'])
    op.drop_constraint('sessions_user_agent_id_fkey', 'sessions', type_='foreignkey')
    op.create_foreign_key('sessions_user_agent_id_fkey', 'sessions', 'user_agents', ['user_agent_id'], ['user_agent_id'])
    op.drop_constraint('siteupdate_userid_fkey', 'siteupdate', type_='foreignkey')
    op.create_foreign_key('siteupdate_userid_fkey', 'siteupdate', 'login', ['userid'], ['userid'])
    op.drop_constraint('submission_folderid_fkey', 'submission', type_='foreignkey')
    op.create_foreign_key('submission_folderid_fkey', 'submission', 'folder', ['folderid'], ['folderid'], ondelete='SET NULL')
    op.drop_constraint('tag_updates_userid_fkey', 'tag_updates', type_='foreignkey')
    op.create_foreign_key('tag_updates_userid_fkey', 'tag_updates', 'login', ['userid'], ['userid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tag_updates_userid_fkey', 'tag_updates', type_='foreignkey')
    op.create_foreign_key('tag_updates_userid_fkey', 'tag_updates', 'login', ['userid'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('submission_folderid_fkey', 'submission', type_='foreignkey')
    op.create_foreign_key('submission_folderid_fkey', 'submission', 'folder', ['folderid'], ['folderid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('siteupdate_userid_fkey', 'siteupdate', type_='foreignkey')
    op.create_foreign_key('siteupdate_userid_fkey', 'siteupdate', 'login', ['userid'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('sessions_user_agent_id_fkey', 'sessions', type_='foreignkey')
    op.create_foreign_key('sessions_user_agent_id_fkey', 'sessions', 'user_agents', ['user_agent_id'], ['user_agent_id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('reportcomment_userid_fkey', 'reportcomment', type_='foreignkey')
    op.create_foreign_key('reportcomment_userid_fkey', 'reportcomment', 'login', ['userid'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('report_closerid_fkey', 'report', type_='foreignkey')
    op.create_foreign_key('report_closerid_fkey', 'report', 'login', ['closerid'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('journalcomment_hidden_by_fkey', 'journalcomment', type_='foreignkey')
    op.create_foreign_key('journalcomment_hidden_by_fkey', 'journalcomment', 'login', ['hidden_by'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('emailblacklist_userid_fkey', 'emailblacklist', type_='foreignkey')
    op.create_foreign_key('emailblacklist_userid_fkey', 'emailblacklist', 'login', ['added_by'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('comments_parentid_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_hidden_by_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key('comments_parentid_fkey', 'comments', 'comments', ['parentid'], ['commentid'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('comments_hidden_by_fkey', 'comments', 'login', ['hidden_by'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('charcomment_hidden_by_fkey', 'charcomment', type_='foreignkey')
    op.create_foreign_key('charcomment_hidden_by_fkey', 'charcomment', 'login', ['hidden_by'], ['userid'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###
