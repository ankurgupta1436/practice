



def clock_angle():
    hour = int(input("Enter hour (0-12): "))
    minute = int(input("Enter minute (0-59): "))

    # Convert hour to 12-hour format
    hour = hour % 12

    # Calculate angles
    minute_angle = minute * 6
    hour_angle = (hour * 30) + (minute * 0.5)

    # Find difference
    angle = abs(hour_angle - minute_angle)

    # Take smaller angle
    if angle > 180:
        angle = 360 - angle

    print("Smaller angle:", angle, "degrees")

clock_angle()