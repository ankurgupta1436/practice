#  Print the product of digits of a given number.

def product_of_digits():
    n = int(input("Enter the number: "))
    product = 1
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n//10

        print("Product of digits is: ", product)

product_of_digits()