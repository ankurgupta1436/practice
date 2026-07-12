# Find the sum of digits of a number.

def sum_of_digits():
    num = int(input("Enter the number: "))
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print(f"The sum of {original} is {total}")


sum_of_digits()