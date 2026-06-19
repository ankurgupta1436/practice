# Take three numbers and print the largest.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))

if(num1 > num2 and num1 > num3):
    print("First number is greater")
elif(num1 < num2 and num2 > num3):
    print("Second Number is greater")
else:
    print("Third number is greater")