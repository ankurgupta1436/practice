# Take day and month and check if it forms a valid calendar date (ignoring leap years).

def check_date():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))

    if month < 1 or month > 12:
        print("Invalid Date")
    elif month == 2:
        if 1 <= day <= 28:
            print("Valid Date")
        else:
            print("Invalid Date")
    elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
            print("Valid Date")
        else:
            print("Invalid Date")
    else:
        if 1 <= day <= 31:
            print("Valid Date")
        else:
            print("Invalid Date")

check_date()