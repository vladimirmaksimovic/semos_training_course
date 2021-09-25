# Strings

a = "Hello World!"
print(a)  # "Hello World!"

# Multiline Strings

b = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit...
"""
print(b)

c = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ...
'''
print(c)

# Strings are Arrays

print(a[0])  # H
print(a[1])  # e
print(a[2])  # l
print(a[3])  # l
print(a[4])  # o

# Looping Through a String

for letter in a:  # letter in "a" variable/array
    print(letter)

# String Length

print(len(a))  # 12

# Check String

print("World" in a)  # True

# Conditionali Check String

if "Hello" in a:
    print("Hi there ...")

# Check if NOT

if "Yellow" not in a:
    print("There is only 'Hello', not 'Yellow'")

# Slicing

print(a[1:5])  # ello

# Slice From the Start

print(a[:5])  # Hello

# Slice To the End

print(a[6:])  # World!

# Negative Indexing

print(a[-12:-6])  # Hello

# Upper Case

print(a.upper())  # "HELLO WORLD!"

# Lower Case

print(a.lower())  # "hello world!"

# Remove Whitespace

print(a.strip())

# Replace String

print(a.replace("World", "Python"))  # Hello Python!

# Split String

print(a.split(" "))  # ["Hello", "World!"]

# String Concatenation

d = "Citroen"
e = "C3"
f = d + " " + e
print(f)  # Citroen C3

# String Format

j = "Hello"
k = "{} World!"
print(k.format(j))  # Hello World!

l = "Fiat"
m = "Punto"
n = "2001"
o = "Car brand: {2}, car type: {0}, car year: {1}"
print(o.format(m, n, l))  # Car brand: Fiat, car type: Punto, car year: 2001

# Escape Character "\"

p = "Python \"Escape\" Character"
print(p)  # Python "Escape" Character
