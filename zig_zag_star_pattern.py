rows = 5
cols = 9

for i in range(rows):
    for j in range(cols):
        if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()