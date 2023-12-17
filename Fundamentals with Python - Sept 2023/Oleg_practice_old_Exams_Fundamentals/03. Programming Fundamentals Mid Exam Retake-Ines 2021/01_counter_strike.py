initial_energy = int(input())
counter_energy = initial_energy
counter_won_battles = 0

while True:
    command = input()

    if command == "End of battle" or counter_energy < 0:
        print(f"Won battles: {counter_won_battles}. Energy left: {counter_energy}")
        break

    distance_to_enemy = int(command)

    if distance_to_enemy <= counter_energy:
        counter_energy -= distance_to_enemy
        counter_won_battles += 1
    else:
        print(f"Not enough energy! Game ends with {counter_won_battles} won battles and {counter_energy} energy")
        break
    if counter_won_battles % 3 == 0:
        counter_energy += counter_won_battles