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
    'Tag der Arbeit': Holiday('Tag der Arbeit', month=5, day=1),
    'Erster Weihnachtstag': Holiday('Erster Weihnachtstag', month=12, day=25),
    'Zweiter Weihnachtstag': Holiday('Zweiter Weihnachtstag', month=12, day=26),
    'Heilige Drei Könige': Holiday('Heilige Drei Könige', month=1, day=6),
    'Mariä Himmelfahrt': Holiday('Mariä Himmelfahrt', month=8, day=15),
    'Tag der Deutschen Einheit': Holiday('Tag der Deutschen Einheit',
                                         month=10, day=3),
    'Reformationstag': Holiday('Reformationstag', month=10, day=31),
    '500. Reformationstag': Holiday('Reformationstag', year=2017, month=10, day=31),
    'Allerheiligen': Holiday('Allerheiligen', month=11, day=1),
    'Buß- und Bettag': Holiday('Buß- und Bettag', month=11, day=15,
                               offset=[Week(weekday=2)]),
}


HOLIDAY_EXCLUDE_MAP = {
    'BW': {'Mariä Himmelfahrt',
           'Reformationstag',
           'Buß- und Bettag'},
    'BY': {'Mariä Himmelfahrt',
           'Reformationstag',
           'Buß- und Bettag'},
    'BE': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'BB': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Allerheiligen',
           'Buß- und Bettag'},
    'HB': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'HH': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'HE': {'Heilige Drei Könige',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'MV': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Allerheiligen',
           'Buß- und Bettag'},
    'NI': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'NW': {'Heilige Drei Könige',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Buß- und Bettag'},
    'RP': {'Heilige Drei Könige',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Buß- und Bettag'},
    'SL': {'Heilige Drei Könige',
           'Reformationstag',
           'Buß- und Bettag'},
    'SN': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Allerheiligen'},
    'ST': {'Fronleichnam',
           'Mariä Himmelfahrt',
           'Allerheiligen',
           'Buß- und Bettag'},
    'SH': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Reformationstag',
           'Allerheiligen',
           'Buß- und Bettag'},
    'TH': {'Heilige Drei Könige',
           'Fronleichnam',
           'Mariä Himmelfahrt',
           'Allerheiligen',
           'Buß- und Bettag'},
}

# Add the special 500th Reformation day for states where the
# Reformation day is not already a holiday
for excluded_holidays in HOLIDAY_EXCLUDE_MAP.values():
    if 'Reformationstag' not in excluded_holidays:
        excluded_holidays.add('500. Reformationstag')

HOLIDAY_MAP = {k: (set(ALL_GERMAN_HOLIDAY_RULES.keys()) - v)
               for k, v in HOLIDAY_EXCLUDE_MAP.items()}


def get_german_holiday_calendar(state_code):
    """Get german holiday calendar class for a specific state.

    Valid state code abbreviations are found in the ``STATE_CODE_MAP``.

    Examples:
        Get a pandas datetime index of holidays:

        .. ::

           pandas_calendar_cls = get_german_holiday_calendar('NW')
           # results in a pandas datetime index:
           holidays = pandas_calendar_cls().holidays('2015', '2015-12-31')

    """
    if state_code not in STATE_CODE_MAP:
        raise StateCodeError('', state_code)

    class GermanBankHolidays(AbstractHolidayCalendar):
        rules = [ALL_GERMAN_HOLIDAY_RULES[name]
                 for name in HOLIDAY_MAP[state_code]]

    return GermanBankHolidays
