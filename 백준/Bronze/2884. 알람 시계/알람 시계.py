from datetime import datetime, timedelta


h, m = map(int, input().split())

time1 = datetime(2023, 11, 23, h, m, 0)

time2 = time1 + timedelta(minutes=-45)
print(time2.hour, time2.minute)