# Take two numbers and check if both are positive and their sum is less than 100.

def two_sum(num1, num2):
    if num1 > 0 and num2 > 0:
        if num1 + num2 < 100:
            return "Both numbers are positive and their sum is less than 100."
        else:
            return "Both numbers are positive, but their sum is 100 or greater."
    else:
        return "One or both numbers are not positive."

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(two_sum(num1, num2))
except ValueError:
    print("Please enter valid integers.")