"""creating table in sqlite

Revision ID: 80cf41863ab1
Revises: 
Create Date: 2020-06-12 11:37:02.443481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80cf41863ab1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_iframe_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iframeID', sa.Integer(), nullable=False),
    sa.Column('iframeURL', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user_master',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loginID', sa.Integer(), nullable=False),
    sa.Column('emailID', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_dt', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user_login_audit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loginID', sa.Integer(), nullable=True),
    sa.Column('attemptedTimeStamp', sa.TIMESTAMP(), nullable=False),
    sa.Column('statusFlag', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['loginID'], ['tb_user_master.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loginID', sa.Integer(), nullable=True),
    sa.Column('userToken', sa.String(), nullable=False),
    sa.Column('expiryTimeStamp', sa.TIMESTAMP(), nullable=False),
    sa.Column('createdTimeStamp', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['loginID'], ['tb_user_master.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_user_token')
    op.drop_table('tb_user_login_audit')
    op.drop_table('tb_user_master')
    op.drop_table('tb_iframe_details')
    # ### end Alembic commands ###
