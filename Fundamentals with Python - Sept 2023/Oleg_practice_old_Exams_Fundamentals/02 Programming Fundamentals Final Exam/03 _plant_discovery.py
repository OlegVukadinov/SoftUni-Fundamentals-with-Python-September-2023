n = int(input())
plants = {}

for _ in range(1, n + 1):
    plant, rarity = input().split("<->")
    rarity = int(rarity)

    plants[plant] = {"rarity": rarity, "ratings": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(': ')
    action = current_command[0]

    if action == "Rate":
        plant, rating = current_command[1].split(" - ")
        if plant in plants:
            plants[plant]['ratings'].append(int(rating))
        else:
            print("error")

    elif action == "Update":
        plant, new_rarity = current_command[1].split(" - ")
        if plant in plants:
            plants[plant]['rarity'] = int(new_rarity)
        else:
            print("error")
    elif action == "Reset":
        plant = current_command[1]
        if plant in plants:
            plants[plant]["ratings"] = []
        else:
            print("error")
            continue
print("Plants for the exhibition:")
for key, value in plants.items():
    if plants[key]['ratings']:
        plants[key]['average_rating'] = sum(value['ratings']) / len(value['ratings'])
    else:
        plants[key]["average_rating"] = 0
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['average_rating']:.2f}")

