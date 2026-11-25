
"""add llm_calls

Revision ID: 70f87a82a7a6
Revises: 636040cf9f90
Create Date: 2026-11-25 20:15:14.070423
"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "70f87a82a7a6"
down_revision: Union[str, Sequence[str], None] = "636040cf9f90"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """No schema changes required; previous migration handles these tables."""
    pass


def downgrade() -> None:
    """No schema changes to reverse."""
    pass
