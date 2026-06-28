# Take two angles of a triangle and compute the third angle.

def third_angle(angle1, angle2):
    if angle1 > 0 and angle2 > 0 and (angle1 + angle2) < 180:
        angle3 = 180 - (angle1 + angle2)
        return f"The third angle is {angle3}°."
    else:
        return "Invalid angles. The sum of the two angles must be less than 180°."

try:
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    print(third_angle(angle1, angle2))

except ValueError:
    print("Please enter valid numeric values.")