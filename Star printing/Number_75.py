# Program to print 75

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

    # Print 5
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif i < 3 and j == 0:
            print("*", end="")
        elif i > 3 and j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print()
