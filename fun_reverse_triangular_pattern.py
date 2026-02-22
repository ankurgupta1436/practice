def reverse_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

# Example usage
rows = int(input("Enter number of rows: "))
reverse_triangle(rows)