# Check if a number is a strong number (sum of factorials of digits = number). 



def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += factorial(digit)
    temp //= 10

if total == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
