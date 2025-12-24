# List functions
list1 = [5, 2, 8, 5, 1]
print("Original list:", list1)
list1.append(12)           # Add item
list1.insert(1, 7)         # Insert at index
list1.remove(2)            # Remove item
print("Popped item:", list1.pop())   # Remove and return last item
print("Index of 5:", list1.index(5))
print("Count of 5:", list1.count(5))
list1.sort()               # Sort list
print("Sorted list:", list1)
list1.reverse()            # Reverse list
print("Reversed list:", list1)
list2 = list1.copy()       # Copy list
list1.clear()              # Clear list
print("Cleared list:", list1)

# Tuple functions
tuple1 = (8, 3, 8, 1, 7)
print("Tuple:", tuple1)
print("Index of 8:", tuple1.index(8))
print("Count of 8:", tuple1.count(8))
