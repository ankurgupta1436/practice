# Print the sum of all odd numbers up to n.

def sum_odd():
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1, 2):
        total += i

    print("Sum of odd numbers =", total)

sum_odd()