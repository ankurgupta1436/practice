# Program to print 164
for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2 or (i == 0 and j == 1) or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 6
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or j == 0 or (i >= 3 and j == 4):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 4
    for j in range(5):
        if i == 3 or j == 4 or (j == 0 and i < 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()