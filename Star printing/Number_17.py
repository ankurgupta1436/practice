# Program to print 17

# Program to print 17

for i in range(7):

    # Print 1
    for j in range(5):
        if j == 2:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 7
    for j in range(5):
        if i == 0:
            print("*", end="")
        elif i > 0 and j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print()
