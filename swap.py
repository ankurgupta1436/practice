# Using third variable
a = 5
b = 10
temp = a
a = b
b = temp
print("Using third variable swap a&b:", a, b)

# Without third variable
x = 4
y = 7
x, y = y, x
print("Without third variable swap x &y:", x, y)
