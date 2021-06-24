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
    url = 'https://redcs.tencent.com/deliver/timesheet'

    for d in dateLists:
        body = '{"qflow_task_id":"105288","order_id":"TS20201112105288","ltc_id":"20190604117564","project_name":"长沙城市超级大脑（数据大脑平台+部分智慧应用）","service_sub":"交付实施","task_name":"长沙城市超级大脑（数据大脑平台+部分智慧应用）_B类_其他_小程序开发-定制开发和集成交付-长沙超脑_2020/11/12","in_team":"是","spent_person":"p_liyulong","data":[{"spent_date":"2019-09-18","deliver_stage":"开发阶段-代码开发","spent_length":8,"mark":"应用开发、前端框架构建、后台编程语言开发等技术支持技术经理，小程序开发-交付实施服务","stage_desc":"客户如有除产品标准功能外的额外需求而必要进行的二次开发","spent_desc":"与客户业务代表沟通，厘清本次二次开发需求，制定二次开发计划"}],"type":"1","sub_type":""}'
