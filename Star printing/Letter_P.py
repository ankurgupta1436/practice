# Program to print letter P

for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or (j == 4 and i == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()