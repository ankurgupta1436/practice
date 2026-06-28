# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.  

# Check if an amount can be divided into 2000, 500, and 100 currency notes.

def amount(amt):
    if amt % 100 != 0:
        return "The amount cannot be completely divided into 2000, 500, and 100 currency notes."

    notes2000 = amt // 2000
    amt = amt % 2000

    notes500 = amt // 500
    amt = amt % 500

    notes100 = amt // 100

    return (f"2000 notes = {notes2000}\n"
            f"500 notes = {notes500}\n"
            f"100 notes = {notes100}")

try:
    amt = int(input("Enter the amount: "))
    print(amount(amt))

except ValueError:
    print("Please enter a valid amount.")