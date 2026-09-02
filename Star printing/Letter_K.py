# Program to print letter K
for i in range(7):
    for j in range(5):
        if j == 0 or (i == 0 and j == 4) or (i == 1 and j == 3) or (i == 2 and j == 2) or (i == 3 and j == 1) or (i == 4 and j == 2) or (i == 5 and j == 3) or (i == 6 and j == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()