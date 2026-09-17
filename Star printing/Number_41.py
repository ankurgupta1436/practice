# Program to print 41

for i in range(7):

    # Print 4
    for j in range(5):
        if j == 0 and i < 4:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        elif i == 3:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        elif i == 6 and j in range(1, 4):
            print("*", end="")
        else:
            print(" ", end="")

    print()
