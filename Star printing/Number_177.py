for i in range(7):
    # Pattern for '1'
    for j in range(5):
        if j == 2 or (i == 0 and j == 1) or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Pattern for the first '7'
    for j in range(5):
        if i == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Pattern for the second '7'
    for j in range(5):
        if i == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
