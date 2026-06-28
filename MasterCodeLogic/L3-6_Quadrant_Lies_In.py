#  Take coordinates (x, y) and determine which quadrant the point lies in. 

def quadrant(x,y):
    if x > 0 and y > 0:
        return "The point lies in the 1st quadrant."
    elif x < 0 and y > 0:
        return "The point lies in 2nd quadrant."
    elif x < 0 and y < 0:
        return "The point lies in 3th quadrant."
    elif x > 0 and y < 0:
        return "The point lies in 4 th quadrant."
    elif x == 0 and y == 0:
        return "The point lies at the origin."
    elif x == 0:
        return "The point lies on Y-axis"
    else:
        return "The point lies on X-axis"
    
    
try:
    x = int(input("Enter the x-coordinates:  "))
    y = int(input("Enter the y-coordinates: "))
    print(quadrant(x,y))

except ValueError:
    print("Please enter a valid number.")

