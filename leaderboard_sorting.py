# Leaderboard Ranking System using Selection Sort

players = []

def add_player():
    name = input("Enter Player Name: ")
    score = int(input("Enter Score: "))
    players.append({"name": name, "score": score})
    print("Player added successfully.\n")

def display_leaderboard():
    if not players:
        print("No players available.\n")
        return
    rank = 1
    for p in players:
        print(f"Rank {rank}: {p['name']} - {p['score']}")
        rank += 1
    print()

def sort_by_score():
    n = len(players)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if players[j]["score"] > players[max_index]["score"]:
                max_index = j
        players[i], players[max_index] = players[max_index], players[i]
    print("Leaderboard sorted by score (High to Low).\n")

while True:
    print("1. Add Player")
    print("2. Display Leaderboard")
    print("3. Sort by Score")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_player()
    elif choice == 2:
        display_leaderboard()
    elif choice == 3:
        sort_by_score()
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")
