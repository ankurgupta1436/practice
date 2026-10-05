# Program to print 105

for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 0
    for j in range(5):
        if i == 0 or i == 6 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 5
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif j == 0 and i < 3:
            print("*", end="")
        elif j == 4 and i > 3:
            print("*", end="")
        else:
            print(" ", end="")

    print()
