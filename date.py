
import datetime
 

def getCurrentDate():
    
    now = datetime.datetime.now()


    time_now = (now.year, now.month, now.day)

    return str(now.month) + "/" + str(now.day)  + "/" + str(now.year)
 