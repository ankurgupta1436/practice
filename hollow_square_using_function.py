# Hollow Square Pattern - Method 2 (Using Function)

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

size = int(input("Enter the size of square: "))
hollow_square(size)
