from src.database import repository
from src.database.session import Session

DEFAULT_SESSION = Session


class DatabaseService:
    item: repository.AbstractRepository

    def __init__(self, session=DEFAULT_SESSION):
        self.default_session = session

    def __enter__(self):
        self.session = self.default_session()
        self.item = repository.SqlAlchemyRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.session.close()
        else:
            self.rollback()
            self.session.close()

    def commit(self):
        self._commit()

    def rollback(self):
        self._rollback()

    def _rollback(self):
        self.session.rollback()

    def _commit(self):
        self.session.commit()
