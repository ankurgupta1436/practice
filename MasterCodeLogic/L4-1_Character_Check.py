# Take a character and check if it is a letter, a digit, or neither.

def check_ch(ch):
    if ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z':
        return f"{ch} is a letter."
    elif ch >= '0' and ch <= '9':
        return f"{ch} is a digit."
    else:
        return f"{ch} is neither a letter nor a digit"

ch = input("Enter a character: ")
print(check_ch(ch))