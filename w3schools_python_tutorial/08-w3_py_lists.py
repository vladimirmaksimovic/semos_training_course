# Python Lists

listExample01 = ["Citroen", "Fiat", "Opel"]
print(listExample01)  # ["Citroen", "fiat", "Opel"]

listExample02 = [1, 2, 3, 4]
print(listExample02)  # [1, 2, 3, 4]

listExample03 = [True, False]
print(listExample03)  # [True, False]

listExample04 = [1, True, "Hyndai", False, "5"]
print(listExample04)  # [1, True, "Hyndai", False, "5"]

print(type(listExample04))  # <class 'list'>

print(listExample04[0])  # 1
print(listExample04[2])  # "Hyndai"
print(listExample04[3])  # False
print(listExample04[-1])  # 5
print(listExample04[1:4])  # [True, "Hyndai", False]
print(listExample04[:3])  # [1, True, "Hyndai"]
print(listExample04[2:])  # ["Hyndai", False, 5]
print(listExample04[-4:-1])  # [True, "Hyndai", False]

# Check if Item Exists

if "Hyndai" in listExample04:
    print(listExample04[1])  # True


# Change List Item Value

listExample04[2] = "BMW"
print(listExample04)  # [1, True, "BMW", False, "5"]

# Change a Range of Item Values

listExample04[0:2] = ["Skoda", "Lada"]
print(listExample04)  # ["Skoda", "Lada", "BMW", False, "5"]

listExample04.insert(3, "Renault")
print(listExample04)  # ['Skoda', 'Lada', 'BMW', 'Renault', False, '5']

# Append Items - add an item to the end of the list

listExample04.append("Mazda")
# ['Skoda', 'Lada', 'BMW', 'Renault', False, '5', 'Mazda']
print(listExample04)

# Extend List - add any iterable object - lists, tuples, sets, dictionaries...

listExample04.extend(listExample01)
# ['Skoda', 'Lada', 'BMW', 'Renault', False, '5', 'Mazda', 'Citroen', 'Fiat', 'Opel']
print(listExample04)

# Remove List Items

listExample04.remove(False)
# ['Skoda', 'Lada', 'BMW', 'Renault', '5', 'Mazda', 'Citroen', 'Fiat', 'Opel']
print(listExample04)

listExample04.pop(4)
# ['Skoda', 'Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat', 'Opel']
print(listExample04)

listExample04.pop()
# ['Skoda', 'Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']
print(listExample04)

del listExample04[0]
print(listExample04)  # ['Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']
# or delete the list completely

# clear list
listExample02.clear()
print(listExample02)  # []

# Loop Lists

# for ... in ...
for listItem in listExample04:
    print(listItem)  # ['Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']

# for ... in ...range(len(list))
for i in range(len(listExample04)):
    # ['Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']
    print(listExample04[i])

# while
i = 0
while i < len(listExample04):
    print(listExample04[i])
    i += 1
    # ['Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']

# List Comprehension

# Short syntax for creating a new list based on the values of an existing list.

# Example_01

[print(listItem) for listItem in listExample04]
# ['Lada', 'BMW', 'Renault', 'Mazda', 'Citroen', 'Fiat']

# Example_02

"""
frenchCarList = []

for car in listExample04:
    if "Renault" in listExample04:
        frenchCarList.append(car)

print("French cars: ", frenchCarList)
"""

frenchCarList = [car for car in listExample04 if "Renault" in car]

print("French cars: ", frenchCarList)
# French cars:  ['Renault']

# Example 03

frenchCarList = [car for car in range(3)]
print("New list in range to 3rd index: ", frenchCarList)
# New list in range to 3rd index:  [0, 1, 2]

# Example 04

frenchCarList = [car for car in range(10) if car < 4]
print(frenchCarList)
# [0, 1, 2, 3]

# Example 05

frenchCarList = [car.upper() for car in listExample04]
print(frenchCarList)
# ['LADA', 'BMW', 'RENAULT', 'MAZDA', 'CITROEN', 'FIAT']

# Example 06

frenchCarList = ["Hello World!" for car in listExample04]
print(frenchCarList)
# ['Hello World!', 'Hello World!', 'Hello World!', 'Hello World!', 'Hello World!', 'Hello World!']

# Example 07

frenchCarList = [car if car == "Renault" or
                 car == "Citroen" else
                 "Not a French Car" for
                 car in listExample04]
print(frenchCarList)
# ['Not a French Car', 'Not a French Car', 'Renault', 'Not a French Car', 'Citroen', 'Not a French Car']

# Sort Lists

# Alphanumerically - case sensitive

listExample04.sort()
print(listExample04)
# ['BMW', 'Citroen', 'Fiat', 'Lada', 'Mazda', 'Renault']

# Descending

listExample04.sort(reverse=True)
print(listExample04)
# ['Renault', 'Mazda', 'Lada', 'Fiat', 'Citroen', 'BMW']

#  Case Insensitive Sort

listExample05 = ["beetle", "Golf 2", "Ascona", "fiat 500", "Trabant"]

listExample05.sort()
print(listExample05)
#['Ascona', 'Golf 2', 'Trabant', 'beetle', 'fiat 500']

listExample05.sort(key=str.lower)
print(listExample05)
# ['Ascona', 'beetle', 'fiat 500', 'Golf 2', 'Trabant']

# Reverse Order

listExample05.reverse()
print(listExample05)
# ['Trabant', 'Golf 2', 'fiat 500', 'beetle', 'Ascona']

# List Copy

listExample06 = listExample05.copy()
print(listExample06)
# ['Trabant', 'Golf 2', 'fiat 500', 'beetle', 'Ascona']

listExample06 = list(listExample04)
print(listExample06)
# ['Renault', 'Mazda', 'Lada', 'Fiat', 'Citroen', 'BMW']

# Join Lists

listExample06 = listExample04 + listExample05
print(listExample06)
# ['Renault', 'Mazda', 'Lada', 'Fiat', 'Citroen', 'BMW', 'Trabant', 'Golf 2', 'fiat 500', 'beetle', 'Ascona']

for listItem in listExample03:
    listExample01.append(listItem)

print(listExample01)
# ['Citroen', 'Fiat', 'Opel', True, False]

listExample01.extend(listExample04)
print(listExample01)
# ['Citroen', 'Fiat', 'Opel', True, False, 'Renault', 'Mazda', 'Lada', 'Fiat', 'Citroen', 'BMW']
