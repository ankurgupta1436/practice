#  Program to print thr letter G
for i in range(5):
    for j in range(5):
        if i == 0 or j == 0 or i == 4 or j == 4 and i >= 2 or i == 2 and j >= 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
