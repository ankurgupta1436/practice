def star_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

star_pyramid(5)