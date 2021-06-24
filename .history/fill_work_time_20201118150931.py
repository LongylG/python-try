import datetime
import chinese_calendar
a = datetime.datetime.today()
b = chinese_calendar.is_holiday(a)
c = chinese_calendar.is_workday(a)

print(a)
print(b)
print(c)
