def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome.
    Ignores case and non-alphanumeric characters.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal, Panama",
        "No 'x' in Nixon",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "Madam In Eden, I'm Adam"
    ]
    for case in test_cases:
        print(f"'{case}' is a palindrome: {is_palindrome(case)}")