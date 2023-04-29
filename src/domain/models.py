from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, TypeVar, Iterable
from abc import ABC


EntityProperties = Any
TypeTask = TypeVar('TypeTask')


class Entity(ABC):
    id: EntityProperties

    def __repr__(self):
        fields = [f'{key}={value}' for key, value in self.__dict__.items()]
        return f'{self.__name__}({", ".join(fields)})'


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

    @staticmethod
    def get_expired_tasks(tasks: Iterable[TypeTask]) -> list[TypeTask]:
        return [task for task in tasks if task.is_expired()]

    @staticmethod
    def get_valid_tasks(tasks: Iterable[TypeTask]) -> list[TypeTask]:
        return [task for task in tasks if not task.is_expired()]

    def is_expired(self):
        return date.today() > self.start_date

    def __repr__(self):
        return super().__repr__()


@dataclass
class DoneTask(Task):
    completion_date: datetime = datetime.now()

    def __repr__(self):
        return super().__repr__()


@dataclass
class User(Entity):
    username: str = field(compare=False)
    first_name: str = field(compare=False)
    last_name: str = field(compare=False)
    id: int | None = field(compare=True, default=None)


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
