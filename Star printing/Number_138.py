# Program to print 138

for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 3
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 8
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()