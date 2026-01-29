# Palindrome check for string
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Palindrome check for number
n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
