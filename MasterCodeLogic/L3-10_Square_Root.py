#Check whether a number is a perfect square (without using the square root function). 
def is_perfect_square(num):
    if num < 0:
        return False

    for i in range(num + 1):
        if i * i == num:
            return True

    return False



num = 25
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")




# Check whether a number is a perfect square (without using the square root function). 

def perfect_square(num):
    f=0
    for i in range(1, num):
        if i * i == num:
            f=1
            break
    if f == 1:
        return "Number is a perfect suqare."
    else:
        return "Number is not a peerfect square."
num = int(input("Enter a number: "))
print(perfect_square(num))