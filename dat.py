"""
Write a Python program to subtract five days from current date.

Write a Python program to print yesterday, today, tomorrow.

Write a Python program to drop microseconds from datetime.

Write a Python program to calculate two date difference in seconds.
"""
from datetime import date, timedelta, datetime
#1
today = date.today()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)
#2
today = date.today()
print(f'yesterday: {today - timedelta(days = 1)}\ntoday: {today}\ntomorrow: {today + timedelta(days = 1)}')
#3
dt = datetime.now()
dt = dt.replace(microsecond=0)
print(dt, '.000000', sep = '')
#4
def difference_in_seconds(date1, date2):
  # Convert dates to timestamps in seconds
  timestamp1 = date1.timestamp()
  timestamp2 = date2.timestamp()

  #
  difference = abs(timestamp1 - timestamp2)

  return difference

# Example for exercise 4
date1 = datetime(2024, 2, 22, 10, 0, 0)
date2 = datetime(2024, 2, 23, 12, 30, 0)

difference = difference_in_seconds(date1, date2)

print(f"The difference between {date1} and {date2} is {difference} seconds.")