# Take a weekday number (1–7) and determine if it is a weekday or weekend

def weekend_day(num):
    if num == 1 or num == 7:
        return "Its Weakend"
    elif num == 2 or num == 3 or num == 4 or num == 5 or num == 6:
        return "Its Weekday"
    else:
        return "Please enter a valid number"
try:
    num = int(input("Enter number from 1-7: "))
    print(weekend_day(num))
except ValueError:
    print("Pleasse enter integers.")






def weekend_day(num):
    if num in [6, 7]:
        return "It's Weekend"
    elif num in [1, 2, 3, 4, 5]:
        return "It's Weekday"
    else:
        return "Please enter a valid number"

try:
    num = int(input("Enter a number from 1 to 7: "))
    print(weekend_day(num))
except ValueError:
    print("Please enter an integer.")





def weekend_day(num):
    if 1 <= num <= 5:
        return "It's Weekday"
    elif 6 <= num <= 7:
        return "It's Weekend"
    else:
        return "Please enter a valid number"

try:
    num = int(input("Enter a number from 1 to 7: "))
    print(weekend_day(num))
except ValueError:
    print("Please enter an integer.")