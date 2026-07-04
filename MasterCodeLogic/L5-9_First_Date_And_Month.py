# Take two dates (day and month) and determine which one comes first in the calendar. 

def first_date(d1, m1, d2, m2):
    if m1 < m2:
        print("First date comes first in the calendar.")
    elif m1 > m2:
        print("Second date comes first in the calendar.")
    else:
        if d1 < d2:
            print("First date comes first in the calendar.")
        elif d1 > d2:
            print("Second date comes first in the calendar.")
        else:
            print("Both dates are the same.")

day1 = int(input("Enter first date (day): "))
month1 = int(input("Enter first date (month): "))

day2 = int(input("Enter second date (day): "))
month2 = int(input("Enter second date (month): "))

first_date(day1, month1, day2, month2)