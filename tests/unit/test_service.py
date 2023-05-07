import pytest

from src.service import formatters as serv_formatters
from src.domain import models, exceptions
from src.database import formatters as db_formatters


def test_note_formatter():
    title = 'Test Note'
    description = 'Test description'
    note = models.Note(
        title=title,
        description=description,
        user_id=1,
        category_id=2,
    )
    formatter = serv_formatters.NoteFormatter()
    assert formatter.format(note) == f'Title: {title}\nDescription: {description}'


def test_date_or_datetime1():
    date = db_formatters.date_or_datetime(16, 'May')
    assert date() == '2023-05-16'


def test_date_or_datetime2():
    datetime = db_formatters.date_or_datetime(16, 'January', '19:00')
    assert datetime() == '2023-01-16 19:00'


def test_raise_in_date_or_datetime():
    with pytest.raises(exceptions.InvalidDate):
        date = db_formatters.date_or_datetime(31, 'April')
        date()
