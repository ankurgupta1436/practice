# Take a year and print the corresponding century (e.g., 19th century, 20th century) 

def find_century(year):
    century = (year - 1) // 100 + 1

    if century % 10 == 1 and century % 100 != 11:
        suffix = "st"
    elif century % 10 == 2 and century % 100 != 12:
        suffix = "nd"
    elif century % 10 == 3 and century % 100 != 13:
        suffix = "rd"
    else:
        suffix = "th"

    print(f"{century}{suffix} century")

year = int(input("Enter a year: "))
find_century(year)