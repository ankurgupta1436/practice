# Print first n terms of an arithmetic progression (a, d).


a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

for i in range(n):
    print(a + i * d, end=" ")