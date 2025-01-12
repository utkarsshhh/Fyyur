"""empty message

Revision ID: a8ad9f5d73b5
Revises: 937e32f892fc
Create Date: 2024-03-08 15:35:21.809397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ad9f5d73b5'
down_revision = '937e32f892fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website', sa.String(length=400), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('website')

    # ### end Alembic commands ###
