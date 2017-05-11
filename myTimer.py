import time
from datetime import datetime
import Save_language

def getdata():
    language = Save_language()
    language.Get_language()
    
if __name__ == "__main__":
    while True:
        current = datetime.now()
        if((current.hour == 0) and (current.minute == 0) and (current.second == 0)):
            getdata()
        time.sleep(1)
