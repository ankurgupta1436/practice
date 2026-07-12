# Print the reverse of a given number.

def reverse_num(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


num = int(input("Enter a number: "))
print("Reversed number:", reverse_num(num))