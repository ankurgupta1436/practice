# Program to pront Letter Y

n = 5

for i in range(n):
    for j in range(n):
        if i == j and i < n // 2 + 1:
            print("*", end=" ")
        elif j == n - 1 - i and i < n // 2 + 1:
            print("*", end=" ")
        elif i >= n // 2 and j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
