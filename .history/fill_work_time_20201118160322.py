import json
import datetime
import chinese_calendar
import calendar
import requests


# 根据开始日期、结束日期返回这段时间里所有工作日集合


def getDatesByTimes(sDateStr, eDateStr):
    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    if(chinese_calendar.is_workday(datestart)):
        list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        if(chinese_calendar.is_workday(datestart)):
            list.append(datestart.strftime('%Y-%m-%d'))
    return list


workDateList = getDatesByTimes("2019-09-18", "2020-10-01")

# post(workDateList)
# 发送填报请求


def post(dateLists):
    for d in dateLists:
