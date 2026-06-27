# Take a 3-digit number and check if all digits are distinct.
def distinct_number(a, b ,c):
    if a != b and a != c and b != c :
        return "All three numbers are distinct"
    else:
        return "Either one number or two are same"
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(distinct_number(a,b,c))