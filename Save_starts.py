# -*- coding: cp936 -*-
import requests
from datetime import date, time, datetime, timedelta
import database

class Save_starts(object):
    def Get_result(self,data_A,data_B):
        if(len(data_A)==0):
            return data_B
        j=0
        i=0
        re=[]
        k=0
        lengthA=len(data_A)
        lengthB=len(data_B)
        while(i<lengthA and j<lengthB):
            num1=data_A[i]['stargazers_count']
            num2=data_B[j]['stargazers_count']
            if(num1>=num2):
                re.append(data_A[i])
                k=k+1
                if(k==10):
                    break;
                i=i+1
            else:
                re.append(data_B[j])
                k=k+1
                if(k==10):
                    break;
                j=j+1
        if(k<10):
            if(i==10):
                while(k<10 and j<lengthB):
                    re.append(data_B[j])
                    j=j+1
                    k=k+1
            elif(j==10):
                while(k<10 and i<lengthA):
                    re.append(data_A[i])
                    i=i+1
                    k=k+1
        return re
            
    #获取前十项目详细情况
    #参数：无
    #返回值：无
    def Get_starts(self):
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
        resultB=[]
        while True and i<l:
            iter_now=datetime.now()
            iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
            if str(iter_now_time)==str(strnext_time):
                x=repositorie[i]
                
                response=requests.get('https://api.github.com/search/repositories?q=created:'+x+'&sort=starts').json()
                
                if response['incomplete_results']==False:
                    total_count=response['total_count']
                    items=response['items']
                    j=0
                    resultA=[]
                    if(total_count<10):
                        while(j<total_count):
                            item=items[j]
                            data={}
                            data['stargazers_count']=item['stargazers_count']
                            data['repo_url']=item['html_url']
                            data['repo_name']=item['name']
                            owner=item['owner']
                            data['user_url']=owner['html_url']
                            data['user_login']=owner['login']
                            resultA.append(data)
                            j=j+1
                    else:
                        while(j<10):
                            item=items[j]
                            data={}
                            data['stargazers_count']=item['stargazers_count']
                            data['repo_url']=item['html_url']
                            data['repo_name']=item['name']
                            owner=item['owner']
                            data['user_url']=owner['html_url']
                            data['user_login']=owner['login']
                            resultA.append(data)
                            j=j+1
                    i=i+1
                    resultB.append(resultA)    
                iter_now=datetime.now()
                iter_time=iter_now+period
                strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
                continue
        length=len(resultB)
        j=0
        B=[]        
        while(j<length):
            B=self.Get_result(B,resultB[j])
            j=j+1
        L=len(B)
        j=0
        #数据库操作
        while(j<L):
            mydatabase.update_projects_data(j+1,B[j]['repo_name'],B[j]['repo_url'],B[j]['stargazers_count'],B[j]['user_login'],B[j]['user_url'])            
            j=j+1
