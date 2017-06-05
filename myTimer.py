# -*- coding: cp936 -*-
import time
from datetime import datetime
import Save_language
import Save_repositories
import Save_starts
import Save_locations
import Save_users

def getdata():
    #��ȡ��Ŀ�������
    language = Save_language.Save_language()
    language.Get_language()
    #��ȡÿ����Ŀ�������
    repositories = Save_repositories.Save_repositories()
    repositories.Get_repositories()
    #��ȡ�����û��������
    locations = Save_locations.Save_locations()
    locations.Get_locations()
    #��ȡǰʮ��Ŀ��ϸ���
    starts = Save_starts.Save_starts()
    starts.Get_starts()
    #��ȡǰʮ�û���ϸ��Ϣ
    users = Save_users.Save_users()
    users.Get_users()
    
    
    
if __name__ == "__main__":
    while True:
        current = datetime.now()
        if((current.hour == 0) and (current.minute == 0) and (current.second == 0)):
            getdata()
        time.sleep(1)
