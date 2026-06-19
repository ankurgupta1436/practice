#  Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 

letter = input("Enter a character: ")

if(letter >= 'A' and letter <= 'Z'):
    print(letter, " is in Upper Case")
elif(letter >= 'a' and letter <= 'z'):
    print(letter, " is in lower case")
else:
    print("Only alphabet characters are allowed")