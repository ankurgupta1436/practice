# Print cubes of numbers from 1 to n.

def cube_num(num):
    for i in range(1, num +1 ):
        print(i * i * i)

num = int(input("Enter the number: "))
cube_num(num)