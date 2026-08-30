# Program to print Letter B
n = 5

for i in range(n):
    for j in range(n):
        if j == 0 or (j == 4 and i != 0 and i != 2 and i != 4) or i == 0 or i == 2 or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
