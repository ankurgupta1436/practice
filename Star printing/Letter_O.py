# Program too print lettr O
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 1 <= j <= 5 or (j == 0 or j == 6) and 1 <= i <= 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()