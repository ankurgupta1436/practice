# Program to print 40

for i in range(7):

    # Print 4
    for j in range(5):
        if j == 3:                 # Right vertical line
            print("*", end="")
        elif i == 3:               # Middle horizontal line
            print("*", end="")
        elif j == 0 and i < 3:     # Left vertical line (top half)
            print("*", end="")
        else:
            print(" ", end="")

        print(" ", end="")

    print("  ", end="")

    # Print 0
    for j in range(5):
        if i == 0 or i == 6:       # Top and bottom
            print("*", end="")
        elif j == 0 or j == 4:     # Left and right vertical
            print("*", end="")
        else:
            print(" ", end="")

    print()
