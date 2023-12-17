# Read the number of rows
n = int(input())

# Initialize the grid
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Function to attack a square and update the grid
def attack_square(row, col):
    if 0 <= row < n and 0 <= col < len(grid[row]) and grid[row][col] > 0:
        grid[row][col] -= 1

# Process the attacks
attacks = input().split()
destroyed_ships = 0

for attack in attacks:
    row, col = map(int, attack.split('-'))
    attack_square(row, col)
    if grid[row][col] == 0:
        destroyed_ships += 1

# Print the number of destroyed ships
print(destroyed_ships)