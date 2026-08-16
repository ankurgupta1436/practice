# Print Square of Stars (n x n Stars) 

num = int(input("Enter the number:"))

for i in range(0,num):
    for j in range(0,num):
        print("*", end="")
    print()