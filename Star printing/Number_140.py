# Program to print 140
for i in range(7):

    # Print 1
    for j in range(5):
        # Stem is at column 2. Serif at top (row 0, col 1). Base at bottom (row 6, cols 0-4).
        if j == 2 or (i == 0 and j == 1) or (i == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 4
    for j in range(5):
        # Left side only goes down to row 3, right side is full height, crossbar at row 3
        if (j == 0 and i <= 3) or i == 3 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Print 0
    for j in range(5):
        # Outer border creates the 0 box
        if i == 0 or i == 6 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
