# Check if a number is a palindrome. 

def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False
    
num = int(input("Enter the numbers: "))
if palindrome(num):
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not a palindrome") 