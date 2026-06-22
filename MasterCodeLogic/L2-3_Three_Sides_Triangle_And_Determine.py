# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene. 

side1 = int(input("Enter left side: "))
side2 = int(input("Enter right side: "))
side3 = int(input("Enter bottom side: "))

# Check if it is a valid triangle
if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):

    if side1 == side2 == side3:
        print("It is an Equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It is an Isosceles triangle.")
    else:
        print("It is a Scalene triangle.")
else:
    print("The sides do not form a valid triangle.")