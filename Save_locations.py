# -*- coding: cp936 -*-
import requests
from datetime import date, time, datetime, timedelta
import database

class Save_locations(object):

    #��ȡ�����û��������
    #��������
    #����ֵ����
    def Get_locations(self):
        location=['America','US','USA','the United States','China','France','Germany','India','Russia','England','Britain','the United Kingdom','UK','Australia']
        mydatabase=database.Database()
        now=datetime.now()
        #�趨��30����ٷ���GitHub API
        period=timedelta(days=0,hours=0,minutes=0,seconds=30)
        next_time=now+period
        strnext_time=next_time.strftime('%Y-%m-%d %H:%M:%S')
        i=0
        j = 0
        count = 0
        while True and i<14:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=location[i]
                #����������Ӣ���ı���кܶ����ÿ���û�д�¹���ʱ���кܶ���д���������Ҫ��ѯÿ����ƶ�Ӧ���û��ж��٣������������
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
