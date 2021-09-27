# Sets

"""
- unordered - items in a set don't have a defined
order and they appear in different order every
time of use,
- unchangeable - cannot change the items after the set
has been created,
- don't allow duplicates,
- unindexed,
- any data type,
"""

set_example_01 = {"Fender", "Gibson", "Ibanez"}
print(set_example_01)  # {"Fender", "Gibson", "Ibanez"}
print(type(set_example_01))  # <class 'set'>

# can't access items in set by refering to an index or a key

for item_set in set_example_01:
    print(item_set)
    # Fender, Ibanez, Gibson

print("Ibanez" in set_example_01)  # True

# Add new set items

set_example_01.add("Yamaha")
print(set_example_01)
# {'Fender', 'Gibson', 'Yamaha', 'Ibanez'}

# Add Sets

set_example_02 = {True, 1, False, 0}
list_example_01 = [1, 2, 3, 4]

set_example_01.update(set_example_02)
print(set_example_01)
# {False, True, 'Gibson', 'Fender', 'Ibanez', 'Yamaha'}

set_example_01.update(list_example_01)
print(set_example_01)
# {False, 'Yamaha', True, 2, 3, 4, 'Fender', 'Ibanez', 'Gibson'}

# Remove Set Item

set_example_01.remove(True)
print(set_example_01)
# {False, 2, 3, 4, 'Ibanez', 'Gibson', 'Fender', 'Yamaha'}

set_example_01.discard(False)
print(set_example_01)
# {2, 3, 4, 'Fender', 'Ibanez', 'Yamaha', 'Gibson'}

set_example_01.pop()
print(set_example_01)
# {3, 4, 'Gibson', 'Yamaha', 'Fender', 'Ibanez'}

set_example_01.clear()
print(set_example_01)
# set()

del set_example_02
# print(set_example_02)
# NameError: name 'set_example_02' is not defined

# ... Loop as the rest of array types ...

# Join Two Sets

# union - returns a new set with all items from both sets - exclude duplicates

set_example_03 = {"a", "b", "c"}
set_example_04 = {1, 2, 3}

set_example_05 = set_example_03.union(set_example_04)
print(set_example_05)
# {1, 2, 3, 'c', 'b', 'a'}

# update - inserts items - exclude duplicates

set_example_01.update(set_example_03)
print(set_example_01)
# {'a', 'c', 'b'}

# intersection_update - insert set items and keep ONLY duplicates

set_example_01.intersection_update(set_example_03)
print(set_example_01)
# {'b', 'c', 'a'}

# intersection - return items that are present in both sets

set_example_01.intersection(set_example_03)
print(set_example_01)
# {'b', 'c', 'a'}

# symmetric_difference_update() - keep all but NOT the duplicates

set_example_01.symmetric_difference_update(set_example_03)
print(set_example_01)
# set()

# symmetric_difference - return a new set tha contains only the elements that are NOT present in both sets
