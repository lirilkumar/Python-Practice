from datetime import datetime,date
import time


print(datetime.utcnow().isoformat())
print(datetime.utcnow().replace(hour=0,minute=0,second=0,microsecond=0).isoformat()+'Z')
print(int(time.mktime(datetime.now().timetuple()) * 1000))
print(datetime.utcnow().date())

print(datetime.strptime('12/15/2014 13:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0).isoformat()+'Z')
