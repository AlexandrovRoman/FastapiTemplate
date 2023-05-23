"""Test model

Revision ID: 3727b0fbed2b
Revises: 
Create Date: 2023-05-19 13:21:06.902977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3727b0fbed2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_table',
    sa.Column('test_field', sa.Integer(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('test_field')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_table')
    # ### end Alembic commands ###