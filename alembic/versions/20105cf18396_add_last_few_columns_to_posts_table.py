"""add last few columns to posts table

Revision ID: 20105cf18396
Revises: c6b8f99e020d
Create Date: 2021-11-20 00:21:59.365073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20105cf18396'
down_revision = 'c6b8f99e020d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
