#Take a character and check if it’s a vowel or consonant. 

letter = input("Enter the character: ")

if(letter >= 'A'  and letter <= 'Z' or letter >= 'a' and letter <= 'z'):
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A'  or letter == 'E'  or letter == 'I' or letter == 'O' or letter == 'U' ):
        print(letter, "is a vowel.")
    else:
        print(letter," is a consonant")
else:
    print("Please enter a Character.")