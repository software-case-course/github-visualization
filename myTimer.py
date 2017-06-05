# -*- coding: cp936 -*-
import time
from datetime import datetime
import Save_language
import Save_repositories
import Save_starts
import Save_locations
import Save_users

def getdata():
    #获取项目语言情况
    language = Save_language.Save_language()
    language.Get_language()
    #获取每年项目数量情况
    repositories = Save_repositories.Save_repositories()
    repositories.Get_repositories()
    #获取地区用户数量情况
    locations = Save_locations.Save_locations()
    locations.Get_locations()
    #获取前十项目详细情况
    starts = Save_starts.Save_starts()
    starts.Get_starts()
    #获取前十用户详细信息
    users = Save_users.Save_users()
    users.Get_users()
    
    
    
if __name__ == "__main__":
    while True:
        current = datetime.now()
        if((current.hour == 0) and (current.minute == 0) and (current.second == 0)):
            getdata()
        time.sleep(1)
