"""empty message

Revision ID: 6489c194e23a
Revises: 0cdd55c528ae
Create Date: 2023-05-06 23:19:41.606107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6489c194e23a'
down_revision = '0cdd55c528ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('algo_course', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'algo_course', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'algo_course', type_='foreignkey')
    op.drop_column('algo_course', 'user_id')
    # ### end Alembic commands ###