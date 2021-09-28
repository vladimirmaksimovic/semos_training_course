# dictionaries

dictionary_example_01 = {
    "brand": "Fiat",
    "model": "Bravo",
    "year": 2012,
    "floating_flywheel": True,
    "colors": ["red", "white", "black"]
}

"""
- written with curly brackets {},
- store data in key:value pairs,
- ordered, changeable and does not allow duplicates,
- data types: string, int, boolean and list
"""

print(dictionary_example_01)
# {'brand': 'Fiat', 'model': 'Bravo', 'year': 2012, 'floating_flywheel': True, 'colors': ['red', 'white', 'black']}

print(type(dictionary_example_01))
# <class 'dict'>

print(dictionary_example_01["brand"])
# Fiat

print(len(dictionary_example_01))
# 5

# Access Dictionary Items

print(dictionary_example_01["model"])
# Bravo

# get() method

print(dictionary_example_01.get("year"))
# 2012

# get keys()

print(dictionary_example_01.keys())
# dict_keys(['brand', 'model', 'year', 'floating_flywheel', 'colors'])

# add new item to dictionary

dictionary_example_01["colors"] = "grey"
print(dictionary_example_01)
# {'brand': 'Fiat', 'model': 'Bravo', 'year': 2012, 'floating_flywheel': True, 'colors': 'grey'}

# get values()

print(dictionary_example_01.values())
# dict_values(['Fiat', 'Bravo', 2012, True, 'grey'])

dictionary_example_01["colors"] = [
    "grey", "red", "white", "black", "metallic"]
print(dictionary_example_01)
# {'brand': 'Fiat', 'model': 'Bravo', 'year': 2012, 'floating_flywheel': True, 'colors': ['grey', 'red', 'white', 'black', 'metallic']}

# Get Items  return each item in a dictionary, as tuples in a list

print(dictionary_example_01.items())
# dict_items([('brand', 'Fiat'), ('model', 'Bravo'), ('year', 2012), ('floating_flywheel', True), ('colors', ['grey', 'red', 'white', 'black', 'metallic'])])

# Check if Key Exists

if "black" in dictionary_example_01["colors"]:
    print("Yes, there is a model with black color.")
else:
    print("Sorry, black color is not preset.")

# update() Dictionary

dictionary_example_01.update({"year": 2020})
print(dictionary_example_01["year"])
# 2020

# Remove Dictionary Items - pop(), popitem(), clear(), del

# Loop through a Dictionary

for key in dictionary_example_01:
    print("Key: ", key)


for value in dictionary_example_01:
    print("Value: ", dictionary_example_01[value])

# or

for dictionary_key in dictionary_example_01.keys():
    print("Key: ", dictionary_key)

for dictionary_value in dictionary_example_01.values():
    print("Value: ", dictionary_value)

# or both

for dictionary_item in dictionary_example_01.items():
    print("Item: ", dictionary_item)

"""
Item:  ('brand', 'Fiat')
Item:  ('model', 'Bravo')
Item:  ('year', 2020)
Item:  ('floating_flywheel', True)
Item:  ('colors', ['grey', 'red', 'white', 'black', 'metallic'])
"""

# copy() a Dictionary

dictionary_example_02 = dictionary_example_01.copy()
print(dictionary_example_02)
# {'brand': 'Fiat', 'model': 'Bravo', 'year': 2020, 'floating_flywheel': True, 'colors': ['grey', 'red', 'white', 'black', 'metallic']}

# dict() - copy a dictionary

dictionary_example_03 = dict(dictionary_example_01)
print(dictionary_example_03)
# {'brand': 'Fiat', 'model': 'Bravo', 'year': 2020, 'floating_flywheel': True, 'colors': ['grey', 'red', 'white', 'black', 'metallic']}

# Nested Dictionaries

dictionary_example_04 = {
    "dictionary_example_01": dictionary_example_01,
    "dictionary_example_02": dictionary_example_02,
    "dictionary_example_03": dictionary_example_03
}

print(dictionary_example_04)
"""
{'dictionary_example_01': {'brand': 'Fiat', 'model': 'Bravo', 'year': 2020, 'floating_flywheel': True, 'colors': ['grey', 'red', 'white', 'black', 'metallic']}, 'dictionary_example_02': {'brand': 'Fiat', 'model': 'Bravo', 'year': 2020, 'floating_flywheel': True, 'colors': ['grey', 
'red', 'white', 'black', 'metallic']}, 'dictionary_example_03': {'brand': 'Fiat', 'model': 'Bravo', 'year': 2020, 'floating_flywheel': True, 
'colors': ['grey', 'red', 'white', 'black', 'metallic']}}
"""
