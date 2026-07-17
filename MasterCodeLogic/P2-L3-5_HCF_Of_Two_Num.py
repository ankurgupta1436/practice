# Find HCF (GCD) of two numbers using loops. 

def compute_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x   

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    
    result = compute_hcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is {result}")

except ValueError:
    print("Invalid input! Please enter integer values only.")