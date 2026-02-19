height = 10
width = 7

for i in range(height):
    for j in range(width):
        if i == 0 or i == height-1 or j == 0 or j == width-1:
            print("*", end=" ")
        elif i == height-2 and j == width//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
