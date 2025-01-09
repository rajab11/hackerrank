import calendar

month,day,year=(int(i) for i in input().split(' '))
dayNumber=calendar.weekday(year,month,day)

days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[dayNumber])
