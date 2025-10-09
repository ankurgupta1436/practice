# Type conversions
x = "15"
y = 2.7
z = 0

print("int():", int(x))             # Convert string to integer
print("float():", float(x))         # Convert string to float
print("str():", str(y))             # Convert float to string
print("bool():", bool(z))           # Convert zero to boolean (False)
print("list():", list("hello"))     # Convert string to list
print("tuple():", tuple([1, 2, 3])) # Convert list to tuple
print("set():", set([1, 2, 2, 3]))  # Convert list to set (duplicates removed)
