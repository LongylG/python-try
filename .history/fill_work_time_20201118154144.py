import datetime
import chinese_calendar
import calendar
a = datetime.datetime.now()
b = chinese_calendar.is_holiday(a)
c = chinese_calendar.is_workday(a)

print(a)
print(b)
print(c)

# 根据开始日期、结束日期返回这段时间里所有天的集合


def getDatesByTimes(sDateStr, eDateStr):
    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        list.append(datestart.strftime('%Y-%m-%d'))
    return list


getDatesByTimes("2019-09-18",)
