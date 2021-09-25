# Booleans

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False


def comparison(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")


comparison(5, 3)  # a is greater than b

# Evaluate Values and Variables

print(bool("Hello"))    # True
print(bool(2))          # True

a = "Hello"
b = 2

print(bool(a))  # True
print(bool(b))  # True

# False Values

print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False

# Boolean from class


class example_class():
    def __len__(self):
        return 0


example_object = example_class()
print(bool(example_object))  # False

# Boolean from function


def example_function():
    return True


print(example_function())  # True
