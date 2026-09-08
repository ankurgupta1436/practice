# Program to print 5
for i in range(7):
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or (i < 3 and j == 0) or (i > 3 and j == 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()
