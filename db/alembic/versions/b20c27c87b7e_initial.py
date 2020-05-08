"""Initial

Revision ID: b20c27c87b7e
Revises: 
Create Date: 2020-05-08 13:21:15.947310

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b20c27c87b7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tesera_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=250), nullable=True),
                    sa.Column('en_name', sa.String(length=250), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('photoUrl', sa.String(), nullable=True),
                    sa.Column('bgg_rating', sa.Float(), nullable=True),
                    sa.Column('min_players', sa.SmallInteger(), nullable=True),
                    sa.Column('min_players_recommended', sa.SmallInteger(), nullable=True),
                    sa.Column('max_players', sa.SmallInteger(), nullable=True),
                    sa.Column('max_players_recommended', sa.SmallInteger(), nullable=True),
                    sa.Column('play_time_min', sa.SmallInteger(), nullable=True),
                    sa.Column('play_time_max', sa.SmallInteger(), nullable=True),
                    sa.Column('tesera_url', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('en_name'),
                    sa.UniqueConstraint('name'),
                    sa.UniqueConstraint('tesera_id')
                    )
    op.create_table('game_category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('category_game_mtm',
                    sa.Column('game_category_id', sa.Integer(), nullable=True),
                    sa.Column('game_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['game_category_id'], ['game_category.id'], ),
                    sa.ForeignKeyConstraint(['game_id'], ['game.id'], )
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_game_mtm')
    op.drop_table('game_category')
    op.drop_table('game')
    # ### end Alembic commands ###