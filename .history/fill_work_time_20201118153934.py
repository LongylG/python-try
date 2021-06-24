import datetime
import chinese_calendar
import calendar
a = datetime.datetime.now()
b = chinese_calendar.is_holiday(a)
c = chinese_calendar.is_workday(a)

print(a)
print(b)
print(c)

month = calendar.month(2020, 9).format
print(month)
