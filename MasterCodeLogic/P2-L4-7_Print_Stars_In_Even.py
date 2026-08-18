# Print Stars in Even Numbers (2, 4, 6, 8, 10) 

num = n = 10

for i in range(2, n + 1, 2):
    for j in range(i):
        print("*", end="")
    print()
