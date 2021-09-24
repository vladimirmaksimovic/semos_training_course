# Python Variables

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

a = "Hello!"
b = 3
c = 10.4
d = True
f = ["One", 2, 3.2, False]

# Variable Types

print(type(a))  # string
print(type(b))  # intiger
print(type(c))  # float
print(type(d))  # boolean
print(type(f))  # list

# to specify the data type of a variable use casting

g = str(3)  # g will be string = "3"
h = int(3)  # h will be integer = 3
i = float(3)  # i will be float = 3.0

# Case-Sensitive

j = 2
J = 2.23
# "J" variable will not overwrite "j" variable
print(j)  # 2
print(J)  # 2.23

# Variable Name

# Must start with a letter or underscore character.
# Can only contain alpha-numeric character and underscores (A-z, 0-9, and _).
# Variable names are case-sensitive.

myvar = "var 01"
my_var = "var 02"
_my_var = "var 03"
myVar = "var 04"
MYVAR = "var 05"
myvar2 = "var 06"

# A variable cannot start with a number.

# Multi Words Variable Names

variableName = "Hello World!"  # Camel Case
VariableName = "Hello World!"  # Pascal Case
variable_name = "Hello World!"  # Snake Case

# Assign Multiple Values

k, l, m = "Fiat", "Citroen", "Hyundai"
# k = "Fiat", l = "Citroen", m = "Hyundai"

# Assign One Value to Multiple Variables

n = o = p = "Ford"
# n = "Ford", o = "Ford", p = "Ford"

# Unpacking

german_cars = ["BMW", "WV", "Opel"]
q, r, s = german_cars
# q = "BMW", r = "WV", s = "Opel"

# Global and Local Variables

# Global Variable

w = "World!"


def helloWorldFn01():
    t = "Hello "
    print(t + w)


helloWorldFn01()  # "Hello World!"

# The "global" Keyword


def helloWorldFn02():
    global x
    x = "World!"


helloWorldFn02()

print("Hello " + x)  # "Hello World!"

# or to change the value of a global variable inside a function

z = "Python"


def helloWorldFn03():
    global z
    z = "World!"


helloWorldFn03()

print("Hello " + z)  # "Hello World!"
