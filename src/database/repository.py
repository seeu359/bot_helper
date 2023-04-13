from abc import ABC, abstractmethod
from typing import Iterable, Type
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain import models
from src.domain.models import Entity


class AbstractRepository(ABC):

    def get_list(
            self, model: Type[models.Entity],
            user_id: int,
            period: date | None = None):
        return self._get_list(model, user_id, period)

    def get(self, model: Type[models.Entity], entity_id: int) -> models.Entity:
        return self._get(model, entity_id)

    def add(self, entity: Entity):
        self._add(entity)

    def done(self, entity: Entity):
        self._done(entity)

    @abstractmethod
    def _get_list(
            self, model: Type[models.Entity],
            user_id: int,
            period: date | None = None
    ) -> Iterable[models.Entity]:
        raise NotImplementedError

    @abstractmethod
    def _get(self, model: Type[models.Entity], entity_id: int):
        raise NotImplementedError

    @abstractmethod
    def _add(self, entity: Entity):
        raise NotImplementedError

    @abstractmethod
    def _done(self, entity: Entity):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session):
        self.session = session

    def _get_list(
            self,
            model: Type[models.Entity],
            user_id: int,
            period: date | None = None):

        if period is None:
            query = select(model).where(model.user_id == user_id)
        else:
            query = select(model).where(model.start_date == period, model.user_id == user_id)
        entities = self.session.scalars(query).all()
        return entities

    def _get(self, model: Type[models.Entity], entity_id: int) -> models.Entity:
        query = select(model).where(model.id == entity_id)
        entity = self.session.scalar(query)
        return entity

    def _done(self, entity: Entity):
        pass

    def _add(self, entity: Entity):
        self.session.add(entity)
