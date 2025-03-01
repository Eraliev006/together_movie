"""film genre association table

Revision ID: 4ca933a35408
Revises: 41cf6ea245d0
Create Date: 2025-02-08 11:01:17.390369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ca933a35408'
down_revision: Union[str, None] = '41cf6ea245d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('original_title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('poster_url', sa.String(), nullable=True),
    sa.Column('trailer_url', sa.String(), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('age_rating', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_films_title'), 'films', ['title'], unique=False)
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('film_genres_association',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'genre_id')
    )
    op.alter_column('rooms', 'slug',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'slug',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('film_genres_association')
    op.drop_table('genres')
    op.drop_index(op.f('ix_films_title'), table_name='films')
    op.drop_table('films')
    # ### end Alembic commands ###
