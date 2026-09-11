# Program to print 12

# Program to print 12

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
        elif i < 3 and j == 4:
            print("*", end="")
        elif i > 3 and j == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print()
