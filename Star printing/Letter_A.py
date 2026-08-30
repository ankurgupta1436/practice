n = 5

for i in range(n):
    for j in range(n):
        if (j == 0 or j == n - 1) and i != 0:
            print("*", end=" ")
        elif i == 0 and j == 1:
            print("*", end=" ")
        elif i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n")
      
for i in range(5):
    for j in range(5):
        if (i == 0 and j == 2) or \
           (i == 1 and (j == 1 or j == 3)) or \
           (i == 2) or \
           (i > 2 and (j == 0 or j == 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
