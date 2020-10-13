"""empty message

Revision ID: 157f87dc2ceb
Revises: 7eb25c2cc4d0
Create Date: 2020-10-12 18:29:03.687691

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '157f87dc2ceb'
down_revision = '7eb25c2cc4d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('papel', sa.String(), nullable=True),
    sa.Column('ativada', sa.Boolean(), nullable=False),
    sa.Column('ultimo_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('papel', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ativada', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('ultimo_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_model_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
