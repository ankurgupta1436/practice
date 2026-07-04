# Take a 3-digit number and check if the sum of the first and last digit equals the middle digit. 

def check_number(n):
    first = n // 100
    middle = (n // 10) % 10
    last = n % 10

    if first + last == middle:
        print("Sum of first and last digit is equal to the middle digit.")
    else:
        print("Sum of first and last digit is not equal to the middle digit.")


num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    check_number(num)
else:
    print("Please enter a valid 3-digit number.")