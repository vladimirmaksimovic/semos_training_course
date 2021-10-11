# Functions

# define f-n
def fun_01():
    print("Hello World!")


# call f-n
fun_01()  # Hello World!

# Arguments - args / Parameters - params


def fun_02(first_name, last_name, phone):
    print("First name: ", first_name)
    print("Last name: ", last_name)
    print("Phone number: ", phone)


fun_02("Ania", "Kubow", 333555)
fun_02("Brad", "Traversy", 555333)
fun_02("Dave", "Gray", 222333)

# Arbitrary Arguments - *args

"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""


def fun_03(*car):
    print("You won:" + car[3])


fun_03("Fiat", "BMW", "Opel", "Skoda", "Lada")


def fun_04(car_01, car_02, car_03):
    print("You won:" + car_03)


fun_04(car_01="Fiat", car_02="BMW", car_03="Opel")

# Arbitrary Keyword Arguments - **kwargs

"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""


def fun_05(**car):
    print("You won:" + car["Fiat"])


fun_05(Fiat="Bravo", BMW="x5", Opel="Corsa")

# Default Parameter Value


def fun_06(mando=" the way."):
    print("This is " + mando)


fun_06("a tomato.")
fun_06("a joke.")
fun_06("paradise.")
fun_06()  # This is the way.

# Passing a List as an Argument

"""
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
"""

list_01 = ["Mercedes", "Reanult", "Dacia"]


def fun_07(list_01):
    print(list_01)


fun_07(list_01)


def fun_08(list_01):
    for car in list_01:
        print(car)


fun_08(list_01)

# Return Values


def fun_09(a):
    return 3 * a


print(fun_09(2))
print(fun_09(-3))
print(fun_09(0.8))

# The pass Statement

"""
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""


def fun_10():
    pass  # no error

# Recursion


"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
