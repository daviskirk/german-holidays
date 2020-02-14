
**NOTE:**
This library was born before there were better solutions that now exist. The
library [holidays](https://github.com/dr-prodigy/python-holidays) is better
maintained and more accurate and includes not only german holidays but many
other countries as well. I would suggest you use it instead.

German Bank Holidays
====================

```python
from german_holidays import get_german_holiday_calendar

# german holiday class for nordrhein-westfalen
cal_cls = get_german_holiday_calendar('NW')
cal = cal_cls()

print(cal.holidays())
```
