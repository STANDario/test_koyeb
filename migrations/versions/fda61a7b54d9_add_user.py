"""add User

Revision ID: fda61a7b54d9
Revises: 6b33a7537070
Create Date: 2023-12-17 18:56:31.025347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fda61a7b54d9'
down_revision: Union[str, None] = '6b33a7537070'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('tags', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('tags_name_key', 'tags', type_='unique')
    op.create_unique_constraint('unique_tag_user', 'tags', ['name', 'user_id'])
    op.create_foreign_key(None, 'tags', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.drop_constraint('unique_tag_user', 'tags', type_='unique')
    op.create_unique_constraint('tags_name_key', 'tags', ['name'])
    op.drop_column('tags', 'user_id')
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
