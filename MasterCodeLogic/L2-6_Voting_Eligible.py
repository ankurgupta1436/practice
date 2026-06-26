# Check voting eligibility for a given age (18+).

def voting(age):
    if age < 18:
        return "Not Eligible for voting"
    if age >= 18:
        return f"{age} age is Eligible for voting"
    
age = int(input("Enter age you want to check: "))
print(voting(age))