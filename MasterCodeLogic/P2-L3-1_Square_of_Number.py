# Print the squares of numbers from 1 to n. 

def square_num(num):
    for i in range(1, num + 1):
        print(i * i)
num = int(input("Enter the number: "))
square_num(num)