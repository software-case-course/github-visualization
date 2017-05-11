# -*- coding: cp936 -*-
import requests
from datetime import date, time, datetime, timedelta
import database

class Get_total(object):

    #获取项目语言情况
    #参数：无
    #返回值：无
    def Get(self):        
        year=[]
        mydatabase=database.Database()
        now=datetime.now()
        now_time=now.strftime('%Y')
        y=int(now_time)
        i=0
        yearData=2007
        #获取2007到当前年份的字符串列表
        while yearData<=y:
            year.append(str(yearData))
            yearData=yearData+1
            i=i+1
        total_number=0
        #设定隔30秒后再访问GitHub API
        period=timedelta(days=0,hours=0,minutes=0,seconds=1)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        i=0
        l=len(year)
        while True and i<l:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=year[i]
                response=requests.get('https://api.github.com/search/repositories?q=created:'+x).json()
                total_number=total_number+response['total_count']
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                i=i+1
                continue
        mydatabase.update_total_data("total_count",total_number)
