# Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.

def even_odd(a, b):
    
    if a % 2 == 0 and b % 2 == 0:
        return "Both are Even"

    elif a % 2 != 0 and b % 2 != 0:
        return "Both are Odd"
    
    else:
        return "One is even and one is odd"
    
a = int(input("Enter the vlaue of a: "))
b = int(input("Enter the vlaue of b: "))

print(even_odd(a,b))
    
