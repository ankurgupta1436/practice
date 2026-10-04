# 97
print("\n97")
for i in range(7):

    # Print 9
    for j in range(5):
        if i == 0 or i == 3:
            print("*", end="")
        elif i < 3 and (j == 0 or j == 4):
            print("*", end="")
        elif i > 3 and j == 4:
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