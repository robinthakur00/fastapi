"""add content column to posts table

Revision ID: 2e9da825bfb8
Revises: d519ce0f61bf
Create Date: 2021-11-19 23:52:37.804536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e9da825bfb8'
down_revision = 'd519ce0f61bf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
