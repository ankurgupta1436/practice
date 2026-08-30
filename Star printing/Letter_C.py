# Program to print Letter C
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == 4 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
