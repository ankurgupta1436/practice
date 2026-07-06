# Print the sum of first n natural numbers.

def sum_natural():
    n = int(input("Enter a number: "))
    total = n * (n + 1) // 2
    print("Sum =", total)

sum_natural()