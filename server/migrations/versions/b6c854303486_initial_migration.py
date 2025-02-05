"""initial migration

Revision ID: b6c854303486
Revises: 
Create Date: 2025-01-22 09:07:48.616935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6c854303486'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###
