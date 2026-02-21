def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
rows = int(input("Enter number of rows: "))
number_triangle(rows)