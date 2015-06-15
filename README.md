German Bank Holidays
====================

```python
from german_holidays import get_german_holiday_calendar

# german holiday class for nordrhein-westfalen
cal_cls = get_german_holiday_calendar('NW')
cal = cal_cls()

print(cal.holidays())
```
