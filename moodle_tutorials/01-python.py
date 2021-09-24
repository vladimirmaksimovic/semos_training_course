# Chapters Exercises

# 01_03

print("Hello World!")


# 02_01

name_01 = input("Hi, what's your name? ")
age_01 = int(input("How old are you? "))

if age_01 < 13:
    print("You're too young to register", name_01)
else:
    print("Feel free to join", name_01)


# 02_07

"""
print("Hello World!")
print("Goodbye World!")
"""

# 02_09

"""
print("Hello world") #syntax error

10 * (2 / 0) # runtime error

name_02 = "Alice"
print("Hello name") # sematic error
"""

# 03_01

age = 30
print(age)  # 30
print(type(age))  # int

email_address = "name@email.com"
print(email_address)  # name@email.com
print(type(email_address))  # str

# 03_02

cookies = "Sugar"
print(cookies)  # Sugar
print(type(cookies))  # str

cookies = 1
print(cookies)  # 1
print(type(cookies))  # int

Cookies = 3
print(Cookies)  # 3
print(cookies)  # 1

first_name = "Jeff"
print(first_name)  # Jeff

first_Name = "Sara"
print(first_name)  # Jeff

# 03_05

print("Hi!")
name = input("What's your name? ")

print("It's nice to meet you,", name)
answer = input("Are you enjoying the course? ")

if answer == "Yes":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")

# 03_06

print("Hi!")

name = input("What's your name? ")
print("It's nice to meet you,", name)

answer = input("Are you enjoying the course? ")

if answer == "Yes":
    print("That's good to hear!")
elif answer == "No":
    print("Oh no! That makes me sad!")
else:
    print("Wrong answer!")

# 03_07

"""
Challenge 1:
This is going to be tricky ;)
2**3 = 8
Challenge complete!
"""

print("Challenge 1:")

# A message for the user
message = "This is going to be tricky ;)"
# Message = "Very tricky!"

# show the message on the screen
print(message)

# Perform mathematical operations
result = 2**3  # 8
print("2**3 = ", result)

# result = 5 - 3
#print("5 - 3 =", result)

print("Challenge complete!")

# 04_03

plant = "Irises"

if plant == "Cacti":
    print(plant, "don't need a lot of water")
else:
    print(plant, "love water")

print("Thanks!")

# 04_06

user_question = input("What is your favorite food?")

if user_question == "Kacamak":
    print("Yep! So amazing!")
else:
    print("Yuck! That's not it!")

print("Thank's for playing!")

# 05_01

"""
print("~~~ The Shimmy ~~~")

print("Take one step to the right and stomp.")
print("Take one step to the left and stomp.")
print("Shake those hips!")
"""

print("~~~ The Shimmy ~~~")


def shimmy():
    print("Take one step to the right and stomp.")
    print("Take one step to the left and stomp.")
    print("Shake those hips!")


shimmy()
shimmy()
shimmy()

# 05_02


def say_hello():
    print("Hello, friends!")


say_hello()
say_hello()
say_hello()

# 05_03

"""
def wash_car():
    print("Wash with tri-color foam")
    print("Rinse twice")
    print("Dry with large blow dryer")

    print("Wash with white foam")
    print("Rinse once")
    print("Air dry")
"""

"""
def wash_car(amount_paid):
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(6)
"""


def wash_car(amount_paid):
    msg_01, msg_02, msg_error = (
        "You have selected car wash option 01!",
        "You have selected car wash option 02!",
        "We don't have car wash option for that amount!")

    if(amount_paid == 6):
        print(msg_01)
    elif(amount_paid == 12):
        print(msg_02)
    else:
        print(msg_error)


amount_paid = int(input("Please input car wash amount: "))

wash_car(amount_paid)

# 05_04

"""
def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        print("The balance is", current_balance)

withdraw_money(100, 80)
"""

"""
def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here!")
"""


def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance
        # print("Current balance is: ", current_balance)


current_balance = float(input("Please input your balance: "))
amount = float(input("Please input your amount: "))

balance = withdraw_money(current_balance, amount)
print("Your balance is: ", balance)

if (balance <= 50):
    print("Warning, you have to make a deposit!")
else:
    print("Nothing to see here!")


# 05_07

# Prints out the name of a favorite city

"""
def favorite_city(name):
    print("One of my favorite cities is", name)

favorite_city("Santa Barbara, California")
favorite_city("Asheville, North Carolina")
favorite_city("Amsterdam, The Netherlands")
"""


def favorite_city(name):
    print("One of my favorite cities is: ", name)


name = input("Please enter the name of your favorite city: ")

favorite_city(name)

# Indentation Example

a = 5
b = 3

if a > b:
    print(str(a) + " > " + str(b) + ", an a is greater then b.")
else:
    print("a is lesser than b.")

# Variables and Data Types Examples

name = "John Doe"
print(type(name))  # str

age = 30
print(type(age))  # int

average_height = 170.5
print(type(average_height))  # float

# Operaters

# Adding
add = 3 + 2
print(add)  # 5

# Substracting
sub = 3 - 2
print(sub)  # 1

# Multiplying
mul = 3 * 2
print(mul)  # 6

# Dividing
div = 3 / 2
print(div)  # 1.5

# Exponents
exp = 3 ** 2
print(exp)  # 9

# Floor Devision
flo = 3 // 2
print(flo)  # 1

# Modular
mod = 5 % 3
print(mod)  # 2
