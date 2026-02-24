def hollow_butterfly(n):
    # Upper half
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example
hollow_butterfly(5)