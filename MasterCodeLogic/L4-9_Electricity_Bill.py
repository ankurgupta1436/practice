# Take electricity units consumed and calculate the bill as per slabs (using if-else).

def calculate_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

    return bill

try:
    units = float(input("Enter electricity units consumed: "))
    
    if units < 0:
        print("Please enter a valid number of units.")
    else:
        print("Electricity Bill = ₹", calculate_bill(units))
except ValueError:
    print("Please enter a valid numeric value.")