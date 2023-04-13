import calendar
from datetime import date

from src.domain import exceptions

YEAR = date.today().year

MONTH_MAPPER = {
        'January': ('01', calendar.monthrange(YEAR, 1)[1]),
        'February': ('02', calendar.monthrange(YEAR, 2)[1]),
        'March': ('03', calendar.monthrange(YEAR, 3)[1]),
        'April': ('04', calendar.monthrange(YEAR, 4)[1]),
        'May': ('05', calendar.monthrange(YEAR, 5)[1]),
        'June': ('06', calendar.monthrange(YEAR, 6)[1]),
        'July': ('07', calendar.monthrange(YEAR, 7)[1]),
        'August': ('08', calendar.monthrange(YEAR, 8)[1]),
        'September': ('09', calendar.monthrange(YEAR, 9)[1]),
        'October': ('10', calendar.monthrange(YEAR, 10)[1]),
        'November': ('11', calendar.monthrange(YEAR, 11)[1]),
        'December': ('12', calendar.monthrange(YEAR, 12)[1])
    }


def format_day(day: int, month: str):
    _check_day(day, month)
    day = _normalize_day(day)
    month = MONTH_MAPPER[month][0]
    return f'{YEAR}-{month}-{day}'


def _check_day(day: int, month: str) -> None:
    exception = exceptions.InvalidDate
    max_day_in_month = MONTH_MAPPER[month][1]
    if day <= 0:
        raise exception(
            'Day must be greater than 0'
        )
    if day > max_day_in_month:
        raise exception(
            'Max day in %s - %s. Passed value %s' % (
                month, max_day_in_month, day
            )
        )


def _normalize_day(day: int) -> str:
    if len(str(day)) == 1:
        return f'0{day}'
    return str(day)
