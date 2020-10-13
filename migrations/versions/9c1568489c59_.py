"""empty message

Revision ID: 9c1568489c59
Revises: cac9c256e651
Create Date: 2020-10-12 21:09:01.212044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1568489c59'
down_revision = 'cac9c256e651'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('papel', sa.String(), nullable=True),
    sa.Column('ativada', sa.Boolean(), nullable=False),
    sa.Column('ultimo_login', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
