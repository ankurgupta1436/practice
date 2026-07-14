# Print the sum of all even numbers up to n.
def sum_of_even_numbers(n):
    k = n // 2
    even_sum = k * (k + 1)
    return even_sum

n = int(input("Enter a number: "))

result = sum_of_even_numbers(n)

print("Sum of even numbers from 1 to", n, "is:", result)
