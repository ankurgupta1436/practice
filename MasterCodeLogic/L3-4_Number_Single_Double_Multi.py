# Check whether a given integer is single-digit, double-digit, or multi-digit.

def single_double_multi_digit(num):
    num = abs(num)

    if num <= 9:
        return "Given number is single digit"
    elif num <= 99:
        return "Given number is double digit"
    else:
        return "Given number is multi-digit"

try:
    num = int(input("Enter the number: "))
    print(single_double_multi_digit(num))
except ValueError:
    print("Please enter a valid number.")








#  def single_double_multi_digit(num):
    # num = abs
    # if num >= 0 and num <= 9:
        # return "Given number is single digit"
    # elif num >= 10 and num <= 99:
        # return "Given number is double digit "
    # elif num > 99:
        # return "Given number is Multi-digit"
    # else:
        # return "Please enter a valid number."
# num = int(input("Enter the number: "))
# print(single_double_multi_digit(num)) 
    

