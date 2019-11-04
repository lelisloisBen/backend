"""empty message

Revision ID: d051db139a39
Revises: cd73dfec2e06
Create Date: 2019-11-02 18:11:04.757455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd051db139a39'
down_revision = 'cd73dfec2e06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('current_washing', sa.Column('end', sa.BigInteger(), nullable=True))
    op.add_column('current_washing', sa.Column('start', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('current_washing', 'start')
    op.drop_column('current_washing', 'end')
    # ### end Alembic commands ###