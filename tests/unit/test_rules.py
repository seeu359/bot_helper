import pytest

from src.domain import bussines_rules, exceptions


def test_format_data():
    date = bussines_rules.format_day(2, 'January')
    assert date == '2023-01-02'


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