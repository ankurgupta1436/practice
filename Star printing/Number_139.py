# Program to print 139

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

    # Print 9
    for j in range(5):
        if i == 0 or i == 3 or j == 4 or (i < 3 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()