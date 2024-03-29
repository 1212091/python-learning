"""empty message

Revision ID: d911129ddc16
Revises: 7f590e6b7b08
Create Date: 2019-08-19 09:37:45.065714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd911129ddc16'
down_revision = '7f590e6b7b08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('seat', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
