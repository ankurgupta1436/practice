# Print all factors of a given number. 

def print_factors(n):
    print(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Enter the number: ") )
print_factors(n)