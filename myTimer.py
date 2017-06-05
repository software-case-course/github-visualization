# -*- coding: cp936 -*-
import time
from datetime import datetime
from Save_language import Save_language
from Save_repositories import Save_repositories
from Save_starts import Save_starts
from Save_locations import Save_locations


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
    
    
if __name__ == "__main__":
    while True:
        current = datetime.now()
        if((current.hour == 0) and (current.minute == 0) and (current.second == 0)):
            getdata()
        time.sleep(1)
