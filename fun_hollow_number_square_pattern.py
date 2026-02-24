def hollow_number_square(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print(j, end=" ")
            else:
                print("  ", end="")
        print()

# Example
hollow_number_square(5)