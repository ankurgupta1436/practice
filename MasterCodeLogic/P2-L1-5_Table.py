# Print the table of a given number (n × 1 to n × 10).

def table():
    num = int(input("Enter the number: "))

    for i in range (1,11):
        print(f"{num} x {i} = {num * i}")

table()