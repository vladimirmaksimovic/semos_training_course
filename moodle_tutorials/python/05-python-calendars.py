import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2017, 1, 0, 0)
print (st)
"""
January 2017
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""

hc =  calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print (st)
"""
<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">January 2017</th></tr>
<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
<tr><td class="sun">1</td><td class="mon">2</td><td class="tue">3</td><td class="wed">4</td><td class="thu">5</td><td class="fri">6</td><td class="sat">7</td></tr>
<tr><td class="sun">8</td><td class="mon">9</td><td class="tue">10</td><td class="wed">11</td><td class="thu">12</td><td class="fri">13</td><td class="sat">14</td></tr>
<tr><td class="sun">15</td><td class="mon">16</td><td class="tue">17</td><td class="wed">18</td><td class="thu">19</td><td class="fri">20</td><td class="sat">21</td></tr>
<tr><td class="sun">22</td><td class="mon">23</td><td class="tue">24</td><td class="wed">25</td><td class="thu">26</td><td class="fri">27</td><td class="sat">28</td></tr>
<tr><td class="sun">29</td><td class="mon">30</td><td class="tue">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
</table>
"""

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
  print (i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print (name)

for day in calendar.day_name:
  print (day)


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print ("Team meetings will be on:")
for m in range(1,13):
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2017, m)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]
  
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]
      
  print ("%10s %2d" % (calendar.month_name[m], meetday))