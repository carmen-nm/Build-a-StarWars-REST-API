"""empty message

Revision ID: 961def6643c8
Revises: eff0ff927d90
Create Date: 2022-11-27 16:22:46.335641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '961def6643c8'
down_revision = 'eff0ff927d90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('lastname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
