def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")