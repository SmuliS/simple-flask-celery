"""Add task table

Revision ID: b53834e8f8f1
Revises:
Create Date: 2016-01-10 21:37:12.119328

"""

# revision identifiers, used by Alembic.
revision = 'b53834e8f8f1'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'task',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=80), nullable=True),
        sa.Column('description', sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('task')
