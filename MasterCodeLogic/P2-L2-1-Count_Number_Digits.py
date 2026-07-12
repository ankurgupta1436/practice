# Count the number of digits in a given number.

def count(num):
    num = abs(num)

    if num == 0:
        count = 1
    else:
        count = 0
        while num > 0:
            count += 1
            num //= 10

    return count


num = int(input("Enter a number: "))
print("Number of digits:", count(num))

print('\n')


num = int(input("Enter number: "))

count = len(str(abs(num)))
print("Number of digits: ", count)