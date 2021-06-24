import json
import datetime
import chinese_calendar
import calendar
import requests
# import urllib.request
import urllib
import urllib3.poolmanager

# 根据开始日期、结束日期返回这段时间里所有工作日集合


cookie = 'session_id_uv_pv=Veer7hec; last_renew_time=1606128065243; session_id=eyJpdiI6InlYNWpkMjJiR0tKeEdLS25EWlNcLzBRPT0iLCJ2YWx1ZSI6IlFVWkF1RzJOeVRnYTBETWxNV1daWUVmalFzNmNcL3p2bG1QZTdCSDdob0NnVTVCZThsMkVnREpEb051OCt4djZlUnN6N2VGQW5MZjZCZGRGR3RPRSt2UT09IiwibWFjIjoiMjI0MDJmYjg5ODU4NGFjYWY3NDY1NTkzNjEyYWJlYzNiZTU1OGY1MTExOTZlMTI3Nzc4Y2UzYTZmMzQyNzQzYyJ9'


def getDatesByTimes(sDateStr, eDateStr):
    # 填写天数
    max = 1

    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    if(chinese_calendar.is_workday(datestart)):
        list.append(datestart.strftime('%Y-%m-%d'))
        max = max - 1
    while datestart < dateend:
        if (max == 0):
            return list
        datestart += datetime.timedelta(days=1)
        if(chinese_calendar.is_workday(datestart)):
            list.append(datestart.strftime('%Y-%m-%d'))
            max = max - 1
    return list


# 批量填报相同内容工时,使用时先在页面抓取请求
def fill_work(dateLists):
    """
        body变量参数在列表页面获取
        https://redcs.tencent.com/workbench/task-list/
    """
    url = 'https://redcs.tencent.com/deliver/timesheet'
    stage = '开发阶段-代码开发'
    mark = '应用开发、前端框架构建、后台编程语言开发等技术支持技术经理，小程序开发-交付实施服务'
    _id = '105288'
    orderId = 'TS20201112105288'
    ltcCode = '20190604117564'
    name = '长沙城市超级大脑（数据大脑平台+部分智慧应用）'
    taskName = '长沙城市超级大脑（数据大脑平台+部分智慧应用）_B类_其他_小程序开发-定制开发和集成交付-长沙超脑_2020/11/12'
    pCount = 'p_liyulong'
    for d in dateLists:
        body = {"qflow_task_id": _id, "order_id": orderId, "ltc_id": ltcCode, "project_name": name,
                "service_sub": "交付实施", "task_name": taskName, "in_team": "是", "spent_person": pCount,
                "data": [{"spent_date": d, "deliver_stage": stage, "spent_length": 8, "mark": "应用开发、前端框架构建、后台编程语言开发等技术支持技术经理，小程序开发-交付实施服务", "stage_desc": "客户如有除产品标准功能外的额外需求而必要进行的二次开发", "spent_desc": "与客户业务代表沟通，厘清本次二次开发需求，制定二次开发计划"}], "type": "1", "sub_type": ""}
        headers = {'cookie': cookie,
                   'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
                   'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response.json())

# 批量删除工时


def del_error_time(ids):
    base_url = 'https://redcs.tencent.com/deliver/timesheet/'
    for id in ids:
        headers = {'cookie': cookie,
                   'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
                   'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        url = base_url + id
        http = urllib3.PoolManager(num_pools=5, headers=headers)
        response = http.request('GET', url)
        print(response.json)


def get_month_ids(start_time, end_time):
    orderId = 'TS20201112105288'
    spent_person = 'p_jinquanlu'
    base_url = 'https://redcs.tencent.com/deliver/timesheet?spent_date_start={start_time}&spent_date_end={end_time}&type=1&order_id={order_id}&spent_person={person}&ignore_mine=1&page=1&size=50'
    headers = {'cookie': cookie,
               'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
               'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    http = urllib3.PoolManager(num_pools=5, headers=headers)
    response = http.request('DELETE', base_url)
    print(response.status)


get_month_ids("2019-08-01", '2019-09-01')

##workDateList = getDatesByTimes("2020-04-15", "2020-07-31")
# print(workDateList)
# print(len(workDateList))
# fill_work(workDateList)
# ids = ['46887701', '46887700', '46887703',
#        '46887704', '46887705', '46887706', '46887707']
# del_error_time(ids)
