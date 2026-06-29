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