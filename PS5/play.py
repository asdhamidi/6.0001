import time
from datetime import datetime

timebefore = "3 Oct 2016 17:00:10 "
timeafter = "3 Oct 2016 17:00:20 "
time1 = datetime.strptime(timebefore, "%d %b %Y %H:%M:%S")
time2 = datetime.strptime(timeafter, "%d %b %Y %H:%M:%S")
print(time1 > time2)