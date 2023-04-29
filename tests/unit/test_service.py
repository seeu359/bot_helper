from src.service import formatters
from src.domain import models


def test_note_formatter():
    title = 'Test Note'
    description = 'Test description'
    note = models.Note(
        title=title,
        description=description,
        user_id=1,
        category_id=2,
    )
    formatter = formatters.NoteFormatter()
    assert formatter.format(note) == f'Title: {title}\nDescription: {description}'
