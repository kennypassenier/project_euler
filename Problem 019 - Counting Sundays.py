import calendar
import datetime

data = calendar

answer = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if data.weekday(year, month, 1) == 6:
            answer += 1
print(answer)