#Progran Demonstrating various tuple operations in Python
# Creating a tuple
tup = (1, 2, 3, 4, 5)
print('Tuple:', tup)

# Accessing elements
print('First element:', tup[0])
print('Last element:', tup[-1])
print('Elements from index 1 to 2:', tup[1:3])



# Slicing
tup2 = tup[1:4]
print('Sliced tuple:', tup2)
# Concatenation
tup3 = tup + (6, 7, 8)
print('Concatenated tuple:', tup3)
# Repetition
tup4 = tup * 2
print('Repeated tuple:', tup4)
print('Updated tuple:', tup)


# Tuple methods
print('Count of 3:', tup.count(3))
print('Index of 4:', tup.index(4))
# Length
print('Length of tuple:', len(tup))
# Membership
print('Is 2 in tuple?:', 2 in tup)
print('Is 10 not in tuple?:', 10 not in tup)
# Iterating through tuple
for item in tup:
    print('Tuple item:', item)
# Nested tuples
nested_tup = (tup, (6, 7, 8))
print('Nested tuple:', nested_tup)



# Immutability check (this will cause an error if uncommented)
#tup[0] = 10