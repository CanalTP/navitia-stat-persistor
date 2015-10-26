"""Add index on journey_sections

Revision ID: 466453911d1c
Revises: 46225529a0eb
Create Date: 2015-10-26 09:40:36.708169

"""

# revision identifiers, used by Alembic.
revision = '466453911d1c'
down_revision = '46225529a0eb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('journey_sections_request_id_idx', 'journey_sections', ['request_id'], schema='stat')


def downgrade():
    op.drop_index('journey_sections_request_id_idx', schema='stat')
