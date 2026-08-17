# Print a Right-Aligned Triangle of Stars 

num = n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

x = 5
for i in range(1,x+1):
    print(" " * (n - i) + "*" * i)