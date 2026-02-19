n = 6

for i in range(-n, n+1):
    for j in range(-n, n+1):
        if i*i + j*j <= n*n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
