letters = ["P", "Q", "R", "S", "R"]

for letter in letters:
    print("Letter:", letter)

    for i in range(5):
        for j in range(5):

            if letter == "P":
                if j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or (j == 4 and i == 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif letter == "Q":
                if ((j == 0 or j == 4) and i > 0 and i < 4) or (i == 0 or i == 4) and j > 0 and j < 4 or (i == 4 and j == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif letter == "R":
                if j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or (j == 4 and (i == 1 or i == 3)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif letter == "S":
                if i == 0 or i == 2 or i == 4 or (j == 0 and i == 1) or (j == 4 and i == 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

        print()
    print()