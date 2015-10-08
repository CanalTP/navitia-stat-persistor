"""add journey_request

Revision ID: fos5a55d7a
Revises: 14a0ba4227ce
Create Date: 2015-10-08 10:15:14.086759

"""

# revision identifiers, used by Alembic.
revision = 'fos5a55d7a'
down_revision = '14a0ba4227ce'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'response',
        sa.Column('item_on_page', sa.Integer(), nullable=False),
        sa.Column('request_id', sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(['request_id'], ['stat.requests.id'],),
        schema='stat'
    )

def downgrade():
    op.drop_table('response', schema='stat')
