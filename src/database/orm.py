import datetime

from sqlalchemy import (Column, Date, DateTime, ForeignKey, Integer, MetaData, String,
                        Table)
from sqlalchemy.orm import registry, relationship
from src.domain import models

metadata = MetaData()
mapper = registry()


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
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


done_task = Table(
    'done_task',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('start_date', Date),
    Column('completion_date', DateTime, default=datetime.datetime.now(), nullable=False),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('title', String, nullable=False),
    Column('description', String, nullable=True),
)


def start_mapping():
    user_mapper = mapper.map_imperatively(models.User, user)
    mapper.map_imperatively(models.DoneTask, done_task, properties={
        'user': relationship(user_mapper)
    })
    mapper.map_imperatively(models.Task, task, properties={
        'user': relationship(user_mapper),
    })
