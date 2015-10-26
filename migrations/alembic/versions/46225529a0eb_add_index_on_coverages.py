"""Add index on coverages

Revision ID: 46225529a0eb
Revises: fos5a55d7a
Create Date: 2015-10-21 13:04:27.432973

"""

# revision identifiers, used by Alembic.
revision = '46225529a0eb'
down_revision = 'fos5a55d7a'

from alembic import op

def upgrade():
    op.create_index('coverages_request_id_idx', 'coverages', ['request_id'], schema='stat')


def downgrade():
    op.drop_index('coverages_request_id_idx', schema='stat')
