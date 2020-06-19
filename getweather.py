# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:35:13 2020

@author: admin
"""

import requests  
import time
import random
import socket
import http.client
import pymysql
from bs4 import BeautifulSoup
import csv
#import cursor_mysql
import insert_mysql

def getContent(url , data = None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    } # request 的请求头
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout) #请求url地址，获得返回 response 信息
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e: # 以下都是异常处理
            print( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))
    print('request success,get weather data')
    return rep.text # 返回的 Html 全文

if __name__ == '__main__':
    url ='http://www.weather.com.cn/weather/101210101.shtml'
    html = getContent(url) # 调用获取网页信息
    print('my frist python file-get weather data')


def getdata(html_test):
    final = []
    bs = BeautifulSoup(html_test, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body #获取body
    data = body.find('div',{'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date) #添加日期
        inf = day.find_all('p')
        weather = inf[0].string #天气
        temp.append(weather)
        t_high = inf[1].find('span').string#最高温度,夜间可能没有这个元素，需要注意
        t_low = inf[1].find('i').string# 最低温度
        temp.append(t_low)
        temp.append(t_high)
        final.append(temp)
    print('getDate success')
    return final

def writeData(data,name):
	with open(name,'a',errors='ignore',newline='') as f:
			f_csv = csv.writer(f)
			f_csv.writerows(data)
	print('write_csv success')

if __name__ == '__main__':A
    url = 'http://www.weather.com.cn/weather/101210101.shtml'
    html = getContent(url)
    result = getdata(html)#解析网页信息，拿到需要的数据
    writeData(result, 'D:\py_work\weather.csv')#数据写入到 csv文档中
    insert_mysql.insertTable(result)#创建写入数据
    print('my frist python file-write to csv')


