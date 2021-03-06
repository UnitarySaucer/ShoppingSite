"""associate user and reviews

Revision ID: 702ba72e371d
Revises: 19f22bfa630a
Create Date: 2021-10-17 19:02:21.902058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702ba72e371d'
down_revision = '19f22bfa630a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'reviews', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'user_id')
    # ### end Alembic commands ###
