"""highscore

Revision ID: 243b16e113f3
Revises: f657c70537f2
Create Date: 2019-04-19 13:56:56.372204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '243b16e113f3'
down_revision = 'f657c70537f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('highscore', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('highscore', 'rating')
    # ### end Alembic commands ###
