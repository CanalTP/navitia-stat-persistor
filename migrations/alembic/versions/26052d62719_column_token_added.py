"""column token added

Revision ID: 26052d62719
Revises: 130355168524
Create Date: 2016-01-04 15:18:16.869057

"""

# revision identifiers, used by Alembic.
revision = '26052d62719'
down_revision = '130355168524'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(u'requests', sa.Column('token', sa.Text(), nullable=True), schema='stat')


def downgrade():
    op.drop_column(u'requests', 'token', schema='stat')
