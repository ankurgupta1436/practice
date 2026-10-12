# Program to print 129

for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 2
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif i == 1 or i == 2:
            if j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 4 or i == 5:
            if j == 0:
                print("*", end="")
            else:
                print(" ", end="")

    print("  ", end="")

    # Print 9
    for j in range(5):
        if i == 0 or i == 3:
            print("*", end="")
        elif i == 1 or i == 2:
            if j == 0 or j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 4 or i == 5:
            if j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 6:
            if j == 0 or j == 4:
                print("*", end="")
            else:
                print(" ", end="")

    print()