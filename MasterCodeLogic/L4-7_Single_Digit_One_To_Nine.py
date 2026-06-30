# Take a single digit (0–9) and print its word form (Zero to Nine).

def one_to_nine(digit):
    if digit == 0:
        return "Zero"
    elif digit == 1:
        return "One"
    elif digit == 2:
        return "Two"
    elif digit == 3:
        return "Three"
    elif digit == 4:
        return "Four"
    elif digit == 5:
        return "Five"
    elif digit == 6:
        return "Six"
    elif digit == 7:
        return "Seven"
    elif digit == 8:
        return "Eight"
    elif digit == 9:
        return "Nine"
    else:
        return "Please enter an integer between 0 and 9."

try:
    digit = int(input("Enter a number between 0 and 9: "))
    print(one_to_nine(digit))
except ValueError:
    print("Please enter a valid integer.")