# Tuples

# ordered,
# unchangeable, immutable
# allow duplicates,
# any data type
# can contain different data types


tuple_example_01 = ("Stratocaster", "Squier", "Gibson", "Ibanez")

print(tuple_example_01)
# ('Stratocaster', 'Squier', 'Gibson', 'Ibanez')

print(type(tuple_example_01))
# <class 'tuple'>

# Tuple with one item

one_item_tuple = ("one item",)
print(type(one_item_tuple))
# <class 'tuple'>

# ... all characteristics as in Lists ...

"""
to use methods that mutate values in tuple
(change value, append, add, remove, delete)
you have to:
1) convert tuple to list,
2) use method and mutate value
3) convert back list to tuple
"""

# Unpacking Tuple

(a, b, c, d) = tuple_example_01
print(a)  # Stratocaster
print(b)  # Squier
print(c)  # Gibson
print(d)  # Ibanez

# Using Asteriks (*)

"""
The number of variables must match the number of
values in the tuple, if not, you must use an asterisk
to collect the remaining values as a list.
"""

(*fender, les_paul, japanese) = tuple_example_01
print(fender)     # ['Stratocaster', 'Squire']
print(les_paul)   # Gibson
print(japanese)   # Ibanez

# ... all loops are as in Lists ...

# Join and Multiply Tuples

tuple_example_02 = (1, 2, 3, 4, 5)

tuple_example_03 = tuple_example_01 + tuple_example_02
print(tuple_example_03)
# ('Stratocaster', 'Squier', 'Gibson', 'Ibanez', 1, 2, 3, 4, 5)

tuple_example_03 = tuple_example_02 * 3
print(tuple_example_03)
#
