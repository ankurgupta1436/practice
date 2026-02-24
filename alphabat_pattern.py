def alphabet_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()

# Example
alphabet_pattern(5)