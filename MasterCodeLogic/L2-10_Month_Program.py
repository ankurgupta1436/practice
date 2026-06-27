#  Take a month number (1–12) and print the number of days in that month (ignore leap years). 
def month(num):
    if num == 1:
        return "Month 1 has 31 days"
    elif num == 2:
        return "Month 2 has 28 days"
    elif num == 3:
        return "Month 3 has 31 days"
    elif num == 4:
        return "Month 4 has 30 days"
    elif num == 5:
        return "Month 5 had 31 days"
    elif num == 6:
        return "Month 6 has 30 days"
    elif num == 7:
        return "Month 7 has 31 days"
    elif num == 8:
        return "Month 8 has 31 days"
    elif num == 9:
        return "Month 9 has 30 days"
    elif num == 10:
        return "Month 10 has 31 days"
    elif num == 11:
        return "Month 11 has 30 days"
    elif num == 12:
        return "Month 12 has 31 days"
    else:
        return "Invalid input"
num = int(input("Enter a number from 1-12: "))
print(month(num))