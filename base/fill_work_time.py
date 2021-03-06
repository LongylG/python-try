import json
import datetime
import chinese_calendar
import calendar
import requests
# import urllib.request
import urllib
import urllib3.poolmanager
import random


cookie = '_ga=GA1.2.728526774.1599552504; pgv_pvi=4806563840; _gcl_au=1.1.1348498311.1599552521; _qddaz=QD.123299702982053; __root_domain_v=.tencent.com; pgv_pvid=9554451120; pgv_si=s4344743936; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100011561420%22%2C%22first_id%22%3A%2259929ffdd3744294bb6eacc05430cb3c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%221746cc242705a-0506bb2a4503c4-15336251-1296000-1746cc24271b38%22%7D; session_id_uv_pv=y3dh4lRh; session_id=eyJpdiI6IkhrUnJlREx5SnVsUnBvbHJLMmtvbFE9PSIsInZhbHVlIjoiZk1hODVCMnd5UUhFRXgxRlVQRFZIWFwvbnpEWGU4V3IwaGhQZzJHRnJiUlZuYXhEak5zN0dueUI0alpIWjJHYmc3d29LQjVua2NXeHY2V0JEMStoZDBnPT0iLCJtYWMiOiIwZTg2MmRiM2IxY2FlYTBkOTJmNzA1NTZmNDNkMjEyZDJkMWQ1NTI1MTM1Y2E0ZTM0YzY4NWI5NDlmYzZjOWM5In0%3D; last_renew_time=1606128653985'

# 根据开始日期、结束日期返回这段时间里所有工作日集合


def getDatesByTimes(sDateStr, eDateStr):
    # 填写天数
    max = 100

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


def fill_work(dateLists):
    """
        批量填报相同内容工时,使用时先在页面获取到cookie
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
    arr = [2, 3]
    spent_length = arr[random.randint(0, 1)]
    pCount = 'p_liyulong'
    for d in dateLists:
        body = {"qflow_task_id": _id, "order_id": orderId, "ltc_id": ltcCode, "project_name": name,
                "service_sub": "交付实施", "task_name": taskName, "in_team": "是", "spent_person": pCount,
                "data": [{"spent_date": d, "deliver_stage": stage, "spent_length": spent_length, "mark": "应用开发、前端框架构建、后台编程语言开发等技术支持技术经理，小程序开发-交付实施服务", "stage_desc": "客户如有除产品标准功能外的额外需求而必要进行的二次开发", "spent_desc": "与客户业务代表沟通，厘清本次二次开发需求，制定二次开发计划"}], "type": "1", "sub_type": ""}
        headers = {'cookie': cookie,
                   'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
                   'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response.json())


def del_error_time(ids):
    """
        根据id批量删除工时
    """
    base_url = 'https://redcs.tencent.com/deliver/timesheet/'
    cookie = '_ga=GA1.2.728526774.1599552504; pgv_pvi=4806563840; _gcl_au=1.1.1348498311.1599552521; _qddaz=QD.123299702982053; __root_domain_v=.tencent.com; pgv_pvid=9554451120; pgv_si=s4344743936; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100011561420%22%2C%22first_id%22%3A%2259929ffdd3744294bb6eacc05430cb3c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%221746cc242705a-0506bb2a4503c4-15336251-1296000-1746cc24271b38%22%7D; session_id_uv_pv=y3dh4lRh; session_id=eyJpdiI6IkhrUnJlREx5SnVsUnBvbHJLMmtvbFE9PSIsInZhbHVlIjoiZk1hODVCMnd5UUhFRXgxRlVQRFZIWFwvbnpEWGU4V3IwaGhQZzJHRnJiUlZuYXhEak5zN0dueUI0alpIWjJHYmc3d29LQjVua2NXeHY2V0JEMStoZDBnPT0iLCJtYWMiOiIwZTg2MmRiM2IxY2FlYTBkOTJmNzA1NTZmNDNkMjEyZDJkMWQ1NTI1MTM1Y2E0ZTM0YzY4NWI5NDlmYzZjOWM5In0%3D; last_renew_time=1606128653985'

    for id in ids:
        headers = {'cookie': cookie,
                   'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
                   'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        url = base_url + str(id)
        http = urllib3.PoolManager(num_pools=5, headers=headers)
        response = http.request('DELETE', url)

        print(response.status)


def get_month_ids(start_time, end_time):
    """
        查询时间段内工时id集合
    """
    orderId = 'TS20201112105288'
    spent_person = 'lujinquan'
    base_url = 'https://redcs.tencent.com/deliver/timesheet?spent_date_start='+start_time+'&spent_date_end=' + \
        end_time+'&type=1&order_id='+orderId+'&spent_person=' + \
        spent_person+'&ignore_mine=1&page=1&size=50'
    headers = {'cookie': cookie,
               'origin': 'https://redcs.tencent.com', 'content-type': 'application/json;charset=UTF-8',
               'authority': 'redcs.tencent.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    http = urllib3.PoolManager(num_pools=5, headers=headers)
    response = http.request('GET', base_url)
    json_body = json.loads(response._body)
    ids = []
    for i in json_body.get('data').get('list'):
        ids.append(i.get('id'))
    return ids


# ids = get_month_ids("2020-11-01", '2020-11-30')

# print(len(ids))
workDateList = getDatesByTimes("2020-11-03", "2020-11-24")
# print(workDateList)
# print(len(workDateList))
# fill_work(workDateList)
#ids = ['46897586', '46897585']
# del_error_time(ids)

# lists = []
# for i in range(22):
#     arr = [2, 3]
#     n = arr[random.randint(0, 1)]
#     lists.append(n)

print(len(workDateList))
# print(lists)
