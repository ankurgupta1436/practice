# Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

def income_age(age, income):
    if age < 18:
        return "Not Eligible since your age is less than 18"
    if age > 18 and income > 500000:
        return "Eligible for tax"
    elif age > 18 and income < 500000:
        return "Not eligible for tax since income is less than 500000 "
    else:
        return "Invalid Input"
try:
    age = int(input("Enter your age: "))
    income = int(input("Enter your income: "))
    print(income_age(age, income))
except ValueError:
    print("Enter a valid input.")




# def income_age(age, income):
    #if age <= 18:
        #return "Not eligible since your age is 18 or below."
    #elif income > 500000:
      #else:
       # return "Not eligible for tax since income is 500000 or less."

#try:
    #age = int(input("Enter your age: "))
    #income = int(input("Enter your income: "))
    #print(income_age(age, income))   # Correct order
#except ValueError:
    #print("Enter a valid input.")