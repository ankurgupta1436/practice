# Program to print 70

for i in range(7):

    # Print 7
    for j in range(5):
        if i == 0:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 0
    for j in range(5):
        if i == 0 or i == 6:
            print("*", end="")
        elif j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print()
