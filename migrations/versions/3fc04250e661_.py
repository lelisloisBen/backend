"""empty message

Revision ID: 3fc04250e661
Revises: cbe17ec94956
Create Date: 2019-11-05 15:59:23.303104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc04250e661'
down_revision = 'cbe17ec94956'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('current_washing', sa.Column('userEmail', sa.String(length=220), nullable=True))
    op.add_column('current_washing', sa.Column('userID', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('current_washing', 'userID')
    op.drop_column('current_washing', 'userEmail')
    # ### end Alembic commands ###