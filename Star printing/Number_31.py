# Program to print 31

# Program to print 31

for i in range(7):

    # Print 3
    for j in range(5):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print 1
    for j in range(5):
        if j == 2 or i == 6:
            print("*", end="")
        else:
            print(" ", end="")

    print()
