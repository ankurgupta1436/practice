# Program to print 24
# Program to print 24

# Program to print 24

# Program to print 24

for i in range(7):

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

    print("  ", end="")

    # Print 4
    for j in range(5):
        if j == 4:                 # Right vertical line
            print("*", end="")
        elif i == 3:               # Middle horizontal line
            print("*", end="")
        elif j == 0 and i < 3:     # Left vertical line (top half)
            print("*", end="")
        else:
            print(" ", end="")

    print()

