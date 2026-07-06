#  Print the product of digits of a given number.

def product_of_digits():
    num = int(input("Enter a number: "))
    product = 1

    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10

    print("Product of digits =", product)

product_of_digits()