# -*- coding: cp936 -*-
import requests
from datetime import date, time, datetime, timedelta
import database

class Save_users(object):

    #获取关注度前10用户信息
    #参数：无
    #返回值：无
    def Get_users(self):
        mydatabase=database.Database()
        users=[]
        user_url=[]
        follower=[]
        location=[]
        repository=[]
        repository_url=[]
        now=datetime.now()
        #设定30s后访问GitHub API
        response=requests.get('https://api.github.com/search/users?q=+followers:%3E10000&sort=followers').json()
        period=timedelta(days=0,hours=0,minutes=0,seconds=30)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        for i in range(0,10):
            users.append(response['items'][i]['login'])
            user_url.append('https://github.com/'+response['items'][i]['login'])
        j=0
        while True and j<10:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                user_response=requests.get('https://api.github.com/users/'+users[j]).json()
                follower.append(user_response['followers'])
                location.append(user_response['location'])
                repo_response=requests.get('https://api.github.com/search/repositories?q=user:'+users[j]+'&sort=stars').json()
                repository.append(repo_response['items'][0]['name'])
                repository_url.append('https://github.com/'+users[j]+'/'+repo_response['items'][0]['name'])
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                j=j+1
                continue
        #更新数据库
        for i in range(0,10):
            mydatabase.update_users_data(i+1,users[i],user_url[i],follower[i],location[i],repository[i],repository_url[i])
