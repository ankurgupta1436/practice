n = 5

for i in range(1, n+1):
    num = i % 2
    for j in range(i):
        print(num, end=" ")
        num = 1 - num
    print()