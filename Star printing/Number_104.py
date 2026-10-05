# Program to print 104

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

    # Print 4
    for j in range(5):
        if i == 3:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        elif j == 0 and i < 3:
            print("*", end="")
        else:
            print(" ", end="")

    print()
