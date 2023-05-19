"""cpus table

Revision ID: ddb627d7ceab
Revises: 6788ba97dd83
Create Date: 2023-05-19 20:43:50.951204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddb627d7ceab'
down_revision = '6788ba97dd83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cpu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('Core', sa.String(length=64), nullable=True),
    sa.Column('number_of_cores', sa.String(length=64), nullable=True),
    sa.Column('number_of_threads', sa.String(length=64), nullable=True),
    sa.Column('Process_technology', sa.String(length=64), nullable=True),
    sa.Column('Connector', sa.String(length=64), nullable=True),
    sa.Column('Frequency', sa.String(length=64), nullable=True),
    sa.Column('Multiplier', sa.String(length=64), nullable=True),
    sa.Column('HTT_Bclk', sa.String(length=64), nullable=True),
    sa.Column('Memory_type', sa.String(length=64), nullable=True),
    sa.Column('L1_cache', sa.String(length=64), nullable=True),
    sa.Column('L2_cache', sa.String(length=64), nullable=True),
    sa.Column('L3_cache', sa.String(length=64), nullable=True),
    sa.Column('Supply_voltage', sa.String(length=64), nullable=True),
    sa.Column('TDP', sa.String(length=64), nullable=True),
    sa.Column('Number_of_transistors', sa.String(length=64), nullable=True),
    sa.Column('Crystal_area', sa.String(length=64), nullable=True),
    sa.Column('Limit_temperature', sa.String(length=64), nullable=True),
    sa.Column('Instruction_set', sa.String(length=64), nullable=True),
    sa.Column('Other_Features', sa.String(length=64), nullable=True),
    sa.Column('Date_of_issue', sa.String(length=64), nullable=True),
    sa.Column('Cost', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cpu', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cpu_name'), ['name'], unique=True)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_timestamp')

    op.drop_table('post')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))

    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index('ix_post_timestamp', ['timestamp'], unique=False)

    with op.batch_alter_table('cpu', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cpu_name'))

    op.drop_table('cpu')
    # ### end Alembic commands ###