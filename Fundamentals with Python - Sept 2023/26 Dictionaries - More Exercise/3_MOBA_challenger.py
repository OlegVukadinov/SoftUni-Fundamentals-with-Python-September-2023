# Create a dictionary to store player data
players = {}

# Continue reading input until "Season end" is encountered
while True:
    input_line = input()
    if input_line == "Season end":
        break

    if "->" in input_line:
        player, position, skill = input_line.split(" -> ")
        skill = int(skill)

        if player in players:
            if position in players[player] and skill > players[player][position]:
                players[player][position] = skill
            elif position not in players[player]:
                players[player][position] = skill
        else:
            players[player] = {position: skill}
    elif "vs" in input_line:
        player1, player2 = input_line.split(" vs ")

        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()) & set(players[player2].keys())

            if common_positions:
                total_skill1 = sum(players[player1][position] for position in common_positions)
                total_skill2 = sum(players[player2][position] for position in common_positions)

                if total_skill1 > total_skill2:
                    del players[player2]
                elif total_skill2 > total_skill1:
                    del players[player1]

# Sort and print the players
sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))
for player, positions in sorted_players:
    print(f"{player}: {sum(positions.values())} skill")
    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")
