# Example file for Hello World

def main():
  print("Hello World!")
  # name = input("What is your name? ")
  # print("Nice to meet you, ", name)

if __name__ == "__main__":
  main()

""" Variables """

# Declare a variable adn initialize it

f = 0
print(f)

# Re - declare variable

f = "abc"
print(f)

# ERROR: variables of diffrent types cannot be combined

# print("string " + 123) # error

print("string " + str(123)) # OK

""" Functions """

# Global vs. local variables in functions

def someFunction():
  global f
  f = "def"
  print(f)

someFunction()
print(f)

# Define a basic function

def fn1():
  print("I am a function!")

fn1()
print(fn1())
print(fn1)

# function that takes arguments

def fn2(arg1, arg2):
  print(arg1, " =>  ", arg2)

# function that returns arguments

def fn3(x):
  return x * x * x

fn2 (1, "second")
print (fn2(1, "second"))
print (fn3(3))

# function with defined value of argument

def fn4(num, x = 2):
  result = 1
  for i in range(x):
    result = result * num
  return result

print(fn4(2))

""" Conditionals """

def fn5():
  x, y = 1000, 100

  # conditional flow uses if, elif, else
  if (x < y):
    st = "x is less than y"
  elif(x == y):
    st= "x is equal to y"
  else:
    st = "x is greater than y"

""" Loops """

def loopFn():
  x = 0

  # define while loop
  """ while (x < 5):
    print(x)
    x = x + 1 """

  # define a for loop
  """ for x in range(5, 10):
    print(x)

  days = ["Mon", "...", "Sunday"]
  for day in days:
    print (day) """

  # break and continue statements
  for x in range(5, 10):
    # if (x == 7): break  # 5, 6
    if (x % 2 == 0): continue  # 5, 7, 9
    print(x)

  days = ["Mon", "...", "Sunday"]
  for index, day in enumerate(days):
    print (index, day)

loopFn()

""" Classes """

class class1(): # define a class
  def method1(self): # define first class method with "self" argument
    print("myClass method1")

  def method2(self, somestring): # define second class method
    print("myClass method 2" + somestring)

def fn6():
  # instantiate an object instance inside a f-n
  c = class1()
  # call class methods
  c.method1()
  c.method2("This is a string")


# if __name__ == "__fn6__":
fn6()

class class2(class1):
  def method1(self):
    class1.method1(self)
    print("another Class method1")

  def method2(self, somestring):
    print("another Class method 2")