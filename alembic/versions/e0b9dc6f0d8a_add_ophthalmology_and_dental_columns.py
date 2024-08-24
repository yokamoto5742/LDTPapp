"""Add ophthalmology and dental columns

Revision ID: e0b9dc6f0d8a
Revises: 
Create Date: 2024-08-24 19:12:23.399140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0b9dc6f0d8a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient_info', sa.Column('ophthalmology', sa.Boolean(), nullable=True))
    op.add_column('patient_info', sa.Column('dental', sa.Boolean(), nullable=True))
    op.drop_column('templates', 'nonsmoker')
    op.drop_column('templates', 'smoking_cessation')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('templates', sa.Column('smoking_cessation', sa.BOOLEAN(), nullable=True))
    op.add_column('templates', sa.Column('nonsmoker', sa.BOOLEAN(), nullable=True))
    op.drop_column('patient_info', 'dental')
    op.drop_column('patient_info', 'ophthalmology')
    # ### end Alembic commands ###