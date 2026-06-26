# Take the hour of the day (0–23) and print Good Morning, Good Afternoon, Good Evening, or Good Night.

def hour_day(hour):
    if (hour < 0 and hour > 23):
        return "Invalid Hour"
    if 0 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 15:   
        return "Goodafter Noon"
    elif hour <= 15 and hour < 18:
        return "Good Evening"
    else:
        return "Good Night"
    
hour = int(input("Enter Hour between 0-23: "))
print(hour_day(hour))
    




