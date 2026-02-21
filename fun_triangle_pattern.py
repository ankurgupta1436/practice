def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

# Example usage
rows = int(input("Enter number of rows: "))
right_triangle(rows)