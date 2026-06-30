# Take 24-hour time (hours and minutes) and print whether it is AM or PM. 

def am_pm(hour, minutes):
    if 0 <= hour <= 23 and 0 <= minutes <= 59:
        if hour < 12:
            return "It's AM"
        else:
            return "It's PM"
    else:
        return "Invalid time"

try:
    hour = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    print(am_pm(hour, minutes))
except ValueError:
    print("Invalid input")