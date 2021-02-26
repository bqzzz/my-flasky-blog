"""0210_2

Revision ID: 208a62785cec
Revises: 735c05d56696
Create Date: 2021-02-10 13:58:33.186574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '208a62785cec'
down_revision = '735c05d56696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
