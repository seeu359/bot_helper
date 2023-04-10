"""add username column in user table

Revision ID: 0f1c021d21c7
Revises: 4a434a112e79
Create Date: 2023-04-05 02:01:59.210913

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0f1c021d21c7'
down_revision = '4a434a112e79'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
