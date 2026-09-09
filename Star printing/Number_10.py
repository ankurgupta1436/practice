# Programt  to print 10 
for i in range(7):
    for j in range(3):
        if j == 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    for j in range(5):
        if i == 0 or i == 6 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")

    print()
