import requests
from datetime import date, time, datetime, timedelta
import database

class Save_locations(object):

    #获取项目语言情况
    #参数：无
    #返回值：无
    def Get_locations(self):
        location=['America','US','USA','the United States','China','France','Germany','India','Russia','England','Britain','the United Kingdom','UK','Australia'
                  ,'Canada','Denmark','Mexico','Brazil','Argentina','Japan','South Africa','Egypt','Sudan','Poland','Romania','Ireland','Sweden','Iraq','Kazakhstan'
                  , 'Turkey','Italy','Niger']
        mydatabase=database.Database()
        now=datetime.now()
        #设定隔30秒后再访问GitHub API
        period=timedelta(days=0,hours=0,minutes=0,seconds=30)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        i=0
        j = 0
        count = 0
        while True and i<32:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=location[i]
                #由于美国跟英国的别称有很多个，每个用户写下国籍时会有很多种写法，因此需要查询每个别称对应的用户有多少，并把其加起来
                if x == 'America' or x == 'England':
                    j = 4
                response = requests.get('https://api.github.com/search/users?q=location:' + x).json()
                if j != 0:
                    j = j - 1
                    count = count + response['total_count']
                else:
                    count = response['total_count']
                if j == 0:
                    mydatabase.update_locations_data(x, count)
                    count = 0
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                i=i+1
                continue