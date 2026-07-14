# Print the sum of all odd numbers up to n. 


def sum_of_odds(n):
    k = (n + 1) // 2
    odd_sum = k ** 2
    return odd_sum


n = int(input("Enter a number: "))
result = sum_of_odds(n)
print("Sum of odd numbers from 1 to", n, "is:", result)