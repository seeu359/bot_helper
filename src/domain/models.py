from dataclasses import dataclass
from datetime import date, datetime
from typing import Any
from abc import ABC, abstractmethod

EntityProperties = Any


class Entity(ABC):
    id: EntityProperties

    @classmethod
    def _get_cls_name(cls):
        return cls.__name__

    def to_dict(self):
        return self._to_dict()

    @abstractmethod
    def _to_dict(self):
        raise NotImplementedError

    def __repr__(self):
        fields = [f'{items[0]}={items[1]}' for items in self.__dict__.items()]
        return f'{self._get_cls_name()}({", ".join(fields)})'


@dataclass
class Task(Entity):
    start_date: int
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

    def _to_dict(self):
        return {
            'start_date': self.start_date,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id
        }

    def __repr__(self):
        return super().__repr__()


@dataclass
class DoneTask(Task):
    completion_date = datetime.now()

    def _to_dict(self):
        fields = super()._to_dict()
        fields['completion_date'] = self.completion_date

    def __repr__(self):
        return super().__repr__()


class User(Entity):

    def __init__(self, id=None, username=None, first_name=None, last_name=None):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def _to_dict(self):
        pass
