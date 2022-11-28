"""empty message

Revision ID: 2178c3c593ad
Revises: 7aab3be754dc
Create Date: 2022-11-27 17:02:47.306164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2178c3c593ad'
down_revision = '7aab3be754dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
