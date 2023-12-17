field = []
for _ in range(3):
    row = input().split()
    field.append(row)

def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        # Check rows
        if all(cell == player for cell in field[i]):
            return True
        # Check columns
        if all(row[i] == player for row in field):
            return True
    # Check diagonals
    if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
        return True
    return False

if check_winner("1"):
    print("First player won")

elif check_winner("2"):
    print("Second player won")

else:
    print("Draw!")