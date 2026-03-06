n = 5
ch = 65  # ASCII for 'A'

for i in range(1, n+1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()