# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

def x_and_y(x, y):
    if x == 0 and y == 0:
        return "The point is at the origin"
    elif x == 0:
        return "It lies on the Y-axis"
    elif y == 0:
        return "It lies on the X-axis"
    else:
        return "It neither lies on the X-axis nor the Y-axis"

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x_and_y(x, y))
except ValueError:
    print("Only Integers valus are allowed to enter")