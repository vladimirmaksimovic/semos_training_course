# Python uses indentation to indicate a block of code.

# Indentation example

# define function
def fn01(a, b):
    if (a > b):
        print(str(a) + " is greater than " + str(b))
    elif (a == b):
        print(str(a) + " is equal to " + str(b))
    else:
        print(str(a) + " is lesser than " + str(b))


# call function
fn01(5, 2)  # a > b
fn01(2, 3)  # a < b
fn01(5, 5)  # a = b
