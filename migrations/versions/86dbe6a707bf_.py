"""empty message

Revision ID: 86dbe6a707bf
Revises: 09dcc15df575
Create Date: 2019-01-04 21:13:06.985688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86dbe6a707bf'
down_revision = '09dcc15df575'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###
