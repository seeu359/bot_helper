import pytest
from datetime import date, timedelta

from src.domain import bussines_rules, exceptions, models


def test_format_data():
    assert bussines_rules.format_day(2, 'January') == '2023-01-02'


def test_incorrect_month_day():
    with pytest.raises(expected_exception=exceptions.InvalidDate):
        bussines_rules.format_day(30, 'February')


@pytest.mark.parametrize('value, expected',
                         [
                            (1, '01'),
                            (25, '25'),
                            (9, '09'),
                            (10, '10'),
                         ])
def test_normalize_day(value, expected):
    assert bussines_rules._normalize_day(value) == expected


def test_equal_user():
    user1 = models.User(username='test1', first_name='Alexey', last_name='Chere', id=123)
    user2 = models.User(username='test2', first_name='Ivan', last_name='Somename', id=123)
    assert user1 == user2


def test_expired_task_date():
    task_start_date = date.today() - timedelta(days=1)
    task = models.Task(
        start_date=task_start_date,
        title='Test',
        description='Description',
        user_id=1,
    )
    assert task.is_expired()

