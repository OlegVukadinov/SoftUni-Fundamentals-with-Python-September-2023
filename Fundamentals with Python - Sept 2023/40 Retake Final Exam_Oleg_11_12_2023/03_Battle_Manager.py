people_dict = {}

while True:
    command = input().split(":")
    action = command[0]

    if action == "Results":
        break

    if action == "Add":
        name, health, energy = command[1], int(command[2]), int(command[3])
        if name in people_dict:
            people_dict[name][0] += health
        else:
            people_dict[name] = [health, energy]
    elif action == "Attack":
        attacker, defender, damage = command[1], command[2], int(command[3])

        if attacker in people_dict and defender in people_dict:
            people_dict[defender][0] -= damage
            people_dict[attacker][1] -= 1

            if people_dict[defender][0] <= 0:
                del people_dict[defender]
                print(f"{defender} was disqualified!")

            if people_dict[attacker][1] <= 0:
                del people_dict[attacker]
                print(f"{attacker} was disqualified!")

    elif action == "Delete":
        user_name = command[1]

        if user_name == "All":
            people_dict.clear()
        elif user_name in people_dict:
            del people_dict[user_name]

people_count = len(people_dict)
print(f"People count: {people_count}")

for name, stats in sorted(people_dict.items(), key=lambda x: (x[1][0], x[0])):
    print(f"{name} - {stats[0]} - {stats[1]}")