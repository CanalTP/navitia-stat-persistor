"""Add index on info_response

Revision ID: 372e4c6a8689
Revises: 130355168524
Create Date: 2015-12-02 16:59:07.504196

"""

# revision identifiers, used by Alembic.
revision = '372e4c6a8689'
down_revision = '26052d62719'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('info_response_request_id_idx', 'info_response', ['request_id'], schema='stat')


def downgrade():
    op.drop_index('info_response_request_id_idx', schema='stat')
