n = 5

# Upper half
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()
