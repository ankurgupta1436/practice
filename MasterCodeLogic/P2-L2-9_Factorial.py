# Print the factorial of a given number.  
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


n = int(input("Enter a number: "))

result = factorial(n)

print("Factorial of", n, "is:", result)
