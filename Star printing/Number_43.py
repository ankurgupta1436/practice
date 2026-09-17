# Program to print 43

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
    # Print 3
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print()
