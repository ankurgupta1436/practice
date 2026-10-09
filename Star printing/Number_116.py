# Program to print 116

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

    # Print 6
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif i == 1 or i == 2:
            if j == 0:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 4 or i == 5:
            if j == 0 or j == 4:
                print("*", end="")
            else:
                print(" ", end="")

    print()