from dataclasses import dataclass
from datetime import date, datetime
from typing import Any
from abc import ABC

EntityProperties = Any


class Entity(ABC):
    id: EntityProperties

    @classmethod
    def _get_cls_name(cls):
        return cls.__name__

    def __repr__(self):
        fields = [f'{items[0]}={items[1]}' for items in self.__dict__.items()]
        return f'{self._get_cls_name()}({", ".join(fields)})'


@dataclass
class Task(Entity):
    start_date: date
    title: str
    description: str
    user_id: int

    @classmethod
    def get_period(cls, period: str):
        match period:
            case 'Today tasks':
                return date.today()
            case _:
                return

    def is_expired(self, exp_date: date):
        return exp_date > self.start_date

    def __repr__(self):
        return super().__repr__()


@dataclass
class DoneTask(Task):
    completion_date: datetime = datetime.now()

    def __repr__(self):
        return super().__repr__()


@dataclass
class User(Entity):
    username: str
    first_name: str
    last_name: str
    id: int | None = None


@dataclass
class Note(Entity):
    title: str
    description: str
    category_id: int
    user_id: int


@dataclass
class NoteCategory(Entity):
    user_id: int
    name: str
