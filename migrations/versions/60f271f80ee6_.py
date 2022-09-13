"""empty message

Revision ID: 60f271f80ee6
Revises: 3c2714f1e251
Create Date: 2022-09-08 04:38:50.399586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60f271f80ee6'
down_revision = '3c2714f1e251'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fridge', sa.Column('modify_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fridge', 'modify_date')
    # ### end Alembic commands ###