from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
property = Table('property', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('address', VARCHAR(length=500)),
    Column('start_date', DATETIME),
    Column('duration', INTEGER),
    Column('rent', FLOAT),
)

profile = Table('profile', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=500)),
    Column('age', Integer),
    Column('course', String(length=100)),
    Column('graduation', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['property'].drop()
    post_meta.tables['profile'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['property'].create()
    post_meta.tables['profile'].drop()
