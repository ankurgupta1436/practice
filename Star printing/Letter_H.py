# Prigram to print letter H
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
