rows = 5

# Upper half
for i in range(1, rows + 1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)

# Lower half
for i in range(rows, 0, -1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)