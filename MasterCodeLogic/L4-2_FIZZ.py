# Take a number and print Fizz if divisible by 3, Buzz if divisible by 5, and FizzBuzz if divisible by both. 

def fizz_divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "None"
try:
    num = int(input("Enter a number: "))
    print(fizz_divisible(num))

except ValueError:
    print("Please enter only numeric number")