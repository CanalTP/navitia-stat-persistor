"""Remove obsolete indexes

Revision ID: 20cd91cbf353
Revises: 1ddbb9093570
Create Date: 2016-07-04 14:14:37.873240

"""

# revision identifiers, used by Alembic.
revision = '20cd91cbf353'
down_revision = '1ddbb9093570'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_index('journey_sections_type_idx', schema='stat')
    op.drop_index('requests_user_name_idx', schema='stat')
    op.drop_index('requests_api_idx', schema='stat')


def downgrade():
    op.create_index('journey_sections_type_idx', 'journey_sections', ['type'], schema='stat')
    op.create_index('requests_user_name_idx', 'requests', ['user_name'], schema='stat')
    op.create_index('requests_api_idx', 'requests', ['api'], schema='stat')
