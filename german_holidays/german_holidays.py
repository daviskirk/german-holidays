# -*- coding: utf-8 -*-

"""
German bank holiday.
"""


try:
    from pandas import Timedelta
    from pandas.tseries.offsets import Easter, Day, Week
    from pandas.tseries.holiday import EasterMonday, GoodFriday, \
        Holiday, AbstractHolidayCalendar
except ImportError:
    print('Pandas could not be imported')
    raise
from german_holidays.state_codes import STATE_CODE_MAP, StateCodeError


class ChristiHimmelfahrt(Easter):
    def apply(*args, **kwargs):
        new = Easter.apply(*args, **kwargs)
        new += Timedelta('39d')
        return new


class Pfingstsonntag(Easter):
    def apply(*args, **kwargs):
        new = Easter.apply(*args, **kwargs)
        new += Timedelta('49d')
        return new


class Pfingstmontag(Easter):
    def apply(*args, **kwargs):
        new = Easter.apply(*args, **kwargs)
        new += Timedelta('50d')
        return new


class Fronleichnam(Easter):
    def apply(*args, **kwargs):
        new = Easter.apply(*args, **kwargs)
        new += Timedelta('60d')
        return new


ALL_GERMAN_HOLIDAY_RULES = {
    'Karfreitag': GoodFriday,
    # 'Ostersonntag': Holiday('Ostersonntag', month=1, day=1,
    #                         offset=[Easter()]),
    'Ostermontag': EasterMonday,
    'Christi Himmelfahrt': Holiday('Christi Himmelfahrt', month=1, day=1,
                                   offset=[Easter(), Day(39)]),
    # 'Pfingstsonntag': Holiday('Pfingstsonntag', month=1, day=1,
    #                           offset=[Easter(), Day(49)]),
    'Pfingstmontag': Holiday('Pfingstmontag', month=1, day=1,
                             offset=[Easter(), Day(50)]),
    'Fronleichnam': Holiday('Fronleichnam', month=1, day=1,
                            offset=[Easter(), Day(60)]),
    'Neujahrstag': Holiday('Neujahrstag', month=1, day=1),
    '1. Mai': Holiday('1. Mai', month=5, day=1),
    'Erster Weihnachtstag': Holiday('Erster Weihnachtstag', month=12, day=25),
    'Zweiter Weihnachtstag': Holiday('Zweiter Weihnachtstag', month=12, day=26),
    'Heilige Drei Koenige': Holiday('Heilige Drei Koenige', month=1, day=6),
    'Maria Himmelfahrt': Holiday('Maria Himmelfahrt', month=8, day=15),
    'Tag der Deutschen Einheit': Holiday('Tag der Deutschen Einheit',
                                         month=10, day=3),
    'Reformationstag': Holiday('Reformationstag', month=10, day=31),
    '500. Reformationstag': Holiday('Reformationstag', year=2017, month=10, day=31),
    'Allerheiligen': Holiday('Allerheiligen', month=11, day=1),
    'Buss und Bettag': Holiday('Buss und Bettag', month=11, day=15,
                               offset=[Week(weekday=2)]),
}


HOLIDAY_EXCLUDE_MAP = {
    'BW': {'Maria Himmelfahrt',
           'Reformationstag',
           'Buss und Bettag'},
    'BY': {'Maria Himmelfahrt',
           'Reformationstag',
           'Buss und Bettag'},
    'BE': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'BB': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Allerheiligen',
           'Buss und Bettag'},
    'HB': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'HH': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'HE': {'Heilige Drei Koenige',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'MV': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Allerheiligen',
           'Buss und Bettag'},
    'NI': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'NW': {'Heilige Drei Koenige',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Buss und Bettag'},
    'RP': {'Heilige Drei Koenige',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Buss und Bettag'},
    'SL': {'Heilige Drei Koenige',
           'Reformationstag',
           'Buss und Bettag'},
    'SN': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Allerheiligen'},
    'ST': {'Fronleichnam',
           'Maria Himmelfahrt',
           'Allerheiligen',
           'Buss und Bettag'},
    'SH': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buss und Bettag'},
    'TH': {'Heilige Drei Koenige',
           'Fronleichnam',
           'Maria Himmelfahrt',
           'Allerheiligen',
           'Buss und Bettag'},
}

# Add the special 500th Reformation day for states where the
# Reformation day is not already a holiday
for excluded_holidays in HOLIDAY_EXCLUDE_MAP.values():
    if 'Refomationstag' not in excluded_holidays:
        excluded_holidays.add('500. Refomationstag')

HOLIDAY_MAP = {k: (set(ALL_GERMAN_HOLIDAY_RULES.keys()) - v)
               for k, v in HOLIDAY_EXCLUDE_MAP}


def get_german_holiday_calendar(state_code):
    if state_code not in STATE_CODE_MAP:
        raise StateCodeError('', state_code)

    class GermanBankHolidays(AbstractHolidayCalendar):
        rules = [ALL_GERMAN_HOLIDAY_RULES[name]
                 for name in HOLIDAY_MAP[state_code]]

    return GermanBankHolidays
