# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

def alphabet(ch):
    if len(ch) != 1:
        return "Please enter only one character"
    elif 'a' <= ch <= 'm':
        return "Character is in between a and m."
    elif 'n' <= ch <= 'z':
        return "Character is in between n and z"
    else:
        return "Invalid input or not a lowercase letter."
ch = input("Enter a character: ")
print(alphabet(ch))