
# Take three numbers and check if they are in geometric progression.
def check_gp(a, b, c):
    if b * b == a * c:
        print("The numbers are in Geometric Progression.")
    else:
        print("The numbers are not in Geometric Progression.")


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

check_gp(a, b, c)