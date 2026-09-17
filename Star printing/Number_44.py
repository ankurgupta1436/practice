# Program to print 44


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

  # Print second 4
    for j in range(5):
        if j == 0 and i < 4:
            print("*", end="")
        elif j == 4:
            print("*", end="")
        elif i == 3:
            print("*", end="")
        else:
            print(" ", end="")

    print()