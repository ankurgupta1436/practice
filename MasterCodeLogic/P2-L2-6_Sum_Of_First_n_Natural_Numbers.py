# Print the sum of first n natural numbers. 

def sum_natural():
    num = int(input("Enter the number: "))
    total_sum = num * (num  + 1) // 2
    print(total_sum)

sum_natural()
