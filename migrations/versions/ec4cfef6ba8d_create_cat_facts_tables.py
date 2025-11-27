"""create cat facts tables

Revision ID: ваш_revision_id
Revises: 
Create Date: 2024-01-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'ваш_revision_id'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('cat_facts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fact', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='lr3_schema'
    )
    op.create_index('ix_cat_facts_id', 'cat_facts', ['id'], unique=False, schema='lr3_schema')
    
    op.create_table('cat_fact_stats',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('total_facts', sa.Integer(), nullable=True),
        sa.Column('last_updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='lr3_schema'
    )
    op.create_index('ix_cat_fact_stats_id', 'cat_fact_stats', ['id'], unique=False, schema='lr3_schema')


def downgrade() -> None:
    op.drop_index('ix_cat_fact_stats_id', table_name='cat_fact_stats', schema='lr3_schema')
    op.drop_table('cat_fact_stats', schema='lr3_schema')
    op.drop_index('ix_cat_facts_id', table_name='cat_facts', schema='lr3_schema')
    op.drop_table('cat_facts', schema='lr3_schema')