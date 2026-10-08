# Program to print 114

for i in range(7):

    # Print first 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print second 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 4
    for j in range(5):
        if j == 4 or i == 3 or (j == 0 and i < 3):
            print("*", end="")
        else:
            print(" ", end="")

    print()