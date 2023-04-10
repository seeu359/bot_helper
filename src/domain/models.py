from dataclasses import dataclass
from datetime import date


class Entity:
    id: int | None
    user_id: int | None
    start_date: int | None

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

    def __repr__(self):
        return super().__repr__()


class User(Entity):

    def __init__(self, id=None, username=None, first_name=None, last_name=None):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
