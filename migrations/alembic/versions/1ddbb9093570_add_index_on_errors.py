"""add index on errors to speed up purge

Revision ID: 1ddbb9093570
Revises: 372e4c6a8689
Create Date: 2016-03-15 10:51:01.745507

"""

# revision identifiers, used by Alembic.
revision = '1ddbb9093570'
down_revision = '372e4c6a8689'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('errors_request_id_idx', 'errors', ['request_id'], schema='stat')


def downgrade():
    op.drop_index('errors_request_id_idx', schema='stat')
