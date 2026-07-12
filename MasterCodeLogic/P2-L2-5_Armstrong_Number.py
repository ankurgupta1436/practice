# Check if a number is an Armstrong number

def armstrong(num):
    original = num 
    total = 0

    digits = len(str(num))

    while num > 0:
        digit = num % 10
        total =  total + (digit ** digits)
        num = num // 10
    return total == original
num = int(input("Enter the number: "))
if armstrong(num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")