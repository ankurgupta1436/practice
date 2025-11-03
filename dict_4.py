# Creating a dictionary
student = {'Name': 'Ankur Gupta', 'Course': 'C.S.E', 'Branch': 'B.Tech', 'Year': 2, 'College Name': 'KMCLU', 'City': 'Lucknow'}
print('Dictionary:', student)
print('\n')

# Dictionary operations
print('Dictionary Operations---')
# Accessing values
print('Name:', student['Name'])
print('Course:', student.get('Course'))
print('Branch:', student['Branch'])
print('Year:', student['Year'])
print('College Name:', student['College Name'])
print('City:', student['City'])

# Adding a new key-value pair
student['Semester'] = '4th'
print('After adding Semester:', student)
# Updating an existing value
student['Year'] = '3'
print('After updating Year:', student)
# Removing a key-value pair
del student['City']
print('After deleting City:', student)
# Using pop to remove a key-value pair
course = student.pop('Course')
print('After popping Course:', student)
# Using popitem to remove the last inserted key-value pair
popitem = student.popitem()
print('After popping last item:', student) 

# Getting all keys
print('Keys:', student.keys())
# Getting all values
print('Values:', student.values())
# Getting all items
print('Items:', student.items())
# Length of the dictionary
print('Length:', len(student))
print('\n')
# menbership test
print('Is "Name" a key in student?:', 'Name' in student)
print('Is "Name" not a key in student?:', 'Name' not in student)
print('\n')
# Iterating through dictionary
for key, value in student.items():
    print(f'{key}: {value}')
print('\n')


#merging two dictionaries
student2 = student.copy()

student2= {'Name': 'Jhon', 'Hobby': 'Reading', 'Sports': 'Football'}
student.update(student2)
print('After merging with student2:', student)
student3= {'Name': 'Arun Gupta'}
student3.update(student)
print('Merging :', student3)# Clearing the dictionary
student.clear()
print('Cleared Dictionary:', student)