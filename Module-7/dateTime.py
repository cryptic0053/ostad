import datetime

current_datetime=datetime.datetime.now()

formatted_datetime=current_datetime.strftime("%d/%m/%y %H:%M:%S")
print(formatted_datetime)
#YYYY-MM-DD,YYYY-DD-MM,DD-MM-YY

print(current_datetime)
print(current_datetime.year)
print(current_datetime.weekday())
print(current_datetime.month)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)


date1=datetime.datetime(2024,9,1)
date2=datetime.datetime(2023,9,4)

diff=date1-date2
print(diff)

new_date=date1+datetime.timedelta(days=15)
print(new_date)

new_date=date1-datetime.timedelta(days=15)
print(new_date)