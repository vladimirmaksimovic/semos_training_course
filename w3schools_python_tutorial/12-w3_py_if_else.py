# IF ... ELSE ...

"""
Python supports the usual logical conditions from mathematics:

a == b equals,
a != b not equals,
a < b less than,
a <= b less than or equal to,
a > b greater than,
a >= b greater than or equal to,
"""

a = 3
b = 5

# IF ...

if a < b:
    print("b is greater than a")

# IF ... ELSE ...

if a < b:
    print("b is greater than a")
else:
    print("a is greater than b")

# ELIF ...

if a < b:
    print("b is greater than a")
elif a == b:
    print("a and b equal")
else:
    print("a is greater than b")

# short IF ...

if a > b:
    print("a is greater than b")

# short IF ... ELSE ...

print("A") if a > b else print("B")

# Ternary Operators / Conditional Expressions

print("A") if a > b else print("=") if a == b else print("B")

# AND / OR - logical operators to combine conditional statements

if a > 0 and a > b:
    print("a is greater than b")

if a > 5 or a > b:
    print("a is greater than b")

# nested IF ... statements

if a == 2:
    print("To ...")
    if a == b:
        print("... be ...")
    elif a != b:
        print("... not to be...")
    else:
        print("... that is ...")
else:
    print("... the question?")

# PASS statement

"""
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
"""

if b > a:
    pass
