"""
All three subscription tables
Revision ID: 59af27b681f
Revises: 466f4d318cd
Create Date: 2014-11-03 18:50:48.381170
"""
# revision identifiers, used by Alembic.
revision = '59af27b681f'
down_revision = '466f4d318cd'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag_sub',
    sa.Column('sub_by', sa.UUID(), nullable=False),
    sa.Column('sub_to', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['sub_by'], ['user.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sub_to'], ['tag.tag_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('sub_by', 'sub_to')
    )
    op.create_table('user_sub',
    sa.Column('sub_by', sa.UUID(), nullable=False),
    sa.Column('sub_to', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['sub_by'], ['user.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sub_to'], ['user.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('sub_by', 'sub_to')
    )
    op.create_table('idea_sub',
    sa.Column('sub_by', sa.UUID(), nullable=False),
    sa.Column('sub_to', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['sub_by'], ['user.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sub_to'], ['idea.idea_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('sub_by', 'sub_to')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('idea_sub')
    op.drop_table('user_sub')
    op.drop_table('tag_sub')
    ### end Alembic commands ###
