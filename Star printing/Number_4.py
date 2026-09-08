# Program to print 4

for i in range(7):
    for j in range(5):
        if (j == 0 and i < 4) or i == 3 or (j == 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()
