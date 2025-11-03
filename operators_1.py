# Arithmetic Operators
a = 10
b = 3
print('Addition:', a + b)        # 13
print('Subtraction:', a - b)     # 7
print('Multiplication:', a * b)  # 30
print('Division:', a / b)        # 3.333...
print('Floor Division:', a // b) # 3
print('Modulus:', a % b)         # 1
print('Exponent:', a ** b)       # 1000
print('\n')


# Comparison Operators

print('Equal:', a == b)          # False
print('Not Equal:', a != b)      # True
print('Greater Than:', a > b)    # True
print('Less Than:', a < b)       # False
print('Greater or Equal:', a >= b)  # True
print('Less or Equal:', a <= b)     # False
print('\n')



# Logical Operators

c = True
d = False
print('AND:', c and d)           # False
print('OR:', c or d)             # True
print('NOT:', not c)   
print('\n')                      # False

# Assignment Operators


a += 2 # same as a = a + 2
print('a += 2:', a)
a -= 2
print('a -= 2:',a)
a *= 3
print('a *= ', a)
a /= 5
print('a /= 5 :', a)
a %= 2
print('a %= 2:', a)
print('\n')

# Bitwise Operators

e = 5   # (101)
f = 3   # (011)
print('Bitwise AND:', e & f)     # 1
print('Bitwise OR:', e | f)      # 7
print('Bitwise XOR:', e ^ f)     # 6
print('Bitwise NOT:', ~e)        # -6
print('Left Shift:', e << 1)     # 10
print('Right Shift:', e >> 1)    # 2
print('\n')


# Identity Operators
print('Is:', a is b)
print('Is Not:', a is not b)
print('\n')
# Membership Operators
list_1 = [1, 2, 3, 4, 5]
print('In:', 6 in list_1)
print('Not In:', 6 not in list_1)