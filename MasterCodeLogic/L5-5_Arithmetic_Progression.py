# Take three numbers and check if they are in arithmetic progression.

def check_ap():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if (b - a) == (c - b):
        print("Numbers are in Arithmetic Progression")
    else:
        print("Numbers are NOT in Arithmetic Progression")

check_ap()