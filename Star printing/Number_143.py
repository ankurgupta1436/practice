# Program to print 143
for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2 or (i == 0 and j == 1) or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 4
    for j in range(5):
        if (j == 0 and i <= 3) or i == 3 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 3
    for j in range(5):
        # Top, middle, bottom rows, and the entire right vertical border
        if i == 0 or i == 3 or i == 6 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
