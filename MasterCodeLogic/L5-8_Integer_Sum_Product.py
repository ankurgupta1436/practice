# Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.

def check_number(n):
    temp = n
    digit_sum = 0
    digit_product = 1

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_product *= digit
        temp //= 10

    if digit_sum > digit_product:
        print("Sum of digits is greater than the product of digits.")
    else:
        print("Sum of digits is not greater than the product of digits.")


num = int(input("Enter an integer (1-9999): "))

if 1 <= num <= 9999:
    check_number(num)
else:
    print("Please enter a valid number between 1 and 9999.")