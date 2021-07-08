"""empty message

Revision ID: 7c897a849c01
Revises: afc97a333866
Create Date: 2021-06-16 22:30:00.085520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c897a849c01'
down_revision = 'afc97a333866'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Artist_ID', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Venue_ID', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Start_Time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['Artist_ID'], ['Artist.id'], name='Show_Artist_ID_fkey'),
    sa.ForeignKeyConstraint(['Venue_ID'], ['Venue.id'], name='Show_Venue_ID_fkey'),
    sa.PrimaryKeyConstraint('id', 'Artist_ID', 'Venue_ID', name='Show_pkey')
    )
    # ### end Alembic commands ###
