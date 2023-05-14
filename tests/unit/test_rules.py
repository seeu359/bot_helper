import pytest
from datetime import date, datetime, timedelta

from src.domain import models
from src.domain.business_layer.algo_courses import AlgoCourseData


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


def test_get_expired_task():
    tasks = []
    for delta in range(3):
        start_date = date.today() - timedelta(days=delta)
        task = models.Task(
            title='Test',
            description='Description',
            start_date=start_date,
            user_id=delta,
        )
        tasks.append(task)
    expired_tasks = models.Task.get_expired_tasks(tasks)
    expired_tasks_id = [task.user_id for task in expired_tasks]
    assert len(expired_tasks) == 2
    assert 1 in expired_tasks_id and 2 in expired_tasks_id
    assert 0 not in expired_tasks_id


@pytest.mark.parametrize('premium, expected',
                         [
                             (True, 3250),
                             (False, 2250),
                         ]
                         )
def test_get_algo_course_salary(premium, expected):
    algo_course = models.AlgoCourse(
        datetime=datetime.today(), premium=premium, user_id=1, course_id=1
    )
    course_data = AlgoCourseData(algo_course=algo_course)
    assert course_data.salary() == expected
