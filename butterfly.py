n = 5

# Upper wings
for i in range(1, n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)

# Lower wings
for i in range(n, 0, -1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)