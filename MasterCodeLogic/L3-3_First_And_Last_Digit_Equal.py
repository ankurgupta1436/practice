# Take a 4-digit number and check if the first and last digits are equal.  

def first_last(a,b,c,d):
    if a == d:
        return "First and last digits are equal."
    else:
        return "First and last digit are not same"






a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
print(first_last(a,b,c,d))