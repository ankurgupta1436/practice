# Program to print 1
for i in range(7):
    for j in range(5):
        if j == 2 or (i == 1 and j == 1) or (i == 2 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
