# Program to pront Letter W
n = 5

for i in range(n):
    for j in range(2 * n - 1):
        if j == i or j == 2 * n - 2 - i or (i >= n // 2 and (j == n - 1 - i or j == n - 1 + i)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
