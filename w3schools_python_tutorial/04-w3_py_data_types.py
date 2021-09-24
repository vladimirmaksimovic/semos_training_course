# Python Data Types

'''
Text Type:      str
Numeric Type:   int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:      set, forzenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
'''

# String
string_var = "Hello World!"
# string_var = str("Hello World!")

# Intiger
intiger_var = 2
# intiger_var = int(2)

# Float
float_var = 3.3
# float_var = float(3.3)

# Complex - written with a "j" as the imaginary part
complex_var = 1j
# complex_var = complex(1j)

# List
list_var = ["One", 2, True]
# list_var = list(("One", 2, True))

# Tuple
tuple_var = ("Three", 4, False)
# tuple_var = tuple(("Three", 4, False))

# Range
range_var = range(3)

# Mapping
dict_var = {"car brand": "Citroen", "car name": "Saxo", "car age": 2001}
# dict_var = dict(car_brand = "Citroen", car_name = "Saxo", car_age = 2001)

# Set
set_var = {"Citroen", "Saxo", 2001}
# set_var = set(("Citroen", "Saxo", 2001))

# Frozenset
frozenset_var = ({"Citroen", "Saxo", 2001})
# frozenset_var = frozenset(("Citroen", "Saxo", 2001))

# Boolean
bool_var = True  # /False
# bool_var = bool(2)

# Bytes
bytes_var = b"Hello"
bytes_var = bytes(5)

# Bytearray
bytearray_var = bytearray(5)

# Memoryview
memoryview_var = memoryview(bytes(5))

# Casting

# int()
x = int(1)    # x = 1
y = int(2.8)  # y = 2
z = int("3")  # z = 3

# float()
x = float(1)    # x = 1.0
y = float(2.8)  # y = 2.8
z = float("3")  # z = 3.0

# str()
x = str(1)    # x = "1"
y = str(2.8)  # y = "2.8"
z = str(3.0)  # z = "3.0"
