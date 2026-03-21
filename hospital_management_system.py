# Simple Hospital Management System

patients = []

def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    disease = input("Enter Disease: ")
    patients.append({"id": pid, "name": name, "disease": disease})
    print("Patient added.\n")

def view_patients():
    if not patients:
        print("No patients.\n")
        return
    for p in patients:
        print(p)
    print()

def search_patient():
    pid = input("Enter Patient ID: ")
    for p in patients:
        if p["id"] == pid:
            print(p, "\n")
            return
    print("Not found.\n")

def delete_patient():
    pid = input("Enter Patient ID: ")
    for p in patients:
        if p["id"] == pid:
            patients.remove(p)
            print("Deleted.\n")
            return
    print("Not found.\n")

while True:
    print("1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1": add_patient()
    elif ch == "2": view_patients()
    elif ch == "3": search_patient()
    elif ch == "4": delete_patient()
    elif ch == "5": break
    else: print("Invalid choice\n")