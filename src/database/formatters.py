from src.domain import bussines_rules


def date_or_datetime(day: int, month: str, time=None) -> callable:
    def inner():
        bussines_rules.check_day(day, month)
        _month = bussines_rules.get_month(month)
        _day = str(day) if len(str(day)) == 2 else f'{0}day'
        if time is None:
            return f'{bussines_rules.YEAR}-{_month}-{_day}'
        else:
            return f'{bussines_rules.YEAR}-{_month}-{_day} {time}'
    return inner
