from sqlalchemy import (Column, Date, ForeignKey, Integer, MetaData, String,
                        Table)
from sqlalchemy.orm import registry, relationship

from src.domain import models

metadata = MetaData()
mapper = registry()


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String),
    Column('first_name', String),
    Column('last_name', String),
)


task = Table(
    'task',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('start_date', Date, nullable=False),
    Column('title', String, nullable=False),
    Column('description', String, nullable=True),
)


def start_mapping():
    user_mapper = mapper.map_imperatively(models.User, user)
    mapper.map_imperatively(models.Task, task, properties={
        'user': relationship(user_mapper),
    })
