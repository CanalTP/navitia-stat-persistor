"""Cleanup some useless indexes

Revision ID: 130355168524
Revises: 466453911d1c
Create Date: 2015-10-28 14:37:26.677732

"""

# revision identifiers, used by Alembic.
revision = '130355168524'
down_revision = '466453911d1c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_index('coverages_region_id_idx', schema='stat')
    op.drop_index('journey_sections_from_admin_id_idx', schema='stat')
    op.drop_index('requests_user_id_idx', schema='stat')


def downgrade():
    op.create_index('coverages_region_id_idx', 'coverages', ['region_id'], schema='stat')
    op.create_index('journey_sections_from_admin_id_idx', 'journey_sections', ['from_admin_id'], schema='stat')
    op.create_index('requests_user_id_idx', 'requests', ['user_id'], schema='stat')
