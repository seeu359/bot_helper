from abc import ABC, abstractmethod
from collections.abc import Iterable
from datetime import datetime

from src.domain import models


class Presenter(ABC):
    item: models.Entity
    date_format = "%B %-d, %H:%M"

    def format_date(self, date: datetime.date):
        return date.strftime(self.date_format)

    def format(self, entity: models.Entity):
        return self._format(entity)

    def format_all(self, objects: Iterable[models.Entity]):
        if not isinstance(objects, Iterable):
            raise ValueError('Entities must be iterable object')
        for obj in objects:
            if not isinstance(obj, models.Entity):
                raise ValueError(f'<{obj}> must be entity type')
        return self._format_all(objects)

    @abstractmethod
    def _format(self, entity: models.Entity):
        raise NotImplementedError

    @abstractmethod
    def _format_all(self, entities: Iterable[models.Entity]):
        raise NotImplementedError


class TaskFormatter(Presenter):

    def _format_all(self, tasks: Iterable[models.Task]):
        result = ''

        for index, task in enumerate(tasks):
            result += f'{index + 1}) {self.format_date(task.start_date)} - {task.title}\n'
        return result

    def _format(self, task: models.Task):
        return f'Start time: {self.format_date(task.start_date)}\n' \
               f'Title: {task.title}' \
               f'\nDescription: {task.description}'


class NoteFormatter(Presenter):

    def _format_all(self, objects: Iterable[models.Entity]):
        pass

    def _format(self, note: models.Note):
        return f'Title: {note.title}\n' \
               f'Description: {note.description}'
