# Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions. 

temp = int(input("Enter the degree: "))

if(temp <= 15):
    print("Cold")
elif(temp >=16 and temp <= 30):
    print("Warm")
else:
    print("Hot")