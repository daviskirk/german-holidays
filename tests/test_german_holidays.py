"""Testing basic functionality."""

import pandas as pd

from german_holidays import get_german_holiday_calendar


def test_basic():
    """Test example from docstring."""
    pandas_calendar_cls = get_german_holiday_calendar('NW')
    holidays = pandas_calendar_cls().holidays('2015', '2015-12-31')

    assert isinstance(holidays, pd.DatetimeIndex)
    expected = pd.DatetimeIndex(['2015-01-01', '2015-04-03', '2015-04-06', '2015-05-01',
                                 '2015-05-14', '2015-05-25', '2015-06-04', '2015-10-03',
                                 '2015-11-01', '2015-12-25', '2015-12-26'])
    pd.util.testing.assert_index_equal(holidays, expected)
