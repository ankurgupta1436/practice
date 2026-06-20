# Take marks (0–100) and print the corresponding grade (A/B/C/D/F). 
marks = int(input("Enter your marks: "))

if 0 <= marks <= 100:  # if marks <= 0 and  marks <= 100 (Slide mistakes occurs)
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Enter marks that lies from 0 to 100")
    
