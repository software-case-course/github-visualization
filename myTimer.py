# -*- coding: cp936 -*-
import time
from datetime import datetime
import Save_language

def getdata():
    #获取项目语言情况
    language = Save_language()
    language.Get_language()
    #获取每年项目数量情况
    repositories = Save_repositories()
    repositories.Get_repositories
    
if __name__ == "__main__":
    while True:
        current = datetime.now()
        if((current.hour == 0) and (current.minute == 0) and (current.second == 0)):
            getdata()
        time.sleep(1)
