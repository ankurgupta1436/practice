# Check if a number lies within the range [100, 999].

def range_num(num):
    if 100 <= num <= 999:
        return "The number lies between 100 and 999."
    else:
        return "The number does not lie between 100 and 999."

try:
    num = int(input("Enter a number: "))
    print(range_num(num))

except ValueError:
    print("Please enter a valid integer.")