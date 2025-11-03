# Creating a list
list = [1, 2, 3, 4, 5]
print('Original list:', list)
print('\n')

# List operations
print('List Operations---')
# Appending an element to the end of the list
list.append(6)
print('After append:', list)
# Inserting an element at index 2
list.insert(2, 10)
print('After insert:', list)
# Removing the element 10
list.remove(10)
print('After remove:', list)
# slicing the list from index 1 to 4
print('Slicing:', list[1:4])
# Updating the first element
list[0] = 9
print('After updating:', list)
# Counting occurrences of element 4
print('Count of 4 in list:', list.count(4))
# Reversing the list
print('Before reversing:', list)
list.reverse()
print('After reversing:', list)
# Deleting the element at index 3
del list[3]
print('After deleting index 3:', list)
# Sorting the list
list.sort()
print('After sorting:', list)
# Extending the list with another list
list.extend([7, 8, 9])
print('After extending:', list)
# Removing specific elements and finding index
list.remove(5)
print('After removing 5:', list)
# Finding index of element 6
list.index(6)
print('Index of 6:', list.index(6))

list2 = list.copy()
print('Copied list2:', list2)
# Length and membership
print('Length:', len(list))
print('Check 4 in list:', 4 in list)
print('Check 10 not in list:', 4 not in list)
print('\n')
# Iterating through list
for num in list:
    print(num)
print('\n')
# popping last element
print('Popping last element:', list.pop(6))
print('List after pop:', list)
#Clearing the list
list.clear()
print(list)


    