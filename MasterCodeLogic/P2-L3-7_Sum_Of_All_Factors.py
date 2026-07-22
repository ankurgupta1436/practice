# Find the sum of all factors of a number.
def sum_factors(n):
    print (f"Sum of factors of {n} are")
    sum = 0
    for i in range(1, n + 1 ):
        if n % i == 0:
            sum = sum + i

    return sum
n = int(input("Enter the number: "))
print(sum_factors(n))
