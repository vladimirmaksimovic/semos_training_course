# Loops

"""
Python has two primitive loop commands:
    - while loops
    - for loops
"""

# The while Loop

i = 1

while i < 6:
    print("Hello World! Please count me in...", i)
    i += 1  # increment i or loop will continue forever

# The break Statement

a = 1

while a < 5:
    print("Please don't break ...", a)
    if a == 3:
        break  # break loop on 3
    a += 1

# The continue Statement

b = 0

while b < 4:
    b += 1
    if b == 3:
        continue  # skip on 3 and continue
    print("Please continue...", b)

# The else Statement

c = 2

while c < 7:
    print("Go go ... ", c)
    c += 1
else:
    print("That all folks!")

# The For Loops

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

string_var = "Hello World!"
list_var = ["One", 2, True]
tuple_var = (3, False, "Four")
dictionary_var = {"first": 1, "Second": True, "third": "3"}
set_var = {"5", 6, "seven"}

print(type(string_var))
print(type(list_var))
print(type(tuple_var))
print(type(dictionary_var))
print(type(set_var))

for item in string_var:
    print(item)

for item in list_var:
    print(item)

for item in tuple_var:
    print(item)

for item in dictionary_var:
    print(item)

for item in set_var:
    print(item)

# The break Statement

for item in list_var:
    print(item)
    if item == True:
        break

for item in list_var:
    if item == "One":
        break
    print(item)

# The continue Statement

for item in list_var:
    if item == 2:
        continue
    print(item)

# the range() Function

for m in range(3):
    print(m)

for n in range(5, 7):
    print(n)

for l in range(9, 20, 3):
    print(l)

# Else in For Loop

for k in range(4):
    print(k)
else:
    print("When the music is over ...")

"""
The else block will NOT be executed if the loop is stopped by a break statement.
"""

for o in range(5):
    if o == 3:
        break
    print(o)
else:
    print("This is the end ...")

# Nested Loops

car = ["Fiat", "Opel", "Skoda"]
car_type = ["Racing", "Family", "Cargo"]

for c in car:
    for t in car_type:
        print(c, " => ", t)

# The pass Statement

"""
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
"""

for y in [0, 1, 2]:
    pass
# no error msg
