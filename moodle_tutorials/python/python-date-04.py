from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main ():
  now = datetime.now()
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

  """ Timedelta """

  print(timedelta(days=365, hours=5, minutes=1))
  # 365 days, 5:01:00

  print("One year from now it will be: " + str(now + timedelta(days=365)))
  # One year from now it will be: 2022-11-15 21:07:35.254194

  print("In 2 days and 3 weeks, it will be " + 
      str(now + timedelta(days=2, weeks=3)))
      # In 2 days and 3 weeks, it will be 2021-12-08 21:08:45.143584

  t = datetime.now() - timedelta(weeks=1)
  s = t.strftime("%A %B %d, %Y")
  print ("One week ago it was: " + s)
  # One week ago it was: Monday November 08, 2021

  ### How many days until April Fools' Day?

  today = date.today()  # get today's date
  afd = date(today.year, 4, 1)  # get April Fool's for the same year
  # use date comparison to see if April Fool's has already gone for this year
  # if it has, use the replace() function to get the date for next year
  if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

  # Now calculate the amount of time until April Fool's Day  
  time_to_afd = afd - today
  print ("It's just", time_to_afd.days, "days until next April Fools' Day!")

if __name__ == "__main__":
  main()