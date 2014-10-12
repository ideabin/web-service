"""
idea_story_status
Revision ID: cc98a97380
Revises: 4fdde98983
Create Date: 2014-10-12 05:40:25.076142
"""
# revision identifiers, used by Alembic.
revision = 'cc98a97380'
down_revision = '4fdde98983'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('idea', sa.Column('status', sa.String(length=20), nullable=True))
    op.add_column('idea', sa.Column('story', sa.String(length=120), nullable=True))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('idea', 'story')
    op.drop_column('idea', 'status')
    ### end Alembic commands ###