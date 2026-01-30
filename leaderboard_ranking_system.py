players = [
    {"name": "Rahul", "score": 450},
    {"name": "Sneha", "score": 520},
    {"name": "Amit", "score": 390}
]
def sort_by_score(players):
    n = len(players)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if players[j]["score"] > players[max_index]["score"]:
                max_index = j
        players[i], players[max_index] = players[max_index], players[i]
    return players
if __name__ == "__main__":      
    sorted_players = sort_by_score(players)
    for player in sorted_players:
        print(f'Name: {player["name"]}, Score: {player["score"]}')