# Program to print 107

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

    # Print 7
    for j in range(5):
        if i == 0:
            print("*", end="")
        elif i == 1 and j == 3:
            print("*", end="")
        elif i == 2 and j == 3:
            print("*", end="")
        elif i == 3 and j == 2:
            print("*", end="")
        elif i == 4 and j == 2:
            print("*", end="")
        elif i == 5 and j == 1:
            print("*", end="")
        elif i == 6 and j == 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()