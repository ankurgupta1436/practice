# Print all even numbers between 1 and 100.

def even_num():
    num = 1
    while num <= 100:
        if num % 2 == 0:
            print(num)
        num += 1
        

even_num()

print("\n")

def even_number():
    for num in range(2, 101, 2):
        print(num)

even_num()