# Example 62 - Dates and times

import datetime

date = datetime.date(2012, 6, 1)
current_date = datetime.date.today()
print(date)
print(current_date)

time = datetime.time(16, 0, 0)
current_time = datetime.datetime.now()
print(time)
print(current_time)

current_time = current_time.strftime("%H:%M:%S %d-%m-%Y")
print(current_time)

target_datetime = datetime.datetime(2020, 9,4, 10, 0, 0)
present_date = datetime.datetime.now()

if present_date > target_datetime:
    print("Time has passed")
else:
    print("Target time has not passed yet")
