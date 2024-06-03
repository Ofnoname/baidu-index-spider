"""
百度指数爬虫 2024年3月
"""
import json
import time

import requests
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import random
from requests.exceptions import RequestException


def generate_http_headers(credential):
    http_headers = {
        'Cookie': 'BDUSS=' + credential["cookie_BDUSS"],
        'Cipher-Text': credential["cipherText"],
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://index.baidu.com/v2/main/index.html',
        'Host': 'index.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    return http_headers


def calculate_yearly_averages(start_date, end_date, data_series):
    # Convert the start and end dates to datetime objects
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    days_span = (end - start).days + 1

    # Split the data series into a list and replace empty strings with '0'
    data_points = data_series.split(',')
    data_points = ['0' if point == '' else point for point in data_points]
    data_points = np.array(data_points, dtype=float)

    if days_span <= 366:
        dates = pd.date_range(start, periods=len(data_points))
    else:
        weeks_span = len(data_points)
        dates = pd.date_range(start, periods=weeks_span, freq='W')

    # Create a DataFrame with the dates and data points
    df = pd.DataFrame({'Date': dates, 'Data': data_points})
    df.set_index('Date', inplace=True)

    # Calculate the yearly average
    yearly_averages = df.resample('Y').mean().reset_index()
    yearly_averages['Year'] = yearly_averages['Date'].dt.year
    yearly_averages.drop('Date', axis=1, inplace=True)
    yearly_averages.rename(columns={'Data': 'Average'}, inplace=True)

    return yearly_averages


# 解密
def decrypt(ptbk, index_data):
    n = len(ptbk) // 2
    a = dict(zip(ptbk[:n], ptbk[n:]))
    return "".join([a[s] for s in index_data])


def keywords2json(keywords):
    import json
    # Convert each keyword in each sublist into a dictionary with 'name' and 'wordType'
    converted_keywords = [
        [{"name": keyword, "wordType": 1} for keyword in sublist]
        for sublist in keywords
    ]
    # Convert the list of lists of dictionaries into a JSON string
    json_string = json.dumps(converted_keywords, ensure_ascii=False)
    return json_string


def namely(keywords):
    return '+'.join(keywords)


def crawl_request(keywords, startDate, endDate, regionCode, credential, expectedInterval, autoSave):
    print('正在查询：', keywords, startDate, endDate, regionCode)
    words = keywords2json(keywords)

    # 第一级以逗号分隔，第二级以加号分隔
    testwordset = ','.join([namely(keyword) for keyword in keywords])
    max_retries = 3  # 最大重试次数
    retries = 0  # 当前重试次数

    while retries < max_retries:
        try:
            url = f'https://index.baidu.com/api/AddWordApi/checkWordsExists?word={testwordset}'
            rsp = requests.get(url, headers=generate_http_headers(credential), timeout=10).json()
            # 若data的result不为空，则说明关键词不存在，报错并退出
            if rsp['data']['result']:
                print(f'{testwordset}关键词不存在或组合里有不存在的关键词，请检查')
                return -1

            url = f'http://index.baidu.com/api/SearchApi/index?area=0&word={words}&area={regionCode}&startDate={startDate}&endDate={endDate}'
            rsp = requests.get(url, headers=generate_http_headers(credential), timeout=10).json()

            # 获取解密秘钥
            data = rsp['data']['userIndexes']
            uniqid = rsp['data']['uniqid']
            url = f'https://index.baidu.com/Interface/ptbk?uniqid={uniqid}'
            ptbk = requests.get(url, headers=generate_http_headers(credential), timeout=10).json()['data']

            # 数据解密
            res = [0 for _ in range(len(data))]
            for i in range(len(data)):
                index_data = decrypt(ptbk, data[i]['all']['data'])
                # save
                yearly_averages = calculate_yearly_averages(startDate, endDate, index_data)
                print(yearly_averages)

                if autoSave:
                    file_path = f'output/{namely(keywords[i])} {startDate[:4]}-{endDate[:4]} {regions[regionCode]}.csv'
                    yearly_averages.to_csv(file_path, index=False)
                    print(f'已保存文件到 {file_path}')

                res[i] = yearly_averages.to_dict(orient='records')
            return res
        except Exception as e:
            print(f'请求失败，错误信息：{e}')
            retries += 1
            print(f'重试第{retries}次...')
            time.sleep(random.randint(1, 3))  # 在重试前等待一段时间
    if retries == max_retries:
        print(f'请求失败次数过多，已达到最大重试次数{max_retries}，跳过当前连接')
        return -1


regions = {}


def crawl(keywords, startDate, endDate, regionCode, credential, expectedInterval, autoSave):
    global regions
    if not regions:
        with open('./webui/public/city.json', encoding='utf-8') as f:
            regions = json.load(f)

    res = {regionCode: []}
    for i in range(0, len(keywords), 5):
        selected_keywords = keywords[i:i + 5]
        print('已完成：', i, '剩余：', len(keywords) - i)

        if regionCode != '999':
            t = crawl_request(selected_keywords, startDate, endDate, regionCode, credential, expectedInterval, autoSave)
            if t == -1:
                # -1 说明此次查询失败，跳过这个地区，进行下一个地区的查询
                continue
            res[regionCode].extend(t)
            # 每次查询后休息一到五秒，实际上在账号很多的情况下，这个时间可以缩短
            time.sleep(expectedInterval / 1000 + random.randint(1, 3) / 2)
        else:
            # 999 意味着我们需要查询所有地区
            for t_regionCode in regions.keys():
                t = crawl_request(selected_keywords, startDate, endDate, t_regionCode, credential, expectedInterval,
                                  autoSave)
                if t == -1:
                    continue
                # 如果res中没有这个地区的数据，就新建一个
                if t_regionCode not in res:
                    res[t_regionCode] = [0 for _ in range(len(keywords))]
                res[t_regionCode].extend(t)
                time.sleep(expectedInterval / 1000 + random.randint(1, 3) / 2)
    return res
