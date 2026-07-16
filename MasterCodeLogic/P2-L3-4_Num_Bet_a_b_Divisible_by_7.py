# Print all numbers between a and b divisible by 7

def divisible_by_7(a,b):
    for number in range(a, b + 1):
        if number % 7 == 0:
            print(number)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

divisible_by_7(a,b)