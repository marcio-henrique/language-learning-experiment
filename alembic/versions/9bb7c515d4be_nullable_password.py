"""nullable password

Revision ID: 9bb7c515d4be
Revises: ad036d1956fe
Create Date: 2025-05-03 18:29:03.522841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9bb7c515d4be'
down_revision: Union[str, None] = 'ad036d1956fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'password_hash',
    existing_type=sa.String(),
    nullable=True
)



def downgrade() -> None:
    op.alter_column('users', 'password_hash',
    existing_type=sa.String(),
    nullable=False
)

