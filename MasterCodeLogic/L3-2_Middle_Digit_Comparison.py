# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 
def middle_element(a,b,c):
    if b > a and b > c:
        return "Middle digit is largest"
    elif b < a and b < c:
        return "Middle digit is smallest"
    else:
        return "None if them are largest"




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(middle_element(a,b,c))