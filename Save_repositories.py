# -*- coding: cp936 -*-
import requests
from datetime import date, time, datetime, timedelta
import database

class Save_repositories(object):
    #获取每年项目数量情况
    #参数：无
    #返回值：无
    def Get_repositories(self):
        repositorie=[]
        mydatabase=database.Database()
        now=datetime.now()
        now_time=now.strftime('%Y')
        y=int(now_time)
        i=0
        yearData=2007
        #获取2007到当前年份的字符串列表
        while yearData<=y:
            repositorie.append(str(yearData))
            yearData=yearData+1
            i=i+1
        #设定隔1分钟后再访问GitHub API
        total_number=0
        period=timedelta(days=0,hours=0,minutes=1,seconds=0)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        i=0
        l=len(repositorie)        
        while True and i<l:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=repositorie[i]
                response=requests.get('https://api.github.com/search/repositories?q=created:'+x).json()
                if response['incomplete_results']==False:
                    mydatabase.update_repositories_data(x,response['total_count'])
                    total_number=total_number+response['total_count']
                    i=i+1
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                continue
        mydatabase.update_total_data("total_count",total_number)
