from abc import ABC, abstractmethod
from typing import Iterable, Union
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain import models


class AbstractRepository(ABC):

    def __init__(self, session: Session):
        self.session = session

    def get_list(self, model, user_id: int, period: date | None = None):
        return self._get_list(model, user_id, period)

    def get(self, model, user_id: int, entity_id: int | None = None):
        return self._get(model, user_id, entity_id)

    def add(self, entity):
        self._add(entity)

    def done(self, done_task):
        self._done(done_task)

    def delete(self, task: models.Entity):
        self._delete(task)

    @abstractmethod
    def _get_list(
            self, model, user_id: int, period: date | None = None
    ) -> Iterable[models.Entity]:
        raise NotImplementedError

    @abstractmethod
    def _get(self, model, user_id: int, entity_id: int | None):
        raise NotImplementedError

    @abstractmethod
    def _add(self, entity):
        raise NotImplementedError

    @abstractmethod
    def _done(self, done_task):
        raise NotImplementedError

    def _delete(self, task):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def _get_list(self, model, user_id: int, period: date | None = None):
        if period is None:
            query = select(model).where(model.user_id == user_id)
        else:
            query = select(model).where(
                model.start_date == period, model.user_id == user_id
            )
        entities = self.session.scalars(query).all()
        return entities

    def _get(self, entity, user_id: int, entity_id: int | None):
        if entity_id is None:
            query = select(entity).where(
                entity.id == user_id,
            )
        else:
            query = select(entity).where(
                entity.id == entity_id,
                entity.user_id == user_id
            )
        entity = self.session.scalar(query)
        return entity

    def get_notes(self, user_id: int, category_id: int):
        query = select(models.Note).where(
            models.Note.user_id == user_id,
            models.Note.category_id == category_id
        )
        notes = self.session.scalars(query).all()
        return notes

    def _done(self, done_task) -> None:
        self._add(done_task)

    def _add(self, entity: Union[models.Task, models.Entity]):
        self.session.add(entity)

    def _delete(self, entity):
        self.session.delete(entity)
