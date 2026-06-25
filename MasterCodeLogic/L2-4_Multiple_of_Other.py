# Check if one of two given numbers is a multiple of the other.

def multiple(a, b):
    if a == 0  or b == 0:
        return False
    return a % b == 0 or b % a == 0
a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
if multiple(a,b):
    print("One numberr is the multiple of the other.")
else:
    print("Neither number is a multiple of the other.")