"""empty message

Revision ID: 6fb588e01149
Revises: 4c092b54a941
Create Date: 2019-06-04 20:47:44.290475

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6fb588e01149'
down_revision = '4c092b54a941'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'user', ['username'], unique=True)
    # ### end Alembic commands ###
