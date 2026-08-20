#  Print Stars in Odd Numbers (1, 3, 5, 7, 9)
num = n=  10

for i in range(1, n + 1, 2):
    for j in range(i):
        print("*" , end="")
    print()
