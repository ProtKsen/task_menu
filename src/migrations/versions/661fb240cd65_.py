"""

Revision ID: 661fb240cd65
Revises: cafe1db5d469
Create Date: 2023-07-23 14:27:02.002524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661fb240cd65'
down_revision = 'cafe1db5d469'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submenus', sa.Column('_dishes_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submenus', '_dishes_count')
    # ### end Alembic commands ###
