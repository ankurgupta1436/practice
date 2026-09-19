# Program to print 51

for i in range(7):

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

    print("  ", end="")

    # Print 1
    for j in range(5):
        if j == 2 or (i == 6 and j >= 1):
            print("*", end="")
        else:
            print(" ", end="")

    print()