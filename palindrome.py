# palindrime
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    test_strings = ["Racecar", "hello", "A man, a plan, a canal: Panama", "Python"]
    for s in test_strings:
        result = is_palindrome(s)
        print(f'"{s}" is a palindrome: {result}')