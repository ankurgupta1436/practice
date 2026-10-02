# Program to print 92

for i in range(7):

    # Print 9
    for j in range(5):
        if i == 0 or i == 3:
            print("*", end="")
        elif i < 3 and (j == 0 or j == 4):
            print("*", end="")
        elif i > 3 and j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 2
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif i < 3 and j == 4:
            print("*", end="")
        elif i > 3 and j == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print()
