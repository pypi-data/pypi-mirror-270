import datetime

date = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
print(type(date))
print(datetime.datetime.strftime(date, '%Y-%m-%d'))