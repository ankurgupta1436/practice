# Program to print letter J.
for i in range(5):
    for j in range(5):
        if i == 0 or j == 2 or (i == 4 and j < 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
