# Program to print letter Q

for i in range(5):
    for j in range(5):
        if ((i == 0 or i == 4) and j > 0 and j < 4) or \
           (j == 0 or j == 4) and i > 0 and i < 4 or \
           (i == 3 and j == 3) or (i == 4 and j == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()