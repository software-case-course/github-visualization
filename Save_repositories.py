import requests
from datetime import date, time, datetime, timedelta
import database

class Save_repositories(object):
    #获取每年项目数量情况
    #参数：无
    #返回值：无
    def Get_repositories(self):
        repositorie=['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
        mydatabase=database.Database()
        now=datetime.now()
        #设定隔30秒后再访问GitHub API
        period=timedelta(days=0,hours=0,minutes=0,seconds=30)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        i=0
        while True and i<11:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=repositorie[i]
                response=requests.get('https://api.github.com/search/repositories?q=created:'+x).json()
                mydatabase.update_repositories_data(x,response['total_count'])
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                i=i+1
                continue