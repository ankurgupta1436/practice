# Take a day number (1–7) and print the corresponding day name.

def day_num(day):
    if 1 == day:
        return "Sunday"
    elif 2 == day:
        return "Monday"
    elif 3 == day:
        return "Tuesday"
    elif 4 == day:
        return "Wednesday"
    elif 5 == day:
        return "Thursday"
    elif 6 == day:
        return "Friday"
    elif 7 == day:
        return "Saturday"
    else:
        return "Please enter numbers from 1-7"
day = int(input("Enter number from 1-7: "))
print(day_num(day))

    