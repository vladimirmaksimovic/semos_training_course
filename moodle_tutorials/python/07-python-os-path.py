# import modules

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print(os.name)

  # Check for items existence and type
  print("Item exists: " + str(path.exists("text-01.txt")))
  print("Item is a file: " + str(path.isfile("text-01.txt")))
  print("Item is a ditrectory: " + str(path.isdir("text-01.txt")))

  # Work with file paths
  print("Item path: " + str(path.realpath("text-01.txt")))
  print("Item path and name: " + str(path.split(path.realpath("text-01.txt"))))

  # Get the modification time
  t = time.ctime(path.getatime("text-01.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("text-01.txt")))

  # Calculate how long the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text-01.txt"))
  print("It has been " + str(td) + " since the file was modified")
  print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
  main()