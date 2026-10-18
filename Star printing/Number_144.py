# Program to print 144
for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2 or (i == 0 and j == 1) or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 4 (First)
    for j in range(5):
        if (j == 0 and i <= 3) or i == 3 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 4 (Second)
    for j in range(5):
        if (j == 0 and i <= 3) or i == 3 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
