from datetime import date
from datetime import time
from datetime import datetime

def main ():
  # get and print toda's date
  today = date.today()
  print("Today's date is: ", today) # Today's date is:  2021-11-15

  # print out date's individual components
  print("Date's components: ", today.day, today.month, today.year)
  # Date's components:  15 11 2021 
  print("Day: ", today.day, ", Moth: ", today.month, ", Year: ", today.year)
  # Day:  15 , Moth:  11 , Year:  2021

  todayTime = datetime.now()
  print(todayTime) # 2021-11-15 19:49:18.245637 

  time = datetime.time(datetime.now())
  print(time) # 19:49:18.246636

  """
  
  Date Formating
  
  %y/%Y - Year, %a/%A - weekday, %b/%B - Month, %d - Day of month,

  %c - locale's date and time, %x - locale's date, %X - locale's time,

  %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM

  """

  print(today.strftime("%a, %d, %B, %Y")) 
  # Mon, 15, November, 2021

  print(time.strftime("Locale date and time: %c"))
  # Locale date and time: Mon Jan  1 19:59:15 1900
  
  print(time.strftime("Locale date: %x"))
  # Locale date: 01/01/00
  
  print(time.strftime("Locale time: %X"))
  # Locale time: 20:00:48

  print(time.strftime("Current time: %I:%M:%S:%p"))
  # Current time: 08:03:53:PM

  print(time.strftime("24-hour time: %H:%M"))
  # 24-hour time: 20:03

if __name__ == "__main__":
  main()