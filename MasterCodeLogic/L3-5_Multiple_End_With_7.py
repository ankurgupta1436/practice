# Check if a number is a multiple of 7 or ends with 7. 

def multiple_of7 (num):
    if num % 7 == 0 and num % 10 == 7:
        return "Number is divisible by 7 and ends with 7."

    elif num % 7 == 0:
        return "It is divisible by 7"
    elif num % 10 == 7:
        return "It ends with 7 "
    else:
        return "Please Enter a valid number."
    
num = int(input("Enter Number: "))
print(multiple_of7(num))