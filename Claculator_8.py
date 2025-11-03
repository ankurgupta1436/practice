print("Select Operations :")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1/2/3/4):"))
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice==1:
    print("The result is :", num1 + num2)
elif choice==2:
    print("The result is :", num1 - num2)
elif choice==3:
    print("The result is :", num1 * num2)
elif choice==4:
    if num2 != 0:
        print("The result is :", num1 / num2)
    else :
        print("Error:Division by Zero")
else:
    print("Invalid Input")