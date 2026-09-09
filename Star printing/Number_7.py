# Program to print 7
for i in range(7):
    for j in range(5):
        if i == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
