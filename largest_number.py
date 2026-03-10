numbers = input("Enter numbers separated by space: ").split()

largest = int(numbers[0])

for n in numbers:
    n = int(n)
    if n > largest:
        largest = n

print("Largest number is:", largest)