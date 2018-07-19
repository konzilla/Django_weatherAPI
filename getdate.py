

import datetime
from datetime import date


x = datetime.datetime.now()


month = x.strftime('%-m')
day = x.strftime('%-d')
year = x.strftime('%Y')

future_date = date(2019, 6, 4)
today_date = date(int(year), int(month), int(day))
number_of_days = (future_date - today_date).days
weeks = int((number_of_days % 365) / 7)
total_days_completed = (365 - (number_of_days))
percent = ('{:.1%}'.format(total_days_completed / 365)) 

print(number_of_days)
print(weeks)

print('You are at ' + percent)

