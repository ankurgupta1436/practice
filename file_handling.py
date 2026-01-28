# Writing to a file
f = open("data.txt", "w")
f.write("Hello Python")
f.close()

# Reading from a file
f = open("data.txt", "r")
print(f.read())
f.close()